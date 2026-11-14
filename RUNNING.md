# Running Provenance Guard

Provenance Guard is a small web service that guesses whether a piece of text
was written by a person or with AI, explains its guess in plain language, and
lets the writer appeal. It runs entirely on your own machine: **no API key, no
account, nothing sent to a hosted service.**

You start the service in one terminal and talk to it with `curl` from another.

---

## What you need

- **Python 3.11, 3.12 or 3.13** (not 3.14 — `torch` doesn't support it yet)
- About **1.5 GB of free disk** (the libraries plus a ~550 MB language model)
- Two terminal windows

---

## Setup (once)

```bash
python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
python detector.py                 # downloads the model (~550 MB) and scores a sample
python test.py                     # checks the environment
```

You're ready when `python test.py` passes with no `[WARN] Detector model` line.

---

## Run it

**Terminal 1** — start the service and leave it running:

```bash
source .venv/bin/activate
python app.py
```

It listens on `http://127.0.0.1:5000`.

**Terminal 2** — check it's up:

```bash
curl http://127.0.0.1:5000/health
```

### Submit some text

```bash
curl -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d '{"text": "Can'\''t believe the bus was late again. Third time this week, honestly.", "creator_id": "me"}'
```

You get back something like:

```json
{
  "caution": "",
  "confidence": 0.40507,
  "content_id": "c_21390fb882c3",
  "creator_id": "me",
  "formal": false,
  "guess": "human",
  "label": "We think this was probably written by a person.",
  "model_score": 0.3001,
  "style_score": 0.65
}
```

- `guess` is `human`, `unsure` or `ai`; `label` is the sentence shown to the writer.
- `model_score` (how predictable the text is to a language model) and
  `style_score` (sentence-length spread, vocabulary, punctuation) are combined
  70/30 into `confidence`. Below 0.45 reads as human, above 0.80 as AI, and
  anything between is "unsure".
- `formal` / `caution` flag careful, formal writing, which these checks are bad
  at judging, so the writer knows to appeal if the guess is wrong.

**The first submission takes 10–20 seconds** while the model loads into memory.
After that, each one takes about 0.1–0.4 s.

Text must be **50 to 20,000 characters**. Anything else is rejected (`400` or
`413`) and the rejection is logged.

### Appeal a decision

Use the `content_id` from a submit:

```bash
curl -X POST http://127.0.0.1:5000/appeal 
  -H "Content-Type: application/json" 
  -d '{"content_id": "c_0ccb5996d0d6", "reasoning": "I wrote this myself."}'
```

The decision moves to `under_review`. An unknown `content_id` returns `404`.

### Read the audit log

```bash
curl "http://127.0.0.1:5000/log?limit=10"
```

Every decision, appeal and rejection is also written to `logs/audit.jsonl`,
one JSON object per line.

> **On Windows PowerShell, use `curl.exe` and keep the command on one line**,
> escaping the inner quotes:
>
> ```powershell
> curl.exe -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d '{\"text\": \"...at least fifty characters of text here...\", \"creator_id\": \"me\"}'
> ```
>
> In PowerShell plain `curl` is a different tool. Git Bash needs no change.

---

## The routes

| Route | What it does |
|---|---|
| `POST /submit` | Score a piece of text, return a guess and label, log it |
| `POST /appeal` | Contest a decision by `content_id`; moves it to `under_review` |
| `GET /log` | The audit log as JSON (`?limit=N`) |
| `GET /health` | Is the service up, is the model loaded, is rate limiting on |
| `POST /ping` | Echo test — if this answers, the service itself is fine |

---

## Rate limiting

`/submit` allows **5 requests per minute and 50 per day** per caller. The 6th
request within a minute gets `429 rate_limited`, which is also logged. Wait a
minute and it clears. Limits live in `config.py` (`RATE_LIMIT_PER_MINUTE`,
`RATE_LIMIT_PER_DAY`).

---

## Tests and measurements

Run these with the service running in the other terminal unless noted.

| Command | What it does | Time |
|---|---|---|
| `python test.py` | Environment check (no server needed) | seconds |
| `python test_style.py` | Prints both signals on four sample texts (no server needed) | seconds |
| `python test_formality.py` | Runs the formal-writing check on sample essays (no server needed) | seconds |
| `python test_appeals.py` | Appeals on real and fake `content_id`s, checks the log | ~1 min |
| `python measure_cost.py` | Times 10 submissions over 5 mixed texts and prints the average | ~2.5 min |
| `python run_attacks.py --set attack_set` | Runs the attack set, writes results to `results/` | several min |
| `python run_attacks.py --flood 15` | Sends 15 quick submissions to show the `429`s | seconds |
| `python run_eval.py --label <name>` | Runs the five criteria in `criteria.md`, three trials each | several min |
| `python detector.py "some text"` | Score one text with signal one only | seconds |
| `python stylometry.py "some text"` | Score one text with signal two only | seconds |

Scripts that submit a lot (`measure_cost.py`, `test_appeals.py`) pace
themselves or may hit the rate limit; if you see `429`, wait a minute and
re-run.

---

## Where things live

| File | What it does |
|---|---|
| `app.py` | The service and its routes |
| `config.py` | Every setting: model, signal weights, label thresholds, rate limits |
| `detector.py` | Signal one — local GPT-2 predictability score |
| `stylometry.py` | Signal two — sentence-length spread, vocabulary, punctuation |
| `scoring.py` | Combines the signals and turns the score into a label |
| `formality.py` | Detects formal writing, which triggers the caution message |
| `audit.py` | Writes and reads the audit log |
| `logs/audit.jsonl` | The audit log |
| `results/` | Attack runs and evaluation results |
| `criteria.md` | The five criteria the system is evaluated against |

---

## Known limits

- **Plain, simple writing can be mistaken for AI.** Signal one rewards predictable text, so writers using common words in short sentences — second-language writers, younger writers — can score like a machine.
- **Signal two can't read.** Typos, broken-up sentences or a pasted quote move it without changing what the text says.
- **Formal writing is hard to judge**, which is why it gets a caution and an appeal prompt instead of a confident label.

---

## When something goes wrong

| What you see | What it means |
|---|---|
| `curl: (7) Failed to connect` | The service isn't running. Start `python app.py` in the other terminal |
| `404` from curl | Check the path is exactly `/submit`, `/appeal`, `/log` |
| `400 too_short` / `413 too_large` | Text must be 50–20,000 characters |
| `429 rate_limited` | More than 5 submissions in a minute. Wait and retry |
| `Cannot bind parameter 'Headers'` | You're in PowerShell. Use `curl.exe`, on one line |
| Request body arrives empty | Add `-H "Content-Type: application/json"` |
| `Address already in use` | A server from an earlier run is still going. Stop it (Ctrl+C in its terminal, or kill the process) |
| First submission takes 10+ seconds | Normal — the model is loading. Later ones are fast |
| `DetectorUnavailable` | Run `python detector.py` once to download the model |
| `/appeal` returns `404` | That `content_id` isn't in the log — copy it exactly from the submit response |
| `pip install` fails on `torch` | Check `python --version` is 3.11–3.13 |
