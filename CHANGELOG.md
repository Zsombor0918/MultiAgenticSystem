# Changelog

## 2026-11-21 — Conversation reset (partial)

- Used Crew's native dashboard API to close 15 open slots and clear 17 closed sessions; the sessions API returned zero. Studio's live health reported healthy with the bundled payload and Bun available.
- Complete workflow reset remains outstanding: Studio does not offer intent deletion, two prior action records remain, old artifact deletion was rejected by automatic command review, and task restart verification is pending.

## 2026-11-21 — Native skill sync

- Ran Crew's native builtin skill synchronization; no user skill was set aside. Doctor now passes with all 43 builtins current, and the normal VS Code task starts the gateway with the V3 relay.
- Recorded remaining owner actions, the failed intent reset, unverified Studio health and cleanup command rejection in `docs/UPGRADE_0.13.0.md`.

## 2026-11-21 — Crew 0.13.0 upgrade and blocker

- Installed stable 0.13.0 with the official signed installer, preserving local state and retaining Kiro CLI V3 relay. Recorded backup and compatibility evidence in `docs/UPGRADE_0.13.0.md`.
- Confirmed native per-project hook consent is present and currently off for the inspected projects. Live consent and hook execution remain untested.
- Doctor reports stale builtin skills and exits 1; the launcher remains fail-closed and the trial is paused pending a safe synchronization plan.

## 2026-11-16 — Approved embedding configuration correction

- Removed the launcher's fake `KIROCREW_EMBED_MODEL_PATH` after user approval. Crew can now use its default local embedding model (about 610 MB), downloaded in the background on gateway startup. Explicit custom paths remain available. This resolves the reported configuration error while preserving fatal doctor checks and the same VS Code start task.
- Strengthened the startup tests to check the model-path environment reaching doctor. All four tests and shell syntax pass. The real installed Crew doctor also exits **0**, reporting that Crew is ready and the model download is pending.
- Updated the results and next-step instructions. The actual task retry, download and Studio health are still pending; no gateway or paid model sessions were started for this correction.

## 2026-11-16 — Actual startup failure recorded

- Recorded the user's real VS Code task failure: the missing embedding-model placeholder makes Crew doctor and the launcher exit 1 before the gateway starts. The earlier stub tests did not cover the real doctor's model configuration check.
- Updated status and resume instructions to stop dependent work and propose removing the fake custom-model path in favor of Crew's default local model. At that point the correction awaited user agreement under the trial's stop-on-failure rule.

## 2026-11-16 — AI-DLC Studio pilot preparation

### Added

- Documented the pinned AI-DLC Studio 2.0.1 and bundled AI-DLC 2.11.3 choices, provenance, licenses, local setup, capability limits, and remaining live checks in `docs/COMPONENT_DECISIONS.md`, `docs/CAPABILITIES.md`, and `docs/STEP_1_RESULTS.md`. This keeps the integration reproducible and makes the evidence and unknowns visible.
- Added three startup regression tests covering the single VS Code task, the existing gateway options and local Bun path, and stopping startup when Crew's doctor command fails. These protect the one-start-button workflow and prevent continuing after a failed prerequisite.

### Changed

- Updated `scripts/start-kirocrew.sh` to put the pilot's pinned, local Bun on the existing startup path so Studio hooks can use it without adding a second start command or changing the user's shell profile.
- Made a nonzero `kirocrew doctor` result stop startup. A failed prerequisite should be visible before the gateway and extension are used.
- Updated the README and execution notes to reflect the completed offline preparation and keep the next step at the actual VS Code task and live approval trial.

### Verified

- Verified all 373 pinned Studio payload files and the publisher's Bun archive digest; reused the release's committed UI bundle instead of rebuilding it.
- Ran 89 selected upstream Studio tests and three repository startup tests successfully; `bash -n` also passed.
- Installed and enabled Studio locally through Kiro Crew's native app CLI, with trust scoped to this app. This generated a namespaced Advisor definition but did not invoke it or start a model session.

### Still pending

- The Studio checkout, Bun binary, test overlay, fixture, and local app installation are kept in ignored `.runtime/` paths; they are not vendored into this repository.
- The actual **Kiro Crew: Start** VS Code task, live Studio/Bun health, planning and independent review, human approval gate, usage/context evidence, and restart persistence have not yet been verified. No paid Crew worker or model calls were made in this preparation step.
