# Acceptance criteria — Provenance Guard

Five criteria that say what "working" means for this service, written in unit 7
**before** you built it.

**All five are yours.** None are given.

An acceptance criterion names a number or something plainly observable. *"The
detector is accurate"* is an opinion — and perfect AI detection isn't possible
anyway, so it's an opinion about something nobody can deliver. *"Of 10 pieces I
wrote myself, at most 1 is labelled high-confidence AI"* is a criterion.

Under each, write a sentence or two on **why that target**. *"I allow at most 1
false positive in 10 because on a writing site a wrong accusation costs more
than a missed detection"* is a real answer.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## Pick numbers you can defend

**Cover at least three of these five areas.** They're prompts, not a form.

| Area | A question it could answer |
|---|---|
| False positives | How often may a human's writing get called AI? |
| Score spread | How far apart should clearly-AI and clearly-human text score? |
| Label coverage | Is every one of your three labels actually reachable? |
| The appeal path | Does an appeal always change status and always get recorded? |
| Bad input | What happens when `text` is missing, empty, or enormous? |

Two things worth knowing before you pick numbers:

- **The expensive mistake is one-sided.** Missing some AI text costs the site a
  little. Accusing a real writer costs that person a lot. A criterion that
  treats both errors as equally bad is describing a system nobody would ship.
- **Unit 8 tests across three trials, and the target has to hold across all
  three.** Your first signal runs a model, so identical input can score
  differently twice. A target of "at most 1 in 10" against trials of 2, 1, 2 is
  a **miss**.

---
## 1. Of 10 pieces I wrote myself in scenarios.py, at most 1 is labelled high-confidence AI, in each of 3 trials

<!-- Your criterion. It must name a number. -->



**Why this target:**
I chose 10 so there is more chance to see how reliable the system is in scoring the human text as not AI. A wrong accusation is worse than missing an AI text because it costs more falsely accusing a person's hard work. I let one to be labelled as AI because there can be a case where the text is written with predictable words and structured formally without using AI.


---

## 2. Of the 10 formal human pieces in scenarios.py, at least 9 return formal: true from /submit, in each of 3 trials

**Why this target:**
The formal caution exists to protect careful human writers, who the detector is most likely to wrongly call AI. Every miss means one of those writers sees an AI or unsure label with no explanation and no nudge to appeal. That's why I don't go looser than 9 of 10. I don't demand 10 of 10 because the check is strict by design: it allows at most 1% contractions (FORMAL_MAX_CONTRACTION_RATE = 0.01), and one "!" or ALL-CAPS word marks the whole piece casual. A real formal essay can still have one contraction or one emphatic word, so expecting a perfect score would mean expecting human writers to be perfectly consistent.

---

## 3. Of the 10 casual human pieces in scenarios.py, at most 1 returns formal: true from /submit, in each of 3 trials

**Why this target:**
If casual writing gets flagged as formal, the caution stops meaning anything, and readers learn to ignore it, including the formal writers it's meant for. I allow 1 because the check looks for casual signals (contractions, slang like "gonna" or "lol", "!", stretched letters, ALL-CAPS). A short casual piece can happen to avoid all of them and still read as casual to a person. More than 1 in 10 would mean the rules are missing common casual writing, not a rare edge case.

---

## 4. In 10 out of 10 submissions, the formal flag in logs/audit.jsonl matches what /submit returns, in each of 3 trials

<!-- Your criterion. -->


**Why this target:**
The audit log is the record someone checks when a writer appeals. If the log says formal: false but the writer was shown the formal caution, the reviewer is judging from a different picture than the writer saw, and the writer's appeal is weakened by the system's own records. I don't allow any misses, because nothing random is involved here: /submit writes the same is_formal value to both the log and the response. 


---

## 5. Missing text, empty text, text over 20,000 characters, and text under 50 characters each return an error status (400 or 413, never 500) with a message that names the problem. Tested 3 times each.

<!-- Your criterion. -->



**Why this target:**
A 500 means the server crashed and tells the user nothing. A 400 or 413 with a message naming the problem shows the system caught the bad input on purpose, and tells the user exactly what to fix. 20,000 characters is the service's limit, so oversized text is rejected instead of tying up the model. Text under 50 characters is too short for the model and style signals to judge, so any score it got would be meaningless and could still put a label on a writer.


---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 8 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath, like this:

         ## 2. Uncertain cases land in the unsure band

         The system handles uncertain cases well.

         **Why this target:** ...

         > **Revised in unit 8:** Text I judged borderline scores between
         > 0.4 and 0.6 in at least 4 of 5 cases.
         >
         > **Why revised:** "well" gave me nothing to check. I couldn't
         > reach a verdict from it at all.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "At most 1 of 10 of my own pieces flagged as AI" → "at most 3
            of 10", because 1 of 10 turned out to be hard.

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.
     ───────────────────────────────────────────────────────────────────────── -->
