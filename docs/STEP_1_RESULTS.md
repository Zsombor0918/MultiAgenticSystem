# Step 1 results: Studio preparation and bounded offline checks

Date: 2026-11-16. Baseline: `112e0deb31f0b54e16553f2c356a03a02d26e63c`.

**Result: offline preparation passed; the first actual VS Code task failed before gateway startup.** The user supplied the task output after commit `53a6752`: doctor and the launcher exited 1 because the launcher names a nonexistent custom embedding model. Dependent live checks have stopped under the agreed failure rule. Crew was not replaced or benchmarked. No paid Crew/worker sessions, Advisor requests, or model benchmarks were started. This assistant session and its earlier short source-audit agent still consume their own usage; their exact credit cost is not exposed here.

## First actual startup: FAIL

- Expected: **Kiro Crew: Start** passes doctor and starts the gateway with Studio available.
- Actual: doctor reports `custom embedding model unusable` for `.runtime/no-embedding-model.gguf`; both doctor and the VS Code task exit **1**, before the gateway command. A subsequent read-only socket check found no listener on port 5476.
- Cause: the launcher supplies this deliberately missing file through `KIROCREW_EMBED_MODEL_PATH`. The earlier setup used that to prevent a download while allowing keyword search. Making doctor failures fatal in `c05955d` exposed the incompatible configuration. The stub-based startup tests passed but did not validate the real doctor's acceptance of the embedding configuration.
- Source evidence: the installed Crew 0.12.2 `doctor_checks/features.py` treats an invalid custom path as an issue. `embeddings_model.resolve_custom_model()` returns `None` when no custom path is configured, selecting the bundled model. `embeddings_download.ModelDownloadManager` downloads the bundled model in the background at gateway startup, with a pinned hash. The old disable-embeddings endpoint returns HTTP 410; a fake path is not a supported disable setting.
- State: no launcher/configuration fix has been applied in this failure investigation; no retry, substitute gateway, new installation, model session, or fixture harness run was started. The earlier local Studio installation and fixture remain in place. Optional-component warnings and unverified newer Kiro tool names remain separate observations; this output does not establish that every other requirement passes.

### Proposed next experiment — awaiting user agreement

Remove only the launcher's two historical embedding comments and this assignment:

```diff
-export KIROCREW_EMBED_MODEL_PATH="${KIROCREW_EMBED_MODEL_PATH:-$root/.runtime/no-embedding-model.gguf}"
```

Keep doctor failures fatal and retain the same VS Code task. With no explicit custom path inherited from the caller or configured in Crew (neither local config file currently sets one), Crew uses its default local Qwen3 embedding model, about **610 MB**. Expect a one-time background download into Crew's data home and local CPU/RAM use, with no model-provider credit charge for embedding. No hand-written downloader, package upgrade, or Crew patch is needed.

After agreement: apply that small change, add a focused regression check for the model configuration presented by the launcher, and verify shell syntax. The user then reruns the same VS Code task. Inspect its real doctor result and live extension health before considering any planning sessions. Stop again at the first failure; do not assume the default-model download or later integration will succeed.

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
| Actual **Kiro Crew: Start** task | **FAIL**: doctor/launcher exit 1; see the failure record above |
| Extension backend/payload health and session Bun reachability | NOT RUN; startup stopped before gateway |
| Fixture registration/harness transaction through Studio | NOT RUN; fixture contains only its baseline source/issue |
| Technical planning and separate specialist review | NOT RUN; no model calls or worker completion IDs exist for this slice |
| Live hook ownership, human gate and denied premature transition | NOT RUN; fixture tests are not a substitute |
| Native parent/child usage, effective settings and scoped context | NOT RUN; no invented values or zero-cost claims |
| Pending gate/artifact persistence through actual task restart | NOT RUN |

The user supplied evidence of the actual task invocation and failure. No shell-started substitute gateway was launched. The live portion is stopped pending agreement on the correction above; no candidate switch is justified by this launcher configuration error.

## Next action

Agree the proposed startup correction before another attempt. After the corrected task starts successfully, check Studio's Settings/About for healthy backend/payload and Bun reachability, then resume section C of [NEXT_STEP](NEXT_STEP.md). Planning/review, approvals, usage/context and restart checks remain unrun. All system-plan acceptance boxes remain incomplete.
