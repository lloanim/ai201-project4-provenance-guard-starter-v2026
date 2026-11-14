"""
Measure the cost of one /submit run, in seconds of compute.

Nothing here calls a paid API. The detector runs locally, so the real cost
of a run is how long the server spends on it. This script:

  1. sends one warm-up request (the model loads on the first call, so that
     one is reported separately rather than averaged in),
  2. sends 10 timed requests cycling through a mixed set of 5 texts,
  3. reads each run's `seconds` / `model_seconds` back from the audit log,
     which the server measured with time.perf_counter(),
  4. prints the average.

Rate limit: /submit allows 5 per minute, so requests are spaced 13 s apart.
The full run takes about 2.5 minutes. Start the server first:

    python app.py
    python measure_cost.py
"""

import sys
import time

import requests

URL = "http://127.0.0.1:5000"
RUNS = 10
SPACING_SECONDS = 13  # 60 s / 5 per minute, plus a margin
CREATOR = "cost_measure"
# Mixed set: different lengths and styles, since run time depends on the input.
# The 10 runs cycle through these, so each kind is timed twice.
TEXTS = [
    ("short casual", "Can't believe the bus was late again. Third time this week, honestly."),
    ("medium personal",
     "I spent most of Saturday trying to fix the bike chain that kept slipping. "
     "First I thought it was the derailleur, so I adjusted the screws, but that "
     "made it worse. Then my neighbour pointed out the chain was just stretched. "
     "A new one cost twelve dollars and took ten minutes to put on."),
    ("formal",
     "The committee has reviewed the proposal and concludes that the projected "
     "budget is insufficient to meet the stated objectives. Accordingly, we "
     "recommend that the applicants revise the cost estimates and resubmit "
     "prior to the next review cycle."),
    ("AI-style",
     "In today's fast-paced world, effective time management is more important "
     "than ever. By prioritizing tasks, setting clear goals, and minimizing "
     "distractions, individuals can unlock their full potential. Ultimately, "
     "mastering these skills leads to greater productivity and overall well-being."),
    ("long mixed",
     " ".join([
        "Our community garden started three years ago with six plots and a borrowed hose.",
        "Now there are forty plots, a tool shed, and a waiting list that stretches into next spring.",
        "Furthermore, the garden fosters a sense of belonging and promotes sustainable practices.",
        "Mrs. Alvarez still grows the best tomatoes, and nobody has figured out her secret.",
     ] * 3)),
]


def submit_and_time(text):
    r = requests.post(f"{URL}/submit", json={"text": text, "creator_id": CREATOR}, timeout=120)
    if r.status_code != 200:
        print(f"  got {r.status_code}: {r.text[:200]}")
        return None
    cid = r.json()["content_id"]
    entries = requests.get(f"{URL}/log", params={"limit": 50}, timeout=10).json()["entries"]
    for e in entries:
        if e.get("content_id") == cid and "seconds" in e:
            return e
    print(f"  no timed log entry found for {cid}")
    return None


def main():
    try:
        requests.get(f"{URL}/health", timeout=5)
    except requests.RequestException:
        sys.exit(f"Server isn't answering at {URL}. Run `python app.py` first.")

    print("Warm-up run (includes model load):")
    warm = submit_and_time(TEXTS[0][1])
    if warm:
        print(f"  seconds={warm['seconds']}  model_seconds={warm['model_seconds']}")

    totals, model_totals, by_kind = [], [], {}
    for i in range(1, RUNS + 1):
        time.sleep(SPACING_SECONDS)
        kind, text = TEXTS[(i - 1) % len(TEXTS)]
        e = submit_and_time(text)
        if e:
            totals.append(e["seconds"])
            model_totals.append(e["model_seconds"])
            by_kind.setdefault(kind, []).append(e["seconds"])
            print(f"Run {i:2d} [{kind:15s} {len(text.split()):3d} words]: "
                  f"seconds={e['seconds']}  model_seconds={e['model_seconds']}")

    if not totals:
        sys.exit("No successful runs to average.")
    avg = sum(totals) / len(totals)
    avg_model = sum(model_totals) / len(model_totals)
    print(f"\n{len(totals)} runs · average {avg:.3f} s per run "
          f"(detector {avg_model:.3f} s, {avg_model / avg:.0%} of it)")
    print(f"min {min(totals):.3f} s · max {max(totals):.3f} s")
    print("\nBy kind:")
    for kind, secs in by_kind.items():
        print(f"  {kind:15s} avg {sum(secs) / len(secs):.3f} s over {len(secs)} runs")


if __name__ == "__main__":
    main()
