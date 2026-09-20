"""Read-only standard-library reporter for workflow v2 JSONL records."""

from datetime import datetime
import argparse
import base64
import hashlib
import json
import math
import sys
from pathlib import Path

METRIC_TYPES = {"task_started", "handoff", "accepted", "repair", "observation", "usage_snapshot"}
ROLES = {"lead", "worker", "reviewer"}
METRIC_FIELDS = {"schemaVersion", "eventId", "taskId", "attemptId", "eventType", "occurredAt", "artifactVersion", "source", "role", "details", "missingReasons"}
IMPROVEMENT_FIELDS = {"schemaVersion", "eventId", "experimentId", "occurredAt", "taskId", "owner", "state", "change", "reviewTrigger", "qualityToPreserve", "measurement", "revertWhen", "previousGuidance", "evidence", "decision", "missingEvidence", "nextReview"}


class RecordError(ValueError):
    """A record is malformed or violates the frozen contract."""


def require_string(value, label):
    if not isinstance(value, str) or not value.strip():
        raise RecordError(f"{label} must be a nonempty string")


def require_object(value, label):
    if not isinstance(value, dict):
        raise RecordError(f"{label} must be an object")


def validate_number(value, label, integer=False):
    if value is None:
        return
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value) or value < 0:
        raise RecordError(f"{label} must be a nonnegative {'integer' if integer else 'finite number'} or null")
    if integer and type(value) is not int:
        raise RecordError(f"{label} must be a nonnegative integer or null")


def parse_time(value):
    require_string(value, "occurredAt")
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise RecordError("occurredAt must be ISO 8601 with timezone") from exc
    if parsed.tzinfo is None:
        raise RecordError("occurredAt must include a timezone")
    return parsed


def parse_json_line(line):
    def reject_duplicate_keys(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise RecordError("duplicate JSON key")
            result[key] = value
        return result

    def reject_constant(value):
        raise RecordError(f"non-finite numeric value {value}")

    return json.loads(line, object_pairs_hook=reject_duplicate_keys, parse_constant=reject_constant)


def validate_metric(record):
    require_object(record, "record")
    if type(record.get("schemaVersion")) is not int or record["schemaVersion"] != 2:
        raise RecordError("unsupported schemaVersion")
    missing = METRIC_FIELDS - record.keys()
    if missing:
        raise RecordError("missing required fields: " + ", ".join(sorted(missing)))
    for field in ("eventId", "taskId", "attemptId", "source"):
        require_string(record[field], field)
    if record["eventType"] not in METRIC_TYPES:
        raise RecordError("unsupported eventType")
    parse_time(record["occurredAt"])
    if record["artifactVersion"] is None:
        require_object(record["missingReasons"], "missingReasons")
        require_string(record["missingReasons"].get("artifactVersion"), "missingReasons.artifactVersion")
    else:
        require_string(record["artifactVersion"], "artifactVersion")
    if record["role"] not in ROLES:
        raise RecordError("role must be lead, worker or reviewer")
    require_object(record["details"], "details")
    require_object(record["missingReasons"], "missingReasons")
    details, reasons = record["details"], record["missingReasons"]
    if record["eventType"] == "repair":
        require_string(details.get("reason"), "details.reason")
    if record["eventType"] == "observation":
        for field in ("avoidableQuestions", "lateDefects", "effortSeconds"):
            if field not in details:
                raise RecordError(f"details.{field} is required")
            validate_number(details[field], f"details.{field}", field != "effortSeconds")
            if details[field] is None:
                require_string(reasons.get(field), f"missingReasons.{field}")
    if record["eventType"] == "usage_snapshot":
        for field in ("inputTokens", "cachedInputTokens", "outputTokens", "reasoningOutputTokens", "billedCost", "allowance"):
            if field not in details:
                raise RecordError(f"details.{field} is required")
        for field in ("inputTokens", "cachedInputTokens", "outputTokens", "reasoningOutputTokens"):
            validate_number(details[field], f"details.{field}", True)
            if details[field] is None:
                require_string(reasons.get(field), f"missingReasons.{field}")
        if details["inputTokens"] is not None and details["cachedInputTokens"] is not None and details["cachedInputTokens"] > details["inputTokens"]:
            raise RecordError("cachedInputTokens cannot exceed inputTokens")
        if details["outputTokens"] is not None and details["reasoningOutputTokens"] is not None and details["reasoningOutputTokens"] > details["outputTokens"]:
            raise RecordError("reasoningOutputTokens cannot exceed outputTokens")
        if details["billedCost"] is None:
            require_string(reasons.get("billedCost"), "missingReasons.billedCost")
        else:
            require_object(details["billedCost"], "details.billedCost")
            amount = details["billedCost"].get("amount")
            validate_number(amount, "billedCost.amount")
            if amount is None:
                raise RecordError("billedCost.amount must be nonnegative finite number")
            currency = details["billedCost"].get("currency")
            if not isinstance(currency, str) or len(currency) != 3 or not currency.isascii() or not currency.isalpha() or not currency.isupper():
                raise RecordError("billedCost.currency must be three ASCII uppercase letters")
        if details["allowance"] is None:
            require_string(reasons.get("allowance"), "missingReasons.allowance")
        else:
            require_object(details["allowance"], "details.allowance")
    return "v2"


def validate_improvement(record):
    require_object(record, "record")
    if type(record.get("schemaVersion")) is not int or record["schemaVersion"] != 2:
        raise RecordError("unsupported schemaVersion")
    missing = IMPROVEMENT_FIELDS - record.keys()
    if missing:
        raise RecordError("missing required fields: " + ", ".join(sorted(missing)))
    for field in ("eventId", "experimentId", "taskId", "owner", "change", "reviewTrigger", "previousGuidance"):
        require_string(record[field], field)
    parse_time(record["occurredAt"])
    if record["state"] not in {"proposed", "trial", "closed"}:
        raise RecordError("unsupported state")
    for field in ("qualityToPreserve", "measurement", "revertWhen"):
        if not isinstance(record[field], list) or not record[field] or any(not isinstance(item, str) or not item.strip() for item in record[field]):
            raise RecordError(f"{field} must be a nonempty string list")
    for field in ("evidence", "missingEvidence"):
        if not isinstance(record[field], list) or any(not isinstance(item, str) or not item.strip() for item in record[field]):
            raise RecordError(f"{field} must be a string list")
    if record["state"] in {"proposed", "trial"} and record["decision"] is not None:
        raise RecordError("decision must be null for proposed/trial")
    if record["state"] == "trial":
        require_string(record["nextReview"], "nextReview")
    if record["state"] == "closed":
        if record["decision"] not in {"adopted", "revised", "reverted", "deferred"}:
            raise RecordError("invalid closed decision")
        if record["decision"] == "deferred":
            if not record["missingEvidence"]:
                raise RecordError("deferred decision requires missingEvidence")
            require_string(record["nextReview"], "nextReview")
        elif not record["evidence"]:
            raise RecordError("closed decision requires evidence")
    return "v2"


def read_records(text, validator, input_name, event_ids):
    records, errors = [], []
    lines = text.splitlines() if isinstance(text, str) else text
    for line_number, line in enumerate(lines, 1):
        if not line.strip():
            continue
        try:
            record = parse_json_line(line)
            validator(record)
            if record["eventId"] in event_ids:
                raise RecordError("duplicate eventId across inputs")
            event_ids.add(record["eventId"])
            records.append(dict(record, _time=parse_time(record["occurredAt"])))
        except (RecordError, json.JSONDecodeError, TypeError, ValueError) as exc:
            errors.append({"input": input_name, "line": line_number, "reason": str(exc)})
    return records, errors


def new_report():
    return {"schemaVersion": 3, "view": "full", "valid": True, "errors": [], "limitations": [], "attempts": [], "effortByRole": {}, "usageSnapshots": [], "experiments": [], "overdueExperimentIds": []}


def group_metrics(records, report):
    groups = {}
    for record in records:
        groups.setdefault((record["taskId"], record["attemptId"]), []).append(record)
    role_effort = {}
    for group_key in sorted(groups):
        events = sorted(groups[group_key], key=lambda item: (item["_time"], item["eventId"]))
        starts = [item for item in events if item["eventType"] == "task_started"]
        handoffs = [item for item in events if item["eventType"] == "handoff"]
        accepted_events = [item for item in events if item["eventType"] == "accepted"]
        if len(accepted_events) > 1:
            raise RecordError(f"multiple accepted events in attempt {group_key[1]}")
        for handoff in handoffs:
            if handoff["artifactVersion"] is None:
                raise RecordError("handoff requires non-null artifactVersion")
        for first, second in zip(handoffs, handoffs[1:]):
            if first["_time"] == second["_time"] and first["artifactVersion"] != second["artifactVersion"]:
                raise RecordError("equal-time conflicting handoffs")
        accepted = accepted_events[0] if accepted_events else None
        if accepted:
            prior_handoffs = [item for item in handoffs if item["_time"] <= accepted["_time"]]
            if not starts or starts[0]["_time"] > accepted["_time"]:
                raise RecordError("accepted event occurs before task_started")
            if not prior_handoffs or prior_handoffs[-1]["artifactVersion"] != accepted["artifactVersion"]:
                raise RecordError("accepted event requires latest matching handoff")
        values = {field: None for field in ("avoidableQuestions", "lateDefects", "effortSeconds")}
        observed_fields = {field: False for field in values}
        limitations = []
        observations = [item for item in events if item["eventType"] == "observation"]
        for observation in observations:
            for field in values:
                value = observation["details"][field]
                if value is None:
                    limitations.append(f"unknown_{field}")
                elif not observed_fields[field]:
                    values[field] = value
                    observed_fields[field] = True
                elif values[field] is not None:
                    values[field] += value
            effort = observation["details"]["effortSeconds"]
            if effort is not None:
                role_effort.setdefault(observation["role"], {"seconds": 0, "complete": True})
                role_effort[observation["role"]]["seconds"] += effort
            else:
                role_effort.setdefault(observation["role"], {"seconds": 0, "complete": True})["complete"] = False
        if not observations:
            limitations.append("observations_not_recorded")
        observed_roles = {item["role"] for item in observations}
        for role in {item["role"] for item in events} - observed_roles:
            role_effort.setdefault(role, {"seconds": 0, "complete": True})["complete"] = False
        report["attempts"].append({"taskId": group_key[0], "attemptId": group_key[1], "roles": sorted({item["role"] for item in events}), "status": "accepted" if accepted else ("handed_off" if handoffs else "in_progress"), "startedAt": starts[0]["occurredAt"] if starts else None, "acceptedAt": accepted["occurredAt"] if accepted else None, "elapsedToAcceptanceSeconds": (accepted["_time"] - starts[0]["_time"]).total_seconds() if accepted and starts else None, "elapsedToAcceptanceReason": None if accepted and starts else "missing start or acceptance", "repairRounds": sum(item["eventType"] == "repair" for item in events), "firstPassAccepted": bool(accepted and not any(item["eventType"] == "repair" for item in events)) if accepted else None, "avoidableQuestions": values["avoidableQuestions"], "lateDefects": values["lateDefects"], "effortSeconds": values["effortSeconds"], "completenessLimitations": sorted(set(limitations))})
        usage_by_role = {}
        for usage in (item for item in events if item["eventType"] == "usage_snapshot"):
            existing = usage_by_role.get(usage["role"])
            if existing and existing["_time"] == usage["_time"] and existing["details"] != usage["details"]:
                raise RecordError("equal-time conflicting cumulative snapshots")
            if existing is None or usage["_time"] > existing["_time"] or (usage["_time"] == existing["_time"] and usage["eventId"] > existing["eventId"]):
                usage_by_role[usage["role"]] = usage
        for role in sorted(usage_by_role):
            usage = usage_by_role[role]
            report["usageSnapshots"].append({"taskId": group_key[0], "attemptId": group_key[1], "role": role, "occurredAt": usage["occurredAt"], "details": usage["details"]})
    report["effortByRole"] = {
        role: data["seconds"] if data["complete"] else {"seconds": None, "complete": False}
        for role, data in sorted(role_effort.items())
    }


def group_improvements(records, report):
    groups = {}
    for record in records:
        groups.setdefault(record["experimentId"], []).append(record)
    accepted_tasks = {attempt["taskId"] for attempt in report["attempts"] if attempt["status"] == "accepted"}
    for experiment_id in sorted(groups):
        events = sorted(groups[experiment_id], key=lambda item: (item["_time"], item["eventId"]))
        for first, second in zip(events, events[1:]):
            if first["_time"] == second["_time"] and first["state"] != second["state"]:
                raise RecordError("equal-time conflicting experiment states")
        latest = events[-1]
        report["experiments"].append({field: latest[field] for field in IMPROVEMENT_FIELDS})
        if latest["state"] == "trial" and latest["taskId"] in accepted_tasks:
            report["limitations"].append(f"active_trial_after_task_acceptance:{experiment_id}")
            report["overdueExperimentIds"].append(experiment_id)
    report["overdueExperimentIds"].sort()


def file_lines(path, digest):
    """Read raw inputs line by line; parsed records still use O(n) memory."""
    with path.open("rb") as stream:
        for line in stream:
            digest.update(line)
            yield line.decode("utf-8")


def build_report(metrics_text, improvements_text, input_hashes=None):
    digests = {name: hashlib.sha256() for name in ("metrics", "improvements")}
    if isinstance(metrics_text, Path):
        metrics_text = file_lines(metrics_text, digests["metrics"])
    else:
        digests["metrics"].update(metrics_text.encode("utf-8"))
    if isinstance(improvements_text, Path):
        improvements_text = file_lines(improvements_text, digests["improvements"])
    else:
        digests["improvements"].update(improvements_text.encode("utf-8"))
    report = new_report()
    event_ids = set()
    metrics, metric_errors = read_records(metrics_text, validate_metric, "metrics", event_ids)
    improvements, improvement_errors = read_records(improvements_text, validate_improvement, "improvements", event_ids)
    if input_hashes is not None:
        input_hashes.update({name: digest.hexdigest() for name, digest in digests.items()})
    report["errors"] = metric_errors + improvement_errors
    if report["errors"]:
        report["valid"] = False
        return report
    try:
        group_metrics(metrics, report)
        group_improvements(improvements, report)
    except RecordError as exc:
        report["valid"] = False
        report["errors"] = [{"input": "semantic", "reason": str(exc)}]
        report["attempts"] = []
        report["effortByRole"] = {}
        report["usageSnapshots"] = []
        report["experiments"] = []
        report["overdueExperimentIds"] = []
    return report


def report_metrics_text(text):
    return build_report(text, "")


def report_metrics(path):
    return build_report(Path(path), "")


def select_view(report, hashes, view, task_id=None, experiment_id=None, limit=20, cursor=None):
    """Views validate the complete report first; cursors bind to input bytes and query."""
    if not report["valid"]:
        return report
    if view not in ("summary", "detail"):
        raise RecordError("expected summary or detail view")
    if not 1 <= limit <= 200:
        raise RecordError("limit must be between 1 and 200")
    if view == "summary" and cursor is not None:
        raise RecordError("cursor is only valid for detail")
    attempts = [r for r in report["attempts"] if task_id is None or r["taskId"] == task_id]
    usage = [r for r in report["usageSnapshots"] if task_id is None or r["taskId"] == task_id]
    experiments = [r for r in report["experiments"]
                   if (task_id is None or r["taskId"] == task_id)
                   and (experiment_id is None or r["experimentId"] == experiment_id)]
    # An experiment query does not imply unrelated metrics belong to that trial.
    if experiment_id is not None:
        attempts, usage = [], []
    result = {
        "schemaVersion": 3, "view": view, "valid": True,
        "errors": [], "inputHashes": hashes,
        "filters": {"taskId": task_id, "experimentId": experiment_id},
        "counts": {"attempts": len(attempts), "experiments": len(experiments), "usageSnapshots": len(usage)},
        "limitations": report["limitations"][:20],
        "limitationsTotal": len(report["limitations"]),
        "validationScope": "all input records before filtering",
    }
    if view == "summary":
        result["attemptStates"] = {state: sum(r["status"] == state for r in attempts)
                                   for state in ("accepted", "handed_off", "in_progress")}
        result["experimentStates"] = {state: sum(r["state"] == state for r in experiments)
                                      for state in ("proposed", "trial", "closed")}
        result["repairRounds"] = sum(r["repairRounds"] for r in attempts)
        result["unknownObservationAttempts"] = sum(bool(r["completenessLimitations"]) for r in attempts)
        result["overdueExperiments"] = sum(r["experimentId"] in report["overdueExperimentIds"] for r in experiments)
        result["detailAvailable"] = any(result["counts"].values())
        return result
    items = ([{"kind": "attempt", "data": r} for r in attempts]
             + [{"kind": "experiment", "data": r} for r in experiments]
             + [{"kind": "usage", "data": r} for r in usage])
    query = {"schemaVersion": 3, "hashes": hashes, "taskId": task_id, "experimentId": experiment_id, "limit": limit, "view": view}
    query_hash = hashlib.sha256(json.dumps(query, sort_keys=True).encode()).hexdigest()
    offset = 0
    if cursor is not None:
        try:
            payload = json.loads(base64.b64decode(cursor.encode("ascii"), altchars=b"-_", validate=True))
            if not isinstance(payload, dict) or payload.get("query") != query_hash:
                raise ValueError()
            offset = payload["offset"]
            if type(offset) is not int or offset <= 0 or offset >= len(items) or offset % limit:
                raise ValueError()
        except (ValueError, TypeError, KeyError, UnicodeError) as exc:
            raise RecordError("invalid or stale cursor; restart the query") from exc
    next_offset = offset + limit
    result.update(items=items[offset:next_offset], totalItems=len(items), offset=offset,
                  hasMore=next_offset < len(items), nextCursor=None)
    if result["hasMore"]:
        result["nextCursor"] = base64.urlsafe_b64encode(
            json.dumps({"query": query_hash, "offset": next_offset}, sort_keys=True).encode()).decode()
    return result


class JsonArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        raise RecordError(message)


def main(argv=None):
    parser = JsonArgumentParser(description=__doc__)
    parser.add_argument("--metrics", required=True)
    parser.add_argument("--improvements", required=True)
    parser.add_argument("--view", choices=("summary", "detail", "full"), default="summary")
    parser.add_argument("--task-id")
    parser.add_argument("--experiment-id")
    parser.add_argument("--limit", type=int)
    parser.add_argument("--cursor")
    view = None
    try:
        args = parser.parse_args(argv)
        view = args.view
        if args.view != "detail" and (args.cursor is not None or args.limit is not None):
            raise RecordError("--cursor and --limit require --view detail")
        if args.view == "full" and (args.task_id is not None or args.experiment_id is not None):
            raise RecordError("full audit does not accept filters; use summary or detail")
        hashes = {}
        report = build_report(Path(args.metrics), Path(args.improvements), hashes)
        report["inputHashes"] = hashes
        if args.view != "full":
            report = select_view(report, hashes, args.view, args.task_id, args.experiment_id,
                                 args.limit if args.limit is not None else 20, args.cursor)
    except (OSError, UnicodeError, RecordError) as exc:
        report = new_report()
        report["valid"] = False
        report["errors"] = [{"input": "query", "reason": str(exc)}]
    if not report["valid"]:
        report["view"] = view
    print(json.dumps(report, ensure_ascii=False, sort_keys=True, separators=(",", ":")))
    return 0 if report["valid"] else 2


if __name__ == "__main__":
    sys.exit(main())
