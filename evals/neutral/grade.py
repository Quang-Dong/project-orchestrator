import copy, hashlib, importlib.util, json, pathlib, sys
root = pathlib.Path(sys.argv[1]).resolve()
spec = importlib.util.spec_from_file_location("trial_requests", root / "requests.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
rows = [
 {"id":"future","status":"open","due_date":"2026-03-16"},
 {"id":"today-progress","status":"in_progress","due_date":"2026-03-15"},
 {"id":"done","status":"completed","due_date":"2026-03-01"},
 {"id":"old-open","status":"open","due_date":"2026-03-14"},
 {"id":"none","status":"open","due_date":None},
 {"id":"today-open","status":"open","due_date":"2026-03-15"},
 {"id":"cancelled","status":"cancelled","due_date":"2026-03-01"},
 {"id":"old-progress","status":"in_progress","due_date":"2025-12-31"},
 {"id":"future-progress","status":"in_progress","due_date":"2026-03-16"}
]
before=copy.deepcopy(rows)
checks={}
try:
 result=module.attention_today(rows,"2026-03-15")
 checks["ordered_selection"]=[x["id"] for x in result]==["today-progress","old-open","today-open","old-progress"]
 checks["no_input_mutation"]=rows==before
 checks["empty"]=module.attention_today([],"2026-03-15")==[]
 checks["caller_day"]= [x["id"] for x in module.attention_today(rows,"2026-03-14")]==["old-open","old-progress"]
except Exception as e:
 checks["exception"]=type(e).__name__+": "+str(e)
print(json.dumps({"sourceSha256":hashlib.sha256((root/"requests.py").read_bytes()).hexdigest(),"checks":checks,"passed":all(v is True for v in checks.values())}))
sys.exit(0 if all(v is True for v in checks.values()) else 1)
