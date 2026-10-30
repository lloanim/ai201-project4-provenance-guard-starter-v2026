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
## 1. Of 10 pieces I wrote myself, at most 1 is labelled high-confidence AI, in each of 3 trials

<!-- Your criterion. It must name a number. -->



**Why this target:**
I chose 10 so there is more chance to see how reliable the system is in scoring the human text as not AI. A wrong accusation is worse than missing an AI text because it costs more falsly accussing a person's hard work. I let one to be labelled as AI because there can be a case where the text is written with predictable words and structured formally without using AI.


---

## 2. Across 5 clearly-AI and 5 clearly-human texts, the average combined score of the AI texts is at least 0.30 higher than the average for the human texts, in each of 3 trials. 

<!-- Your criterion. -->



**Why this target:**
If the averages are less than 0.30 apart, AI and human text could both land inside the "unsure" band, and the system would not be able tell them apart. I expect the distance to above the minimum which would mean that the system is working reliably. The average combined score is the calculated score from what the text recieves from the model signal (perplexity) and style (shape of the text). The 0.30 is the width of the "unsure" band (0.65 - 0.35). Where a text is AI if its 0.65 or higher and human if its 0.35 or lower. 


---

## 3. Using the inputs in scenarios.py each of the three labels (high-confidence human, unsure, and high-confidence AI) is returned at least once, in each of 3 trials

<!-- Your criterion. -->



**Why this target:**
The system should be able to reach all three labels weather its "high-confidence human", "unsure", or "high-confidence AI". Especially "unsure" where it should label texts that falls between that threshold (0.35 - 0.65) and say that it was not able to determine if its AI or not. Its better that the system gives this as an answer than immediately claim that the work is AI especially if its actually human writen. 


---

## 4. For 5 out of 5 appeals on real content_ids, the status changes from decided to under_review and the appeal shows up in the audit log for that content_id. An appeal with a content_id that does not exist returns an error naming the problem, never a 500, in 3 out of 3 tries

<!-- Your criterion. -->



**Why this target:**
An appeal is the only way a falsely accused writer can push back, so it should work 100% of the time. The status should change so the user can see their content is under review, and the appeal should be recordded in the audit log so there is a history of what happend. With a content_id that does not exist, the system should not crash but return a clear error, so the user knows the ID may be wrong. 


---

## 5. Missing text, empty text, and text over 20,000 characters each return an error status (400 or 413, never 500) with a message that names the problem. Tested 3 times each.

<!-- Your criterion. -->



**Why this target:**
A 500 means the server crashed and tells the user nothing. A 400 or 413 with a message naming the problem shows the system caught the bad input on purpose, and tells the user exactly what to fix. 20,000 characters is the service's limit, so oversized text is rejected instead of trying up the model. 


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
