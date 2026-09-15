import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "skills/project-orchestrator/scripts/check_policy.py"
SPEC = importlib.util.spec_from_file_location("checker", SCRIPT)
checker = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(checker)


def policy():
    return {"schemaVersion": 1, "projectId": "example-project",
            "mainSession": {"modelEffortOwner": "user"},
            "delegation": {"mechanism": "sessions", "models": [
                {"id": "model-a", "effort": {"mode": "allowlist", "values": ["medium", "high"]}},
                {"id": "model-b", "effort": {"mode": "all_supported"}}]},
            "budget": {"mode": "no_self_imposed_cap", "limits": []},
            "permissions": {"smallDirectWork": True, "externalActions": "separate_authorization"},
            "confirmation": {"status": "confirmed", "at": "2026-01-01T00:00:00Z",
                             "evidence": "Fictional user-approved evaluation policy"}}


RUNTIME = {"mechanisms": ["sessions"], "models": [
    {"id": "model-a", "efforts": ["medium", "high"]},
    {"id": "model-b", "efforts": ["low", "high"]}]}


class PolicyTests(unittest.TestCase):
    def test_config_is_not_dispatch(self):
        self.assertEqual(checker.evaluate(policy())[1]["status"], "policy_valid")

    def test_confirmed_selection(self):
        self.assertEqual(checker.evaluate(policy(), "model-a", "high", RUNTIME, project_id="example-project")[1]["status"],
                         "selection_valid")

    def test_template_blocks(self):
        template = json.loads((ROOT / "skills/project-orchestrator/assets/policy.template.json").read_text())
        self.assertEqual(checker.evaluate(template)[0], 2)

    def test_required_fields_cannot_be_omitted(self):
        for field in policy():
            candidate = policy()
            del candidate[field]
            with self.subTest(field=field):
                self.assertEqual(checker.evaluate(candidate)[0], 2)

    def test_confirmation_and_budget_are_distinct(self):
        for field, value in [("confirmation", {"status": "unconfirmed", "at": None, "evidence": None}),
                             ("budget", {"mode": "unconfirmed", "limits": []})]:
            candidate = policy()
            candidate[field] = value
            self.assertEqual(checker.evaluate(candidate)[0], 2)

    def test_lead_and_external_authority_cannot_expand(self):
        candidate = policy()
        candidate["mainSession"]["modelEffortOwner"] = "orchestrator"
        self.assertEqual(checker.evaluate(candidate)[0], 2)
        candidate = policy()
        candidate["permissions"]["externalActions"] = "automatic"
        self.assertEqual(checker.evaluate(candidate)[0], 2)

    def test_reject_model_and_effort(self):
        self.assertEqual(checker.evaluate(policy(), "other", "high", RUNTIME, project_id="example-project")[0], 3)
        self.assertEqual(checker.evaluate(policy(), "model-a", "ultra", RUNTIME, project_id="example-project")[0], 3)

    def test_all_supported_still_needs_runtime(self):
        self.assertEqual(checker.evaluate(policy(), "model-b", "high", RUNTIME, project_id="example-project")[0], 0)
        self.assertEqual(checker.evaluate(policy(), "model-b", "ultra", RUNTIME, project_id="example-project")[0], 4)

    def test_mechanism_unavailable(self):
        runtime = copy.deepcopy(RUNTIME)
        runtime["mechanisms"] = ["subagents"]
        self.assertEqual(checker.evaluate(policy(), "model-a", "high", runtime, project_id="example-project")[0], 4)

    def test_missing_or_invalid_runtime(self):
        for runtime in [None, {}, {"mechanisms": ["sessions"], "models": []}]:
            self.assertEqual(checker.evaluate(policy(), "model-a", "high", runtime, project_id="example-project")[0], 4)

    def test_conflicting_unknown_and_duplicate_fields(self):
        for mutate in [
            lambda p: p.update({"secretPermission": True}),
            lambda p: p.update({"schemaVersion": True}),
            lambda p: p["delegation"]["models"].append(p["delegation"]["models"][0]),
            lambda p: p["delegation"]["models"][1]["effort"].update({"values": ["high"]}),
            lambda p: p["budget"]["limits"].append({"metric": "tokens"}),
            lambda p: p["confirmation"].update({"at": "2026-01-01"})
        ]:
            candidate = policy()
            mutate(candidate)
            self.assertEqual(checker.evaluate(candidate)[0], 2)

    def test_capped_budget_values_and_units(self):
        candidate = policy()
        valid = {"metric": "money", "amount": 10, "unit": "USD", "scope": "task"}
        candidate["budget"] = {"mode": "capped", "limits": [valid]}
        self.assertEqual(checker.evaluate(candidate)[0], 0)
        for amount in [0, -1, True, float("inf"), float("nan")]:
            invalid = copy.deepcopy(candidate)
            invalid["budget"]["limits"][0]["amount"] = amount
            self.assertEqual(checker.evaluate(invalid)[0], 2)
        invalid = copy.deepcopy(candidate)
        invalid["budget"]["limits"][0].update(metric="tokens", amount=1.5, unit="token")
        self.assertEqual(checker.evaluate(invalid)[0], 2)

    def test_cli_is_read_only_and_json(self):
        with tempfile.TemporaryDirectory() as folder:
            directory = Path(folder)
            p, r = directory / "policy.json", directory / "runtime.json"
            p.write_text(json.dumps(policy()))
            r.write_text(json.dumps(RUNTIME))
            before = {x.name: x.read_bytes() for x in directory.iterdir()}
            process = subprocess.run([sys.executable, str(SCRIPT), "--policy", str(p),
                                      "--model", "model-a", "--effort", "high", "--runtime", str(r),
                                      "--project-id", "example-project"],
                                     capture_output=True, text=True)
            self.assertEqual(process.returncode, 0, process.stderr)
            self.assertEqual(json.loads(process.stdout)["status"], "selection_valid")
            self.assertEqual({x.name: x.read_bytes() for x in directory.iterdir()}, before)
            process = subprocess.run([sys.executable, str(SCRIPT), "--policy", str(p),
                                      "--model", "model-a"], capture_output=True, text=True)
            self.assertEqual(process.returncode, 2)

    def test_duplicate_json_key_does_not_override_policy(self):
        with tempfile.TemporaryDirectory() as folder:
            p = Path(folder) / "policy.json"
            p.write_text('{"schemaVersion":1,"schemaVersion":2}')
            process = subprocess.run([sys.executable, str(SCRIPT), "--policy", str(p)],
                                     capture_output=True, text=True)
            self.assertEqual(process.returncode, 2)
            self.assertEqual(json.loads(process.stdout)["status"], "needs_input")


    def test_missing_or_wrong_project(self):
        self.assertEqual(checker.evaluate(policy(), "model-a", "high", RUNTIME)[0], 2)
        self.assertEqual(checker.evaluate(policy(), "model-a", "high", RUNTIME,
                                         project_id="another-project")[0], 3)

    def test_cli_input_hashes_and_budget_limitations(self):
        import hashlib
        with tempfile.TemporaryDirectory() as folder:
            directory = Path(folder)
            p, r = directory / "p.json", directory / "r.json"
            candidate = policy()
            candidate["budget"] = {"mode": "capped", "limits": [
                {"metric": "tokens", "amount": 1, "unit": "token", "scope": "task"}]}
            p.write_text(json.dumps(candidate))
            r.write_text(json.dumps(RUNTIME))
            result = subprocess.run([sys.executable, "-B", str(SCRIPT), "--policy", str(p),
                                     "--runtime", str(r), "--model", "model-a", "--effort", "high",
                                     "--project-id", "example-project"], capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            output = json.loads(result.stdout)
            self.assertEqual(output["inputHashes"]["policy"], hashlib.sha256(p.read_bytes()).hexdigest())
            self.assertEqual(output["inputHashes"]["runtime"], hashlib.sha256(r.read_bytes()).hexdigest())
            self.assertIn("remaining_budget", output["notVerified"])
            self.assertTrue(output["budgetCheckRequired"])
            self.assertEqual(output["status"], "selection_valid")


if __name__ == "__main__":
    unittest.main()
