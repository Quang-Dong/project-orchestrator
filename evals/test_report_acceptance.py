"""Independent CLI acceptance checks; synthetic fixtures, no model-generated wording assertions."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / "skills/project-orchestrator/scripts/report_workflow.py"

def metric(eid, kind, second, revision="r1", details=None):
    return dict(schemaVersion=2, eventId=eid, taskId="task-x", attemptId="attempt-1",
                eventType=kind, occurredAt=f"2026-01-01T00:00:{second:02d}+00:00",
                artifactVersion=revision, source="fixture", role="worker",
                details=details or {}, missingReasons={})

def trial(eid="trial", state="trial", decision=None):
    return dict(schemaVersion=2, eventId=eid, experimentId="experiment-x",
                occurredAt="2026-01-01T00:00:30+00:00", taskId="task-x", owner="lead",
                state=state, change="One bounded fixture change", reviewTrigger="task accepted",
                qualityToPreserve=["same tests"], measurement=["repair rounds"],
                revertWhen=["regression"], previousGuidance="baseline", evidence=["fixture"],
                decision=decision, missingEvidence=[], nextReview="next review")

def base():
    return [metric("start","task_started",0,"r0"),
            metric("handoff","handoff",10), metric("accepted","accepted",20)]

class ReporterAcceptance(unittest.TestCase):
    def run_report(self, metrics, improvements=None):
        with tempfile.TemporaryDirectory() as temp:
            d=Path(temp); m=d/"metrics.jsonl"; i=d/"improvements.jsonl"
            m.write_text("".join(json.dumps(x)+"\n" for x in metrics),encoding="utf8")
            i.write_text("".join(json.dumps(x)+"\n" for x in (improvements or [])),encoding="utf8")
            before={p.name:p.read_bytes() for p in d.iterdir()}
            result=subprocess.run([sys.executable,"-B",str(SCRIPT),"--metrics",str(m),"--improvements",str(i)],
                                  text=True,capture_output=True)
            self.assertEqual({p.name:p.read_bytes() for p in d.iterdir()},before)
            return result.returncode,json.loads(result.stdout)

    def test_elapsed_and_order(self):
        a=base()
        code,out=self.run_report([a[2],a[0],a[1]])
        self.assertEqual(code,0)
        self.assertTrue(out["valid"])
        self.assertEqual(out["attempts"][0]["elapsedToAcceptanceSeconds"],20)

    def test_stale_acceptance_never_succeeds(self):
        a=base(); a[-1]["artifactVersion"]="r2"
        code,out=self.run_report(a)
        self.assertEqual(code,2); self.assertFalse(out["valid"])

    def test_cross_stream_duplicate_id(self):
        code,out=self.run_report(base(),[trial("start")])
        self.assertEqual(code,2); self.assertFalse(out["valid"])

    def test_legacy_is_not_new_measurement(self):
        code,out=self.run_report([{"schemaVersion":1,"taskId":"legacy"},*base()])
        self.assertEqual(code,0)
        self.assertEqual(out["legacyCounts"]["metrics"],1)
        self.assertEqual(len(out["attempts"]),1)

    def test_missing_trial_closure_is_visible(self):
        code,out=self.run_report(base(),[trial()])
        self.assertEqual(code,0)
        self.assertIn("experiment-x",out["overdueExperimentIds"])

    def test_defer_requires_missing_evidence(self):
        code,out=self.run_report(base(),[trial(state="closed",decision="deferred")])
        self.assertEqual(code,2)
        t=trial(state="closed",decision="deferred"); t["missingEvidence"]=["comparison"]
        code,out=self.run_report(base(),[t])
        self.assertEqual(code,0); self.assertEqual(out["overdueExperimentIds"],[])

    def test_counter_snapshots_are_not_added(self):
        a=base()
        for second,n in [(11,100),(21,200)]:
            e=metric("u"+str(n),"usage_snapshot",second,details=dict(
                inputTokens=n,cachedInputTokens=n-10,outputTokens=10,
                reasoningOutputTokens=1,billedCost=None,allowance=None))
            e["missingReasons"]={"billedCost":"unavailable","allowance":"not_applicable"}
            a.append(e)
        code,out=self.run_report(a)
        self.assertEqual(code,0)
        self.assertEqual(len(out["usageSnapshots"]),1)
        def values(x):
            if isinstance(x,dict):
                return [v for k,v in x.items() if k=="inputTokens"]+sum((values(v) for v in x.values()),[])
            if isinstance(x,list): return sum((values(v) for v in x),[])
            return []
        self.assertEqual(values(out["usageSnapshots"]),[200])

    def test_unknown_observation_requires_reason(self):
        a=base()+[metric("o","observation",21,details=dict(
            avoidableQuestions=None,lateDefects=None,effortSeconds=None))]
        code,out=self.run_report(a)
        self.assertEqual(code,2)

    def test_boolean_version_is_not_legacy(self):
        code,out=self.run_report([{"schemaVersion":True}])
        self.assertEqual(code,2)


    def test_absent_observations_stay_unknown(self):
        code,out=self.run_report(base())
        self.assertEqual(code,0)
        for field in ("avoidableQuestions","lateDefects","effortSeconds"):
            self.assertIsNone(out["attempts"][0][field])

    def test_usage_is_grouped_by_role(self):
        records=base()
        for role in ("worker","reviewer"):
            e=metric("u-"+role,"usage_snapshot",21,details=dict(
                inputTokens=100,cachedInputTokens=50,outputTokens=10,
                reasoningOutputTokens=1,billedCost=None,allowance=None))
            e["role"]=role
            e["missingReasons"]={"billedCost":"unavailable","allowance":"not_applicable"}
            records.append(e)
        code,out=self.run_report(records)
        self.assertEqual(code,0)
        self.assertEqual({x["role"] for x in out["usageSnapshots"]},{"worker","reviewer"})

    def test_nullable_usage_fields_require_reasons(self):
        e=metric("u","usage_snapshot",21,details=dict(
            inputTokens=100,cachedInputTokens=50,outputTokens=10,
            reasoningOutputTokens=1,billedCost=None,allowance=None))
        code,out=self.run_report(base()+[e])
        self.assertEqual(code,2)
        self.assertFalse(out["valid"])

    def test_malformed_missing_reasons_is_json_error(self):
        e=metric("bad","task_started",0,None)
        e["missingReasons"]=None
        code,out=self.run_report([e])
        self.assertEqual(code,2)
        self.assertFalse(out["valid"])

    def test_nullable_cost_amount_is_invalid(self):
        e=metric("u","usage_snapshot",21,details=dict(
            inputTokens=100,cachedInputTokens=50,outputTokens=10,
            reasoningOutputTokens=1,billedCost={"amount":None,"currency":"USD"},allowance=None))
        e["missingReasons"]={"allowance":"not_applicable"}
        code,out=self.run_report(base()+[e])
        self.assertEqual(code,2)

    def test_text_api_does_not_write_files(self):
        import importlib.util
        from unittest.mock import patch
        spec=importlib.util.spec_from_file_location("reviewed_reporter",SCRIPT)
        module=importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
        with patch("pathlib.Path.write_text",side_effect=AssertionError("Reporter wrote a file")):
            out=module.report_metrics_text("\n".join(json.dumps(x) for x in base()))
        self.assertTrue(out["valid"])


    def test_partial_role_effort_across_attempts(self):
        a=metric("unknown","observation",1,details=dict(
            avoidableQuestions=None,lateDefects=None,effortSeconds=None))
        a["missingReasons"]={k:"unavailable" for k in a["details"]}
        b=metric("known","observation",2,details=dict(
            avoidableQuestions=0,lateDefects=0,effortSeconds=5))
        b["attemptId"]="attempt-2"
        code,out=self.run_report([a,b])
        self.assertEqual(code,0)
        self.assertFalse(out["effortByRole"]["worker"]["complete"])
        self.assertIsNone(out["effortByRole"]["worker"]["seconds"])

    def test_role_effort_accounts_for_unobserved_attempt(self):
        a=metric("start","task_started",0)
        b=metric("known","observation",2,details=dict(
            avoidableQuestions=0,lateDefects=0,effortSeconds=5))
        b["attemptId"]="attempt-2"
        code,out=self.run_report([a,b])
        self.assertEqual(code,0)
        self.assertFalse(out["effortByRole"]["worker"]["complete"])

if __name__=="__main__": unittest.main()
