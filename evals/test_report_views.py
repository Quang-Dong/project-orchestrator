"""Public deterministic query checks; synthetic data only."""
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

SCRIPT = Path(__file__).resolve().parents[1] / "skills/project-orchestrator/scripts/report_workflow.py"
SPEC = importlib.util.spec_from_file_location("report_views", SCRIPT)
reporter = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(reporter)

def rows(n=25):
    result = []
    for i in range(n):
        result.append(dict(schemaVersion=2, eventId=f"e-{i}", taskId=f"task-{i:04}", attemptId="a",
          eventType="task_started", occurredAt="2026-01-01T00:00:00Z", artifactVersion="r1",
          source="synthetic", role="worker", details={}, missingReasons={}))
    return result

class ViewsTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.metrics = self.root/"metrics.jsonl"
        self.improvements = self.root/"improvements.jsonl"
        self.improvements.write_text("", encoding="utf8")
        self.write(rows())

    def write(self, records):
        self.metrics.write_text("".join(json.dumps(x)+"\n" for x in records), encoding="utf8")

    def run_cli(self, *args):
        run = subprocess.run([sys.executable,"-B",str(SCRIPT),"--metrics",str(self.metrics),
             "--improvements",str(self.improvements),*args],capture_output=True,text=True)
        return run.returncode,json.loads(run.stdout)

    def test_summary_is_default_and_versioned(self):
        code, out = self.run_cli()
        self.assertEqual(code, 0)
        self.assertEqual(out["schemaVersion"], 3)
        self.assertEqual(out["view"], "summary")
        self.assertEqual(out["counts"]["attempts"], 25)
        self.assertNotIn("attempts", out)
        self.assertNotIn("legacyCounts", out)

    def test_full_requires_explicit_view(self):
        code, out = self.run_cli("--view", "full")
        self.assertEqual(code, 0)
        self.assertEqual(out["view"], "full")
        self.assertEqual(out["schemaVersion"], 3)
        self.assertEqual(len(out["attempts"]), 25)
        self.assertIn("inputHashes", out)
        self.assertNotIn("legacyCounts", out)

    def test_full_rejects_query_options_and_summary_rejects_pagination(self):
        for args in [("--view", "full", "--task-id", "task-0000"),
                     ("--view", "full", "--cursor", "anything"),
                     ("--view", "full", "--limit", "20"),
                     ("--view", "summary", "--limit", "20"),
                     ("--cursor", "anything")]:
            with self.subTest(args=args):
                code, out = self.run_cli(*args)
                self.assertEqual(code, 2)
                self.assertFalse(out["valid"])
                self.assertEqual(out["attempts"], [])

    def test_old_records_block_all_views_even_outside_filter(self):
        self.write([*rows(), {"schemaVersion": 1, "eventId": "old"}])
        for args in [(), ("--view", "detail", "--task-id", "task-0000"), ("--view", "full")]:
            code, out = self.run_cli(*args)
            self.assertEqual(code, 2)
            self.assertFalse(out["valid"])
            self.assertEqual(out["attempts"], [])
            self.assertEqual(out["errors"][0]["line"], 26)
            self.assertNotIn("legacyCounts", out)

    def test_default_page_and_continuation_no_duplicates(self):
        code,a=self.run_cli("--view","detail")
        self.assertEqual(code,0); self.assertEqual(len(a["items"]),20)
        self.assertTrue(a["hasMore"])
        code,b=self.run_cli("--view","detail","--cursor",a["nextCursor"])
        self.assertEqual(code,0); self.assertEqual(len(b["items"]),5)
        self.assertFalse(b["hasMore"]); self.assertIsNone(b["nextCursor"])
        ids=[x["data"]["taskId"] for x in a["items"]+b["items"]]
        self.assertEqual(len(set(ids)),25)

    def test_filter_and_unknown_query(self):
        for name,expected in [("task-0002",1),("absent",0)]:
            code,out=self.run_cli("--view","detail","--task-id",name)
            self.assertEqual(code,0); self.assertEqual(out["totalItems"],expected)

    def test_cursor_binds_file_bytes(self):
        _,out=self.run_cli("--view","detail")
        with self.metrics.open("a") as f:f.write("\n")
        code,out=self.run_cli("--view","detail","--cursor",out["nextCursor"])
        self.assertEqual(code,2);self.assertFalse(out["valid"])

    def test_cursor_binds_query_and_limit(self):
        _,out=self.run_cli("--view","detail")
        for args in [("--limit","10"),("--task-id","task-0001")]:
            code,result=self.run_cli("--view","detail","--cursor",out["nextCursor"],*args)
            self.assertEqual(code,2);self.assertFalse(result["valid"])

    def test_invalid_cursors_and_bounds(self):
        for args in [("--cursor","bad!"),("--cursor","W10="),("--limit","0"),("--limit","201")]:
            code,out=self.run_cli("--view","detail",*args)
            self.assertEqual(code,2);self.assertFalse(out["valid"])

    def test_empty_cursor_does_not_silently_restart(self):
        code, out = self.run_cli("--view", "detail", "--cursor", "")
        self.assertEqual(code, 2)
        self.assertFalse(out["valid"])
        self.assertEqual(out["attempts"], [])

    def test_cli_argument_errors_are_versioned_json(self):
        for args in [("--view", "unknown"), ("--view", "detail", "--limit", "wrong")]:
            code, out = self.run_cli(*args)
            self.assertEqual(code, 2)
            self.assertFalse(out["valid"])
            self.assertEqual(out["schemaVersion"], 3)
            self.assertEqual(out["attempts"], [])

    def test_bad_record_outside_filter_blocks(self):
        data=rows();data[-1]["role"]="invalid";self.write(data)
        code,out=self.run_cli("--view","summary","--task-id","task-0000")
        self.assertEqual(code,2);self.assertFalse(out["valid"]);self.assertEqual(out["attempts"],[])

    def test_semantic_error_outside_filter_blocks(self):
        data=rows();data[-1]["eventType"]="accepted";self.write(data)
        code,out=self.run_cli("--view","detail","--task-id","task-0000")
        self.assertEqual(code,2);self.assertFalse(out["valid"])

    def test_summary_size_with_tenfold_history(self):
        self.write(rows(100));_,a=self.run_cli("--view","summary","--task-id","task-0001")
        self.write(rows(1000));_,b=self.run_cli("--view","summary","--task-id","task-0001")
        self.assertEqual(a["counts"],b["counts"])
        self.assertEqual(a["attemptStates"],b["attemptStates"])
        self.assertEqual(len(json.dumps(a)),len(json.dumps(b)))

    def test_file_path_does_not_use_read_text(self):
        with patch.object(Path,"read_text",side_effect=AssertionError("whole-file read")):
            out=reporter.build_report(self.metrics,self.improvements)
        self.assertTrue(out["valid"])

    def test_views_do_not_write(self):
        before={p.name:p.read_bytes() for p in self.root.iterdir()}
        self.run_cli("--view","detail");self.run_cli();self.run_cli("--view","full")
        self.assertEqual(before,{p.name:p.read_bytes() for p in self.root.iterdir()})

    def test_missing_file_is_json_failure(self):
        self.metrics.unlink()
        code,out=self.run_cli("--view","summary")
        self.assertEqual(code,2);self.assertFalse(out["valid"])

    def test_filter_uses_default_summary(self):
        code,out=self.run_cli("--task-id","task-0000")
        self.assertEqual(code,0);self.assertEqual(out["view"],"summary")
        self.assertEqual(out["counts"]["attempts"],1)

if __name__=="__main__": unittest.main()

