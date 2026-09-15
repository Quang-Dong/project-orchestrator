import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).parents[1] / "skills" / "project-orchestrator" / "scripts" / "report_workflow.py"
spec = importlib.util.spec_from_file_location("report_workflow", SCRIPT)
report_workflow = importlib.util.module_from_spec(spec)
spec.loader.exec_module(report_workflow)


def event(event_type, event_id, occurred_at, details=None, missing=None, **extra):
    return {
        "schemaVersion": 2,
        "eventId": event_id,
        "taskId": "task-1",
        "attemptId": "attempt-1",
        "eventType": event_type,
        "occurredAt": occurred_at,
        "artifactVersion": "artifact-1",
        "source": "evidence/test.json",
        "role": "worker",
        "details": details or {},
        "missingReasons": missing or {},
        **extra,
    }


def lines(*records):
    return "\n".join(json.dumps(record, separators=(",", ":")) for record in records)


class MetricReportTests(unittest.TestCase):
    def test_groups_out_of_order_events_and_acceptance(self):
        report = report_workflow.report_metrics_text(lines(
            event("accepted", "e3", "2026-09-15T10:00:03+07:00"),
            event("handoff", "e2", "2026-09-15T10:00:02+07:00"),
            event("task_started", "e1", "2026-09-15T10:00:00+07:00"),
        ))
        self.assertTrue(report["valid"], report)
        self.assertEqual(report["attempts"][0]["status"], "accepted")
        self.assertEqual(report["attempts"][0]["elapsedToAcceptanceSeconds"], 3.0)
        self.assertTrue(report["attempts"][0]["firstPassAccepted"])

    def test_observations_and_latest_usage_are_not_double_counted(self):
        observation = event(
            "observation", "obs", "2026-09-15T10:00:01+07:00",
            {"avoidableQuestions": 2, "lateDefects": 1, "effortSeconds": 12.5},
        )
        usage1 = event(
            "usage_snapshot", "use-1", "2026-09-15T10:00:02+07:00",
            {"inputTokens": 10, "cachedInputTokens": 3, "outputTokens": 8,
             "reasoningOutputTokens": 2, "billedCost": {"amount": 0.2, "currency": "USD"},
             "allowance": {"remaining": 90}},
        )
        usage2 = dict(usage1)
        usage2["eventId"] = "use-2"
        usage2["occurredAt"] = "2026-09-15T10:00:04+07:00"
        usage2["details"] = dict(usage1["details"], inputTokens=12, outputTokens=9)
        report = report_workflow.report_metrics_text(lines(observation, usage1, usage2))
        self.assertTrue(report["valid"], report)
        self.assertEqual(report["attempts"][0]["avoidableQuestions"], 2)
        self.assertEqual(report["attempts"][0]["lateDefects"], 1)
        self.assertEqual(report["attempts"][0]["effortSeconds"], 12.5)
        self.assertEqual(len(report["usageSnapshots"]), 1)
        self.assertEqual(report["usageSnapshots"][0]["details"]["inputTokens"], 12)
        self.assertEqual(report["effortByRole"]["worker"], 12.5)

    def test_null_fields_require_reasons_and_preserve_incompleteness(self):
        record = event(
            "observation", "obs", "2026-09-15T10:00:00+07:00",
            {"avoidableQuestions": None, "lateDefects": 0, "effortSeconds": None},
            {"avoidableQuestions": "not recorded", "effortSeconds": "not recorded"},
        )
        report = report_workflow.report_metrics_text(json.dumps(record))
        self.assertTrue(report["valid"], report)
        attempt = report["attempts"][0]
        self.assertIsNone(attempt["avoidableQuestions"])
        self.assertEqual(attempt["lateDefects"], 0)
        self.assertIsNone(attempt["effortSeconds"])
        self.assertTrue(attempt["completenessLimitations"])

    def test_rejects_malformed_duplicate_keys_unsupported_and_naive_time(self):
        duplicate = '{"schemaVersion":2,"schemaVersion":2}'
        report = report_workflow.report_metrics_text(duplicate)
        self.assertFalse(report["valid"])
        self.assertEqual(report["errors"][0]["line"], 1)
        bad = event("task_started", "e1", "2026-09-15T10:00:00")
        bad["schemaVersion"] = 9
        report = report_workflow.report_metrics_text(json.dumps(bad))
        self.assertFalse(report["valid"])
        bad["schemaVersion"] = 2
        bad["eventType"] = "unknown"
        report = report_workflow.report_metrics_text(json.dumps(bad))
        self.assertFalse(report["valid"])

    def test_acceptance_requires_latest_matching_handoff(self):
        records = [
            event("task_started", "start", "2026-09-15T10:00:00+07:00"),
            event("handoff", "h1", "2026-09-15T10:00:01+07:00"),
            event("handoff", "h2", "2026-09-15T10:00:02+07:00", extra="ignored"),
            event("accepted", "accept", "2026-09-15T10:00:03+07:00"),
        ]
        records[-2]["artifactVersion"] = "artifact-2"
        report = report_workflow.report_metrics_text(lines(*records))
        self.assertFalse(report["valid"])
        self.assertTrue(any("matching handoff" in e["reason"] for e in report["errors"]))

    def test_legacy_records_are_counted_not_aggregated_and_empty_is_valid(self):
        legacy = {"schemaVersion": 1, "eventId": "old", "taskId": "old"}
        report = report_workflow.report_metrics_text(lines(legacy))
        self.assertTrue(report["valid"], report)
        self.assertEqual(report["legacyCounts"]["metrics"], 1)
        self.assertEqual(report["attempts"], [])
        self.assertIn("legacy_records_not_aggregated", report["limitations"])
        empty = report_workflow.report_metrics_text("\n \n")
        self.assertTrue(empty["valid"])
        self.assertEqual(empty["attempts"], [])


if __name__ == "__main__":
    unittest.main()


class FinalContractTests(unittest.TestCase):
    def improvement(self, state="proposed", decision=None, event_id="i1", experiment="exp-1", task="task-1", **kw):
        return {"schemaVersion": 2, "eventId": event_id, "experimentId": experiment,
                "occurredAt": kw.pop("occurred_at", "2026-09-15T10:00:00+07:00"),
                "taskId": task, "owner": "worker", "state": state, "change": "bounded change",
                "reviewTrigger": "close task", "qualityToPreserve": ["correctness"],
                "measurement": ["defects"], "revertWhen": ["quality drops"],
                "previousGuidance": "old", "evidence": kw.pop("evidence", ["evidence/a"]),
                "decision": decision, "missingEvidence": kw.pop("missing", ["baseline"]),
                "nextReview": kw.pop("next_review", "next task")}

    def test_end_to_end_closure_and_open_trial_warning(self):
        metrics = lines(event("task_started", "m1", "2026-09-15T10:00:00+07:00"),
                        event("handoff", "m2", "2026-09-15T10:00:01+07:00"),
                        event("accepted", "m3", "2026-09-15T10:00:02+07:00"))
        improvements = "\n".join(json.dumps(x) for x in [
            self.improvement("trial", event_id="i1"),
            self.improvement("closed", "deferred", event_id="i2", occurred_at="2026-09-15T10:00:03+07:00", missing=["baseline unavailable"], next_review="after baseline")])
        with tempfile.TemporaryDirectory() as d:
            mp=Path(d)/"m";ip=Path(d)/"i";mp.write_text(metrics);ip.write_text(improvements)
            r=report_workflow.build(mp,ip)
        self.assertTrue(r["valid"], r);self.assertEqual(r["experiments"][-1]["decision"], "deferred")

    def test_cross_stream_duplicate_id_and_bad_deferred(self):
        m=json.loads(event_line := lines(event("task_started", "same", "2026-09-15T10:00:00+07:00")))
        bad=self.improvement("closed", "deferred", event_id="same", missing=[], next_review=None)
        with tempfile.TemporaryDirectory() as d:
            mp=Path(d)/"m";ip=Path(d)/"i";mp.write_text(event_line);ip.write_text(json.dumps(bad))
            r=report_workflow.build(mp,ip)
        self.assertFalse(r["valid"]);self.assertGreaterEqual(len(r["errors"]), 1)

    def test_trial_after_acceptance_is_explicitly_overdue(self):
        metrics=lines(event("task_started","m1","2026-09-15T10:00:00+07:00"),event("handoff","m2","2026-09-15T10:00:01+07:00"),event("accepted","m3","2026-09-15T10:00:02+07:00"))
        with tempfile.TemporaryDirectory() as d:
            mp=Path(d)/"m";ip=Path(d)/"i";mp.write_text(metrics);ip.write_text(json.dumps(self.improvement("trial")))
            r=report_workflow.build(mp,ip)
        self.assertTrue(r["valid"]);self.assertEqual(r["overdueExperimentIds"],["exp-1"])

    def test_cli_exit_and_read_only_hashes(self):
        with tempfile.TemporaryDirectory() as d:
            mp=Path(d)/"m";ip=Path(d)/"i";mp.write_text("");ip.write_text("");before=(mp.stat().st_mtime_ns,ip.stat().st_mtime_ns)
            import subprocess,sys
            p=subprocess.run([sys.executable,"-B",str(SCRIPT),"--metrics",str(mp),"--improvements",str(ip)],capture_output=True,text=True)
            self.assertEqual(p.returncode,0);self.assertTrue(json.loads(p.stdout)["valid"]);self.assertEqual(before,(mp.stat().st_mtime_ns,ip.stat().st_mtime_ns))
