import requests

URL = "http://127.0.0.1:5000"

print("== Part 1: 5 appeals on real content_ids ==")
passed = 0
for i in range(5):
    sub = requests.post(f"{URL}/submit", json={
        "text": f"Test submission number {i}. I wrote this myself for checking the appeal flow, honestly.",
        "creator_id": f"appeal_test_{i}",
    }).json()
    cid = sub["content_id"]

    r = requests.post(f"{URL}/appeal", json={"content_id": cid, "reasoning": "I wrote this myself."})
    log = requests.get(f"{URL}/log").json()["entries"]
    mine = [e for e in log if e.get("content_id") == cid]
    statuses = [e.get("status") for e in mine]

    ok = r.status_code == 200 and statuses[:1] == ["decided"] and "under_review" in statuses
    passed += ok
    print(f"[{'PASS' if ok else 'FAIL'}] {cid}  appeal={r.status_code}  log statuses={statuses}")
print(f"{passed}/5 passed\n")

print("== Part 2: 3 appeals on a fake content_id ==")
passed = 0
for i in range(3):
    r = requests.post(f"{URL}/appeal", json={"content_id": f"c_doesnotexist{i}", "reasoning": "test"})
    ok = r.status_code < 500 and "error" in r.json()
    passed += ok
    print(f"[{'PASS' if ok else 'FAIL'}] status={r.status_code}  body={r.json()}")
print(f"{passed}/3 passed")
