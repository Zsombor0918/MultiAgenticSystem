# Changelog

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
