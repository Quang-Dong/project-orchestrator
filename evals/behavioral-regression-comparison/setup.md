# Regression comparison runner

The runner evaluates the frozen T1 case `saved-note-preview-after-edit`. Its named check is `tests/test_workspace.py::WorkspaceTests.test_editing_note_refreshes_report_preview`. That method edits learner A's note to `Saved note A`, refreshes the visible workspace, and asserts that the report shows the saved value. On the original source, the expected assertion is the observed stale value `Initial note A` against `Saved note A`.

Run it from the repository root with the checked-in original fixture, its freshly generated manifest, the complete corrected fixture and its manifest, and a new result-directory path beneath `.data/artifacts/regression-comparison/<run-id>`. Manifests are regenerated from the source-only fixtures so this example works when `.data` contains no prior evaluation history:

```powershell
rtk proxy python -B -c "import hashlib,json,pathlib; specs=[('evals/behavioral-bounded-context/fixtures/T1','evals/behavioral-regression-comparison/fixtures/original-T1.manifest.json'),('evals/behavioral-regression-comparison/fixtures/corrected-T1','evals/behavioral-regression-comparison/fixtures/corrected-T1.manifest.json')]; [(lambda root,out: out.write_text(json.dumps({p.relative_to(root).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(p for p in root.rglob('*') if p.is_file())},indent=2)+chr(10),encoding='utf-8'))(pathlib.Path(src),pathlib.Path(dst)) for src,dst in specs]"
rtk proxy python -B evals/compare_regression.py `
  --original evals/behavioral-bounded-context/fixtures/T1 `
  --original-manifest evals/behavioral-regression-comparison/fixtures/original-T1.manifest.json `
  --output evals/behavioral-regression-comparison/fixtures/corrected-T1 `
  --output-manifest evals/behavioral-regression-comparison/fixtures/corrected-T1.manifest.json `
  --regression saved-note-preview-after-edit `
  --results .data/artifacts/regression-comparison/runner-demo
```

The output snapshot must contain the full same fixture file set. The only changed files accepted are `src/workspace.py` and `tests/test_workspace.py`; the output test must retain both original guard methods unchanged and add the frozen selected regression. The baseline copy keeps the original `src/workspace.py` while receiving the selected test file from the output. The corrected copy receives the output source and identical test bytes. Both copies run the named test and full suite using the active Python interpreter.

The command prints one compact JSON record and exits 0 only for the expected witnessed-red and corrected-green pair, 1 for insufficient behavioral evidence, or 2 for invalid/stale inputs. The expected baseline transcripts must also have process exit 1; corrected checks must have process exit 0. Printed output alone cannot establish either result. Actual command arguments, interpreter version, timestamps, durations, exits, source hashes, check logs, and the full result JSON remain under the requested private result directory. Disposable baseline and corrected trees are removed after the checks from the matching `.data/workspaces/regression-comparison/<run-id>` directory. The runner accepts only a fresh direct-child run ID in each owned root, rejects links, junctions and reparse points in path components and snapshot trees, and removes only its exact workspace run. Never place valuable material in the disposable workspace root.

The AST/transcript and process-exit checks do not prove that the selected
assertion executed or caused the baseline failure. Before treating a result as
a defect-specific red/green witness, a reviewer must inspect actual test
execution and confirm the failure's cause.

The original manifest is generated from the unchanged canonical T1 fixture. The corrected fixture contains only the small synthetic corrected T1 source/test material; it is not a copy of a historical log or result. The fixture README records provenance.

This is a narrow comparison tool for trusted, authorized synthetic Python code. It does not provide OS-level isolation, general-purpose test discovery, a reusable acceptance schema, or product verification.
