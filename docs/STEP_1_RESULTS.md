# Step 1 results: Studio preparation and bounded offline checks

Date: 2026-11-16. Baseline: `112e0deb31f0b54e16553f2c356a03a02d26e63c`.

**Historical snapshot:** The status and next action below describe the first startup failure and its correction at the time of this report. Subsequent startup, upgrade and reset evidence is in [UPGRADE_0.13.0.md](UPGRADE_0.13.0.md); the later live CrewLab trial and its **PARTIAL** result are in [CREWLAB_TRIAL_REPORT.md](CREWLAB_TRIAL_REPORT.md). The later trial does not establish that every mandatory check of [NEXT_STEP.md](NEXT_STEP.md) passed.

**Result: first actual VS Code startup failed; the user-approved correction is applied and real doctor now passes (exit 0).** The original failure after `53a6752` was recorded in `96fc543`. The user explicitly chose “Apply the correction”; the fake model path has now been removed. A new actual VS Code task result and all downstream live checks are still pending. Crew was not replaced or benchmarked. No paid Crew/worker sessions, Advisor requests, or model benchmarks were started. This assistant session and its earlier short source-audit agent still consume their own usage; their exact credit cost is not exposed here.

## First actual startup: FAIL

- Expected: **Kiro Crew: Start** passes doctor and starts the gateway with Studio available.
- Actual: doctor reports `custom embedding model unusable` for `.runtime/no-embedding-model.gguf`; both doctor and the VS Code task exit **1**, before the gateway command. A subsequent read-only socket check found no listener on port 5476.
- Cause: the launcher supplies this deliberately missing file through `KIROCREW_EMBED_MODEL_PATH`. The earlier setup used that to prevent a download while allowing keyword search. Making doctor failures fatal in `c05955d` exposed the incompatible configuration. The stub-based startup tests passed but did not validate the real doctor's acceptance of the embedding configuration.
- Source evidence: the installed Crew 0.12.2 `doctor_checks/features.py` treats an invalid custom path as an issue. `embeddings_model.resolve_custom_model()` returns `None` when no custom path is configured, selecting the bundled model. `embeddings_download.ModelDownloadManager` downloads the bundled model in the background at gateway startup, with a pinned hash. The old disable-embeddings endpoint returns HTTP 410; a fake path is not a supported disable setting.
- State at the end of the failure investigation (`96fc543`): no launcher/configuration fix, retry, substitute gateway, new installation, model session, or fixture harness run had been started. The earlier local Studio installation and fixture remained in place. Optional-component warnings and unverified newer Kiro tool names remained separate observations; the output did not establish that every other requirement passed.

### Approved correction — applied and checked

The user approved removing the launcher's two historical embedding comments and this assignment:

```diff
-export KIROCREW_EMBED_MODEL_PATH="${KIROCREW_EMBED_MODEL_PATH:-$root/.runtime/no-embedding-model.gguf}"
```

Doctor failures remain fatal and the same VS Code task is retained. With no explicit custom path inherited from the caller or configured in Crew (neither local config file sets one), Crew uses its default local Qwen3 embedding model, about **610 MB**. Expect a one-time background download into Crew's data home and local CPU/RAM use, with no model-provider credit charge for embedding. No hand-written downloader, package upgrade, or Crew patch was added.

- **Four startup tests pass** (0.075 seconds): default model selection reaches the doctor without an injected path; an explicit custom path is preserved; doctor failure still prevents gateway startup; local Bun, gateway options and the single VS Code task remain covered. The command stubs verify environment forwarding, not the validity of a supplied GGUF.
- `bash -n scripts/start-kirocrew.sh` passes.
- **Real installed Crew doctor: exit 0**, `Kiro Crew is ready!`, using the corrected launcher's data home and local executable paths, with no inherited custom embedding path. It reports `not downloaded yet (downloads in background on gateway start)` and `embeddings: always-on`. Raw diagnostic output is private/ignored under the pilot directory.
- A standalone diagnostic check was run; the gateway was not started. The default-model download, actual VS Code task retry and Studio health remain unverified. No model sessions or repeat of the 89 unchanged upstream tests were needed.

Next: the user reruns the same VS Code task. Inspect its real result and extension health before considering planning sessions. Stop again at the first failure; a passing diagnostic does not establish successful gateway startup or model download.

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

## Live check status

| Required live evidence | Status |
| --- | --- |
| Actual **Kiro Crew: Start** task | First attempt **FAIL**; approved correction and standalone doctor **PASS**; task retry awaiting user action |
| Extension backend/payload health and session Bun reachability | NOT RUN; startup stopped before gateway |
| Fixture registration/harness transaction through Studio | NOT RUN; fixture contains only its baseline source/issue |
| Technical planning and separate specialist review | NOT RUN; no model calls or worker completion IDs exist for this slice |
| Live hook ownership, human gate and denied premature transition | NOT RUN; fixture tests are not a substitute |
| Native parent/child usage, effective settings and scoped context | NOT RUN; no invented values or zero-cost claims |
| Pending gate/artifact persistence through actual task restart | NOT RUN |

The user supplied evidence of the actual task failure and subsequently approved the correction. No shell-started substitute gateway was launched. Resume at the corrected task's actual UI invocation; this launcher configuration error does not justify a candidate switch.

## Next action

Run **VS Code → Tasks: Run Task → Kiro Crew: Start** again. After it starts successfully, check Studio's Settings/About for healthy backend/payload and Bun reachability, then resume section C of [NEXT_STEP](NEXT_STEP.md). Planning/review, approvals, usage/context and restart checks remain unrun. All system-plan acceptance boxes remain incomplete.
