"""Read-only policy validation. No dispatch, writes, or approval authentication."""
import argparse
import hashlib
import datetime
import json
import math
import re
from pathlib import Path


class Invalid(ValueError):
    pass


def require(condition, message):
    if not condition:
        raise Invalid(message)


def obj(value, keys, label):
    require(isinstance(value, dict), label + " must be an object")
    require(set(value) == set(keys), label + " has missing or unknown fields")
    return value


def text(value):
    return isinstance(value, str) and bool(value.strip())


def unique_strings(values):
    return (isinstance(values, list) and bool(values)
            and all(text(v) for v in values) and len(values) == len(set(values)))


def validate_delegation(delegation):
    obj(delegation, ["mechanism", "models"], "delegation")
    require(delegation["mechanism"] in ("sessions", "subagents"),
            "confirm a coordination mechanism")
    require(isinstance(delegation["models"], list) and delegation["models"],
            "confirm a nonempty worker model list")
    seen = set()
    for model in delegation["models"]:
        obj(model, ["id", "effort"], "model")
        require(text(model["id"]) and model["id"] not in seen, "invalid/duplicate model ID")
        seen.add(model["id"])
        effort = model["effort"]
        require(isinstance(effort, dict), "effort must be an object")
        if effort.get("mode") == "all_supported":
            obj(effort, ["mode"], "all_supported effort")
        else:
            obj(effort, ["mode", "values"], "allowlist effort")
            require(effort["mode"] == "allowlist" and unique_strings(effort["values"]),
                    "confirm a nonempty effort allowlist or all_supported")


def validate_budget(budget):
    obj(budget, ["mode", "limits"], "budget")
    require(budget["mode"] in ("no_self_imposed_cap", "capped"),
            "budget stance is unconfirmed")
    require(isinstance(budget["limits"], list), "budget limits must be a list")
    if budget["mode"] == "no_self_imposed_cap":
        require(not budget["limits"], "no_self_imposed_cap conflicts with limits")
    else:
        require(bool(budget["limits"]), "capped budget needs limits")
        seen_limits = set()
        for limit in budget["limits"]:
            obj(limit, ["metric", "amount", "unit", "scope"], "budget limit")
            require(limit["metric"] in ("tokens", "money"), "unknown budget metric")
            amount = limit["amount"]
            require(type(amount) in (int, float) and math.isfinite(amount) and amount > 0,
                    "budget amount must be positive and finite")
            require(limit["scope"] in ("task", "increment"), "unknown budget scope")
            unit = limit["unit"]
            require(text(unit), "budget unit is required")
            if limit["metric"] == "tokens":
                require(unit == "token" and amount == int(amount),
                        "token limit must be an integer in token units")
            else:
                require(re.fullmatch(r"[A-Z]{3}", unit) is not None,
                        "money limit requires a three-letter currency")
            key = (limit["metric"], unit, limit["scope"])
            require(key not in seen_limits, "duplicate budget limit")
            seen_limits.add(key)


def validate_policy(policy):
    require(isinstance(policy, dict), "policy must be an object")
    require(type(policy.get("schemaVersion")) is int and policy["schemaVersion"] == 2,
            "unsupported policy schemaVersion; expected 2; no automatic migration")
    obj(policy, ["schemaVersion", "projectId", "delegation", "budget", "confirmation"], "policy")
    require(text(policy["projectId"]), "projectId is required")
    if policy["delegation"] is not None:
        validate_delegation(policy["delegation"])
        require(policy["budget"] is not None, "delegation requires a confirmed budget stance")
    if policy["budget"] is not None:
        validate_budget(policy["budget"])
    confirmation = obj(policy["confirmation"], ["status", "at", "evidence"], "confirmation")
    require(confirmation["status"] == "confirmed" and text(confirmation["at"])
            and text(confirmation["evidence"]), "user confirmation is required")
    try:
        timestamp = datetime.datetime.fromisoformat(confirmation["at"].replace("Z", "+00:00"))
    except ValueError as exc:
        raise Invalid("confirmation timestamp is invalid") from exc
    require(timestamp.tzinfo is not None, "confirmation timestamp needs a timezone")
    return policy


def validate_runtime(runtime):
    obj(runtime, ["mechanisms", "models"], "runtime")
    require(unique_strings(runtime["mechanisms"]), "runtime mechanisms are missing/duplicate")
    require(all(v in ("sessions", "subagents") for v in runtime["mechanisms"]),
            "unknown runtime mechanism")
    require(isinstance(runtime["models"], list) and runtime["models"],
            "runtime model inventory is missing")
    seen = set()
    for model in runtime["models"]:
        obj(model, ["id", "efforts"], "runtime model")
        require(text(model["id"]) and model["id"] not in seen, "duplicate runtime model")
        require(unique_strings(model["efforts"]), "runtime effort list is invalid")
        seen.add(model["id"])
    return runtime


def evaluate(policy, model=None, effort=None, runtime=None, project_id=None):
    try:
        validate_policy(policy)
    except (Invalid, TypeError, ValueError, OverflowError) as exc:
        return 2, {"status": "needs_input", "reason": str(exc)}
    if project_id is not None and policy["projectId"] != project_id:
        return 3, {"status": "rejected", "reason": "Policy belongs to a different project."}
    if model is None and effort is None and runtime is None:
        return 0, {"status": "policy_valid",
                   "reason": "Configuration only; no dispatch capability checked."}
    if not text(model) or not text(effort):
        return 2, {"status": "needs_input", "reason": "Dispatch needs model, effort and runtime."}
    if not text(project_id):
        return 2, {"status": "needs_input", "reason": "Selection needs an expected project ID."}
    if policy["delegation"] is None:
        return 3, {"status": "rejected", "reason": "No delegation selection is configured."}
    permitted = next((m for m in policy["delegation"]["models"] if m["id"] == model), None)
    if permitted is None:
        return 3, {"status": "rejected", "reason": "Worker model is outside policy."}
    if (permitted["effort"]["mode"] == "allowlist"
            and effort not in permitted["effort"]["values"]):
        return 3, {"status": "rejected", "reason": "Worker effort is outside policy."}
    try:
        validate_runtime(runtime)
    except (Invalid, TypeError, ValueError) as exc:
        return 4, {"status": "unavailable", "reason": str(exc)}
    actual = next((m for m in runtime["models"] if m["id"] == model), None)
    if policy["delegation"]["mechanism"] not in runtime["mechanisms"]:
        return 4, {"status": "unavailable", "reason": "Coordination mechanism is unavailable."}
    if actual is None or effort not in actual["efforts"]:
        return 4, {"status": "unavailable", "reason": "Requested model/effort is unavailable."}
    return 0, {"status": "selection_valid", "model": model, "effort": effort,
               "mechanism": policy["delegation"]["mechanism"],
               "reason": "Configuration/capability check only; actual authority remains required."}


def load_json(path, raw=None):
    def unique_object(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise Invalid("duplicate JSON key: " + key)
            result[key] = value
        return result
    def reject_constant(value):
        raise Invalid("non-finite JSON number: " + value)
    return json.loads((raw if raw is not None else Path(path).read_bytes()).decode("utf-8-sig"),
                      object_pairs_hook=unique_object, parse_constant=reject_constant)


class JsonArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        raise Invalid(message)


def emit(code, result, policy=None, policy_bytes=None, runtime_bytes=None):
    result["schemaVersion"] = 2
    result["projectId"] = policy.get("projectId") if isinstance(policy, dict) else None
    result["inputHashes"] = {
        "policy": hashlib.sha256(policy_bytes).hexdigest() if policy_bytes is not None else None,
        "runtime": hashlib.sha256(runtime_bytes).hexdigest() if runtime_bytes is not None else None,
    }
    result["notVerified"] = ["approval_authenticity", "runtime_freshness",
                             "remaining_budget", "task_creation_authority"]
    budget = policy.get("budget") if isinstance(policy, dict) else None
    result["budgetCheckRequired"] = budget.get("mode") == "capped" if isinstance(budget, dict) else None
    print(json.dumps(result, ensure_ascii=False))
    return code


def main(argv=None):
    parser = JsonArgumentParser(description=__doc__)
    parser.add_argument("--policy", required=True)
    parser.add_argument("--model")
    parser.add_argument("--effort")
    parser.add_argument("--runtime")
    parser.add_argument("--project-id")
    policy = policy_bytes = runtime_bytes = None
    try:
        args = parser.parse_args(argv)
        policy_bytes = Path(args.policy).read_bytes()
        policy = load_json(args.policy, policy_bytes)
    except (OSError, UnicodeError, ValueError) as exc:
        return emit(2, {"status": "needs_input", "reason": str(exc)}, policy, policy_bytes)
    selection = (args.model, args.effort, args.runtime)
    if any(value is not None for value in selection) and not all(value is not None for value in selection):
        return emit(2, {"status": "needs_input", "reason": "Supply model, effort and runtime together."},
                    policy, policy_bytes)
    runtime = None
    if args.runtime:
        try:
            runtime_bytes = Path(args.runtime).read_bytes()
            runtime = load_json(args.runtime, runtime_bytes)
        except (OSError, UnicodeError, ValueError) as exc:
            return emit(4, {"status": "unavailable", "reason": str(exc)}, policy, policy_bytes, runtime_bytes)
    code, result = evaluate(policy, args.model, args.effort, runtime, args.project_id)
    return emit(code, result, policy, policy_bytes, runtime_bytes)


if __name__ == "__main__":
    raise SystemExit(main())
