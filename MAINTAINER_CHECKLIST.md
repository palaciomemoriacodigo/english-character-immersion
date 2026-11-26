# Release checklist

## Privacy and rights
- [ ] Verify ownership of original material covered by MIT and CC BY-NC 4.0; complete [third-party rights review](docs/RIGHTS_REVIEW.md). Restrict distribution if clearance is unavailable.
- [ ] Inspect Git history, old references and artifacts; ensure public Git identity uses noreply. Do not store real conversations or progress in tracked templates.
- [ ] Run `python scripts/privacy_check.py` before committing and `python scripts/privacy_check.py --generated` after building. Review findings manually; the check is not comprehensive.
- [ ] Review the six illustrations for accidental personal information and UI changes.

## Tests
- [ ] Run validation, unit tests, default and advanced builds and Chromium checks; verify both languages, mobile layout, copy fallback, exact downloads and legal links.
- [ ] Complete a real installation in a new private ChatGPT project and observe a nontechnical tester; verify character retrieval, RPG creation/recovery, corrections and reports in supported text/voice modes.
- [ ] Review Safari/Firefox and real mobile behavior where available.

## Release
- [ ] Confirm scope and version; update VERSION, CHANGELOG and site/release_announcement.json for the planned 13 December 2026 update. Run sync_start and commit generated files.
- [ ] Keep PUBLIC_RELEASE_APPROVED disabled until rights/privacy approval. Deploy using the manual Pages workflow with PUBLISH only after approval. Verify the live URL and downloads.
- [ ] Create a matching v<VERSION> tag only for an approved package release; candidate tags are prereleases. Keep optional advanced packages tested.
