# Manual ChatGPT acceptance tests (pending)
| Input | Expected behavior |
|---|---|
| Hello (new chat) | Four-option main menu |
| I want to talk to Sunny | Direct conversation; no RPG menu |
| Quick start with Nephis | Sleeper/Survival/Feedback later, sheet approval before scene |
| Start an adventure as Awakened | Adapted mission and two abilities |
| End session | Asks once; no report yet |
| No, thanks | No report |
| Feedback now | Observed errors only; export only if tools exist |
| Continue our adventure (no save) | Requests checkpoint; no invented state |
| Save campaign | Private copyable checkpoint |
| Main menu during RPG | No campaign reset |
Run independently for Full and Lite, in text and voice where supported. Record evidence, plan, interface and date privately. These tests are not automatically executed by CI.

## Empezar acceptance (pending)
Repeat all scenarios using only 02_English_Immersion.md and 01_Instrucciones.txt pasted as instructions. Test each character, not just Sunny. Ask the model to locate the relevant source section if a profile or rule is missing. Test natural Spanish requests, beginner-level English, direct in-chat reports without exports, negative report confirmation, and checkpoint recovery with and without a supplied save. Compare behavior to Full/Lite. Never claim equivalent retrieval without observing it.
