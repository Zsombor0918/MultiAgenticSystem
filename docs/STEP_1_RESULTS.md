# Step 1 results: Studio preparation and bounded offline checks

Date: 2026-11-16. Baseline: `112e0deb31f0b54e16553f2c356a03a02d26e63c`.

**Result: preparation passed; live trial incomplete, awaiting the VS Code task.** No mandatory check failed. Crew was not replaced or benchmarked. No paid Crew/worker sessions, Advisor requests, or model benchmarks were started. This assistant session and its one short source-audit agent still consume their own usage; their exact credit cost is not exposed here.

## Completed

- Cloned Studio **2.0.1**, exact commit `8b3881d4737399c3394d8d187f102a5c95d6e528`, into the ignored pilot directory. Kept its patched AI-DLC **2.11.3**, notices and provenance intact.
- Verified **373 payload files** against recorded sizes/SHA-256 hashes. Reused the committed UI bundle; source and installed copy SHA-256: `29916236b068d49641e7923d637aec709ce8c0748612d6551df39f8d42bbb705`. Node syntax check passed; no UI rebuild was needed.
- Installed **Bun 1.4.4** only under the pilot directory. The Linux x64 archive matched the publisher's SHA-256 `bf8ccbfb2b0b80159e0f9a6d15c55317add8077534dbc6130a3edb52fccb395c`; the extracted binary reports 1.4.4.
- Ran **89 selected upstream tests: PASS**, in 24.81 seconds against the installed Crew environment, with test dependencies isolated in the pilot directory. No skipped tests in this selected run.
- Installed Studio through Crew's native app CLI and recorded it enabled. Native registration created one namespaced Advisor file at `~/.kiro/agents/aidlc-studio--aidlc-studio-advisor.json`; no existing global agent was replaced and the Advisor was not invoked. Only this app received local trust; blanket third-party trust remains off. Backups are private/ignored. No gateway was listening during installation/enablement, so the backend hooks have not started.
- Added local Bun to the existing launcher's PATH; changed the doctor command to stop startup on nonzero exit using the script's existing `set -e`.
- Ran **three repository startup tests: PASS**, plus `bash -n`. They exercise the real launcher against temporary command stubs, including a doctor exit of 23 that never reaches gateway startup.
- Prepared an isolated parser fixture and issue, without implementing the requested validation. Its local baseline commit is `e3d4b22675f70de4fac913ec437702e81f2b0183`; `main.py` SHA-256 is `e75e6ec9c7420b964b4fa864a6077f68c0eee5ea9b984ae8a80109ba6605d063`.

## What the upstream checks actually covered

Selected files: `test_manifest.py`, `test_loader.py`, `test_installer_rollback.py`, `test_delivery_at_most_once.py`, `test_payload_kiro_steer_origin.py` from the pinned Studio source.

They cover host manifest/loader compatibility, import/start/stop lifecycle behavior, rollback and user-file preservation, duplicate-delivery protection, and bundled Bun hook classification of host notices versus human turns. Loader tests use isolated homes and a test-only trust stub; delivery tests use a fake host. Bun hook tests execute the actual bundled engine on fixture data. These passes do **not** prove a live browser approval or model-generated plan/review.

The run emitted 15 warnings: Python's fork-with-threads deprecation and aiohttp test-key recommendations. No test failed or hung. No upstream source or installed Crew package was patched.

Reproduce the selected checks after the pinned source/Bun/test overlay are present:

```bash
cd .runtime/pilots/aidlc-studio-2.0.1/source
export PATH="$PWD/../bun/bin:$PATH"
export PYTHONPATH="$PWD/../test-deps"
../../../kirocrew-venv/bin/python -m pytest -q -x -o addopts= \
  tests/test_manifest.py tests/test_loader.py tests/test_installer_rollback.py \
  tests/test_delivery_at_most_once.py tests/test_payload_kiro_steer_origin.py
```

Repository checks: `python3 -m unittest discover -s tests -v` and `bash -n scripts/start-kirocrew.sh`.

## Still NOT RUN

| Required live evidence | Status |
| --- | --- |
| Actual **Kiro Crew: Start** task and extension backend/Bun health | Awaiting the user's UI action; executor cannot click VS Code |
| Fixture registration/harness transaction through Studio | NOT RUN; fixture contains only its baseline source/issue |
| Technical planning and separate specialist review | NOT RUN; no model calls or worker completion IDs exist for this slice |
| Live hook ownership, human gate and denied premature transition | NOT RUN; fixture tests are not a substitute |
| Native parent/child usage, effective settings and scoped context | NOT RUN; no invented values or zero-cost claims |
| Pending gate/artifact persistence through actual task restart | NOT RUN |

The user was asked asynchronously to start the existing task, without sending a model conversation. No shell-started substitute gateway was launched. Continue the live portion only once that action is evidenced. Stop at the first mandatory failure; do not switch candidates or work around it in the same run.

## Next action

Start **VS Code → Tasks: Run Task → Kiro Crew: Start**. Check Studio's Settings/About for healthy backend/payload and Bun reachability. Then continue section C of [NEXT_STEP](NEXT_STEP.md) using `.runtime/pilots/aidlc-studio-2.0.1/fixture/ISSUE.md`, stopping at technical-plan approval. Bound the first planner/reviewer sessions before launching them; do not start a broad benchmark or Advisor run. All system-plan acceptance boxes remain incomplete.
