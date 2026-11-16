# Next run: verify the Crew foundation and shared skill loading

Prepared: 2026-11-16. Status: **plan ready; implementation and runtime trial not executed**.

This is the first bounded part of step 1 in the [system plan](../WORK_PLAN.md). The user will run the execution prompt below. Its purpose is to establish the tool capability record and prove that this repository can supply shared skills through the existing VS Code startup task. It does not attempt the whole development lifecycle at once.

## Why this comes first

The final coordinator must know what Kiro/Codex can do, and it must be able to find and load shared skills when working on different projects. Crew already documents a native shared-library mechanism. Proving that mechanism is less work than building an installer, plugin framework, or second orchestrator. Actual model/effort routing, context inheritance, and credit visibility will then be connected on top of an observed foundation.

The first recommended experiment is a repository-owned `skills/` directory registered with Crew's **`skills.extra_paths`**. This is a proposed integration choice, not a proven local success. Do not assume `<active-project>/.kiro/skills/` follows the coordinator into another selected project.

## Facts checked while preparing this plan

Only version queries, file/source reads, and public-source lookups were performed. No gateway, model session, worker, installation, account-usage query, or runtime configuration change was executed for this document.

| Fact | Evidence and limits |
| --- | --- |
| Crew distribution is `kirocrew 0.12.2` | Read installed Python distribution metadata under the local `.runtime/kirocrew-venv`; this confirms installation, not session behavior |
| Kiro CLI is `2.37.0`; Codex CLI is `0.166.0` | Executed the respective `--version` commands; login/session validity was not tested |
| Codex ACP adapter is `1.11.0` | Read its installed package metadata; no authenticated adapter session was started |
| Local Node is `24.22.3`; Python is `3.12.3`; Git is `2.43.0` | Queried executable versions; the launcher prepends its local Node/venv/adapter paths |
| The VS Code task calls `scripts/start-kirocrew.sh` | Read `.vscode/tasks.json`; it uses the workspace root as its working directory |
| The local setup marker exists | Checked `.runtime/kirocrew/.demo-setup-confirmed`; its existence is not proof that current configuration or login is valid |
| Shared skill paths are a native documented feature | Installed docs and the [v0.12.2 skills guide](https://github.com/kirodotdev/KiroCrew/blob/v0.12.2/src/kiro_crew/docs/skills.md) list `skills.extra_paths`; invalid/nonexistent paths can be skipped and global duplicate names take precedence |
| Per-project skills require exact-project trust | Same skills guide; this does not establish shared-library availability across target projects |
| Spawn exposes model, effort, backend, context switches, and absolute working directory | [v0.12.2 subagents guide](https://github.com/kirodotdev/KiroCrew/blob/v0.12.2/src/kiro_crew/docs/subagents.md); support in the API does not prove a setting was applied by a particular backend |
| Arbitrary role-model keys are not supported | Installed and [v0.12.2 role settings source](https://github.com/kirodotdev/KiroCrew/blob/v0.12.2/src/kiro_crew/config/sections_agent_fields.py) define `background` and `subagent`; do not invent `planner` or `reviewer` configuration keys |
| Launcher currently continues after a nonzero doctor result | Its `kirocrew doctor || printf ...` line warns and then reaches gateway startup. This trial needs a small change to stop before startup if doctor fails; the reason for a failure must be reviewed rather than suppressed |

Earlier usage and capability observations remain in [cost notes](history/RESEARCH_COST_NOTES.md) and [delegation results](history/RESULTS.md). They are historical evidence, not fresh PASS results.

## Focused upstream recheck

These files were reread from their primary repositories for this plan. The identifiers below are **Git file-blob IDs**, not adopted dependency pins or tested Crew integrations.

| Source | Observed fact | Consequence |
| --- | --- | --- |
| [agent-pipeline procedure](https://github.com/roycehoe/agent-pipeline/blob/main/skills/feat-pipeline/SKILL.md), blob `30a9fd2370cd1aa32f08cc53271a46f08176a819` | Uses host-specific agent/skill tools and linked stages; describes explicit model selection, compact context packs, and independent audits | Useful donor for our two-stage planning and context procedures; not a drop-in Crew runtime |
| [ADW model router](https://github.com/pdoronila/adw/blob/main/src/adw/model_router.py), blob `ebefb662e1a5ac417237802e76223d97be62d03c` | Explicitly within-backend; usage probes map Claude/Codex, not Kiro; probe failures retain the configured target | Candidate for adapted usage/failure policy, not evidence of Crew-wide routing or a hard cap |
| [Workgraph README](https://github.com/shiro-el/workgraph-skills/blob/main/README.md), blob `a5afa48d55dce6a8d5db0f011a3e19b940ec7d7b` | Current system uses Linear, pinned submodules, host CLIs, and automatic intermediate merges | Consider focused procedures or another candidate; do not install the whole package as our foundation |

No donor has been selected for installation by this document. Exact upstream commit, license, retained notices, dependencies, and necessary adaptation must be recorded before an import. A better alternative or focused local implementation remains acceptable after explaining the choice.

## Uncertainties and expected handling

| Uncertainty | How to investigate | If the required result fails |
| --- | --- | --- |
| Will the active Crew configuration accept our repository's extra skill path? | Inspect supported configuration and path checks; preserve existing entries and verify the exact effective path | Stop; report the rejected/skipped path and source evidence. Do not silently copy into a global home directory |
| Can the dashboard actually discover and read that exact skill? | Observe a `skill_search` result and exact-key read in the real Crew session | Stop; a matching response or a file on disk alone is not PASS |
| Does shared discovery survive project switching and restart? | Use a second harmless local project selection and restart via the same VS Code task | Stop; report which scope/start lost the skill |
| Are login, adapter, and doctor checks healthy now? | Diagnose using the same environment as the launcher, with secret output redacted | Stop on failure; do not reinstall, upgrade, switch backend, or bypass checks automatically |
| Are model IDs, effort, permissions, context, and telemetry currently verified? | Populate a capability record using current source plus attributed historical evidence | Mark untested fields UNKNOWN. Runtime verification is later work; do not fabricate it or treat unknown as supported |

UNKNOWN is allowed for catalogue fields outside this trial. It is not allowed to turn a failed mandatory startup/discovery check into success. A version differing from this snapshot is not automatically broken: revalidate version-specific assumptions first, and stop if the selected mechanism can no longer be established.

## Execution sequence and scope

### A. Record the foundation before changing runtime behavior

Read the current instructions, system plan, alignment, and relevant historical evidence. Check Git status and preserve unrelated changes. Recheck versions and only the necessary source/configuration fields. Do not dump credential-bearing configuration or transcripts.

Create `docs/CAPABILITIES.md` with Kiro/Codex model/effort/tool/context/permission/usage fields, status, date, source, and limits. Clearly separate documented support, old observations, new observations, and unknowns. Create `docs/COMPONENT_DECISIONS.md` for the native extra-path choice and initial donor decisions/dependencies; leave unselected donors as candidates.

### B. Prepare one small, reversible loading trial

Add `skills/crew-foundation-check/SKILL.md`, a tiny diagnostic that only reports its identity, reads the capability document when available, and identifies unknowns. It must not spawn workers, change code, call external services, or claim full workflow readiness. This diagnostic verifies library plumbing; it is not a replacement for the researched production skills.

Configure the repository's absolute `skills/` directory through the installed supported `skills.extra_paths` mechanism in this project's `.runtime/kirocrew` configuration. Back up the touched local configuration, preserve unrelated entries, and make registration idempotent. Use the existing launcher for any repeatable startup preparation; do not require another normal startup command or a full reinstall. Avoid overwriting a global skill of the same name. Keep local paths/state out of tracked user-specific configuration.

Make the minimal launcher change that stops gateway launch when doctor returns nonzero. Inspect diagnostic behavior before invoking commands that can change configuration. Do not bypass a failure because it might concern an optional backend: report it so the next plan can classify it properly.

Run local syntax/configuration checks before the live trial. Do not patch installed Crew/adapter packages, change sandbox/approval defaults, edit unrelated home configuration, or install donor runtimes in this step. If the native mechanism requires one of those changes, stop with the concrete evidence and proposed alternative.

### C. User-run startup and discovery trial

The user starts Crew with **VS Code → Tasks: Run Task → Kiro Crew: Start**. If the agent cannot operate that UI, give the user the exact action and wait for the evidence; do not substitute a shell-started gateway or claim to have clicked the task.

The user can submit this bounded request in the Crew dashboard:

```text
This is a shared-skill loading check. Use skill_search to find
crew-foundation-check, then read its exact returned key and follow its
read-only diagnostic procedure. Report the skill's identity, what capability
information was available, and what remains unknown. Do not spawn workers,
modify files, or execute an implementation task. If lookup or reading fails,
report the exact failure and stop; do not repeat my request as if it succeeded.
```

Use an available account model without claiming it is already an optimized choice. These parent-session checks can consume usage; do not start a benchmark or workers. Record session identifiers and visible tool evidence, with any reported usage and coverage. Confirm the active project path, then repeat the discovery check after selecting a second harmless local project, and after stopping/restarting through the same VS Code task. Do not use KovacsTrader or modify another real project for this plumbing check. Do not create Git worktrees.

### D. Record results, then end the run

Write `docs/STEP_1_RESULTS.md` with the baseline commit, versions, exact changes, mandatory-check outcomes, evidence, remaining unknowns, and next recommendation. Keep secrets and raw sessions out of Git. Mark only this bounded part of step 1 complete when all mandatory checks pass; the full step remains incomplete if component selection or other deliverables remain. Commit the checked changes locally on success. Report the commit, but do not automatically start step 2 or push this future execution unless the user requests it.

## Mandatory success checks

- Startup uses the existing VS Code task; no extra startup commands are needed.
- A failing doctor result prevents gateway startup in the updated launcher.
- The effective extra skill path points to the repository's real directory and survives a second start without duplicate registration.
- The actual Crew session discovers and reads the exact diagnostic skill from the shared library.
- Discovery/read still works after project selection changes and restart.
- Capability/decision/result records clearly distinguish tested facts from unknowns; no unverified model/effort/monitoring claim is promoted to PASS.

## Stop and rethink rule

**On the first mandatory failure or missing evidence: stop dependent work.** This rule is stricter than the general permission to try alternatives and applies to this execution run. Do not auto-retry, silently switch approach/provider, weaken permissions, reinstall, hide errors, or implement a workaround in the same run. Independent collection of the failing check's evidence and writing the result report are allowed.

Report: failing check, expected result, actual result/exit code, relevant redacted evidence, files/state changed, anything still running, and which later checks were not run. Label hypotheses as hypotheses. Preserve work for inspection; do not hard-reset or discard unrelated changes. Offer the simplest next experiment or replacement approach and end the run. The user and agent then revise this plan before retrying the failed path. If a required user action has not happened, mark NOT RUN / waiting for user evidence, not FAIL or PASS.

## Copyable prompt for the next Codex session

```text
Work in /home/zsom/MultiAgenticSystem. Execute only the bounded foundation
and shared-skill-loading plan in docs/NEXT_STEP.md, sections A through D.
Read AGENTS.md, README.md, WORK_PLAN.md, and docs/RESEARCH_ALIGNMENT.md first.

Keep our complete goal intact: ChatGPT/GitHub issue → Crew technical plan
and review → detailed implementation plan and approval → smart multi-tool
implementation → tests/independent review/PR. Agent/skill selection,
model/effort routing, context handling, and credit-aware decisions are core.
This run establishes their foundation; it does not build the whole system.

Recheck the documented facts, record unknowns, use supported native Crew
mechanisms, and keep changes minimal and reversible. Develop directly in
this repository with ordinary Git; no worktrees. Preserve AGPL licensing.
All normal startup must use the existing VS Code task Kiro Crew: Start.

Prepare the capability and component-decision records, the one harmless
shared diagnostic skill, and the smallest necessary startup integration.
Use the user-run VS Code/dashboard actions in the plan for live evidence.
Do not launch a substitute gateway, paid worker tests, installations, or
backend upgrades. If user action is needed, identify it and wait for the
result instead of pretending it happened.

At the first failed mandatory check, stop dependent work, document the
expected/actual behavior and changed state in docs/STEP_1_RESULTS.md,
explain the best next experiment, and end the run. Do not automatically
retry or work around it. If all checks pass, document and commit this
bounded result locally, report the remaining unknowns, and stop before
step 2. Do not mark the full system or full step 1 finished prematurely.
```
