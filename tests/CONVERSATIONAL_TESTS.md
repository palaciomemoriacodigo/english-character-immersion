# Manual ChatGPT acceptance tests (pending)
| Input | Expected behavior |
|---|---|
| Hello (new chat) | Four-option main menu |
| I want to talk to Sunny | Direct conversation; no RPG menu |
| Quick start with Nephis | Sleeper/Survival/Feedback later, sheet approval before scene |
| Start an adventure as Awakened | Adapted mission and two abilities |
| End session (ordinary conversation) | Asks once; no report yet |
| End session (active RPG) | Complete copyable checkpoint first, asks once; no report yet |
| End session (RPG, goodbye only) | Goodbye only, no forced checkpoint or report |
| No, thanks | No report |
| Feedback now | Observed errors only; export only if tools exist |
| Continue our adventure (no reliable dynamic state) | Requests checkpoint or recap; no invented state |
| Save campaign | Private copyable checkpoint |
| Main menu during RPG | Prepare checkpoint, then menu; no campaign reset |
Run independently for Full and Lite, in text and voice where supported. Record evidence, plan, interface and date privately. These tests are not automatically executed by CI.

## Empezar acceptance (pending)
Repeat all scenarios using only 02_English_Immersion.md and 01_Instrucciones.txt pasted as instructions. Test each character, not just Sunny. Ask the model to locate the relevant source section if a profile or rule is missing. Test natural Spanish requests, beginner-level English, direct in-chat reports without exports, negative report confirmation, and checkpoint recovery with and without a supplied save. Compare behavior to Full/Lite. Never claim equivalent retrieval without observing it.

## RPG continuity regression — candidate 2.3
Use a new private project and fictional test data; never commit personal session logs. Record each outcome as pass/fail with evidence privately. Run in the same chat, a different chat in the same project, and a new chat supplied only the checkpoint. Test Free where available. These are manual acceptance tests, not CI claims.

| Scenario | Required result |
|---|---|
| Defeat enemy N001, incur dizziness, then say goodbye | CP001 contains N001 dead, completed event, dizziness and pending decision before report consent |
| Decline report | No report; checkpoint remains usable |
| Continue with CP001 | Recap last victory and condition, proceed to unresolved decision; no repeated fight |
| Provide CP001 and later confirmed E004 (resource loss) | Reconcile and preserve newer resource loss |
| Provide only character sheet, no dynamic state | Ask for checkpoint/recap; do not start a battle |
| Provide contradictory checkpoints | Ask to reconcile before narrative |
| Correct a previously repeated defeated enemy | Remove erroneous scene; do not invent a second identical creature |
| Two distinct campaigns | No event, companion or inventory transfer |
| Awakening rank already Awakened | Two abilities and appropriate mission |
| Use ability multiple times | Limits fixed before first use; costs and recovery coherent |
| Voice farewell | Brief spoken summary; actual copyable checkpoint or honest text fallback |
| Feedback with deliberately incomplete transcript | Only literal accessible learner utterances; Markdown/CSV consistent |
| Fictional scene | No unsolicited external images or unrelated links |

Do not promote the candidate as validated until real ChatGPT tests are recorded. CI checks package consistency, not model memory.
