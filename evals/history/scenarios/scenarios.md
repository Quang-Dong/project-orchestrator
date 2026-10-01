# Behavioral evaluation

Give the evaluator only scenarios.json and the minimal assigned skill references for the treatment condition. Keep rubric.json out of evaluator inputs. Use the same model/effort and fictional inputs for an independent no-skill control. Ask for decisions, questions and evidence, not real implementation or dispatch. Record exact input/skill hashes and any contamination. Grade observed actions against the held-out rubric; this small exercise cannot establish a universal quality or cost advantage.

For a changed policy checker, run test_policy.py. It covers missing/ambiguous approval, allowed versus available selection, role/settings boundaries, budget types and read-only CLI behavior.
