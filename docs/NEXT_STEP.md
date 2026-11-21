# Next run: integrate the existing AI-DLC Studio Crew extension

**2026-11-21 update:** The local reset removed the failed CrewLab intents, Studio actions and saved Crew chats. CrewLab remains registered with its installed harness. The original parser fixture was removed. Confirm gateway and Studio health after startup and verify CrewLab hook consent before beginning a fresh trial with `.runtime/CrewLab/tasks/01-fix-oversell.md`. See [upgrade and reset results](UPGRADE_0.13.0.md) and [earlier offline checks](STEP_1_RESULTS.md).

**Kiro Crew is fixed and trusted.** This run checks a ready-made extension against our workflow; it does not reconsider or benchmark Crew. Read the [current extension research](research/CREW_EXTENSIONS_2026-11-16.md), [extension source inventory](research/CREW_EXTENSION_SOURCES_2026-11-16.json), and [system plan](../WORK_PLAN.md). This supersedes the earlier diagnostic-skill and BMAD-first experiments.

Reuse order: native Crew → existing Crew extension → portable/adapted component → implement only the remaining gap. The proposed first extension is **AI-DLC Studio 2.0.1**, commit `8b3881d4737399c3394d8d187f102a5c95d6e528`. It bundles **AI-DLC 2.11.3 plus four documented patches**; it is not upstream 2.11.4. The official store currently lists older Studio 1.0.1, so do not accidentally test that while reporting 2.0.1.

## The bounded outcome

**Resume point:** verify Studio health and CrewLab's hook consent, then use the registered CrewLab project for section C. Keep the existing source and payload pins.

Use the actual extension to produce a code-grounded technical plan and separate specialist review for a tiny fixture issue. Verify a real human approval checkpoint, then stop **awaiting the user's technical-plan approval**. Record precisely what remains to connect Crew's backend/model/effort choices, context and usage to the extension.

The detailed implementation plan, second approval, code changes, CI, independent code review, delivery and portability remain required later steps. No mock plan, mere installation, or discovery response counts as a successful planning/review integration.

## Facts and unknowns

- Installed Crew 0.13.0 meets Studio 2.0.1's declared minimum 0.11.0. Check only changed or extension-specific prerequisites.
- Studio is Apache-2.0; bundled AI-DLC is MIT-0. Its manifest records the upstream base, payload hashes and compatibility patches. Retain these notices and receipts.
- Studio requires Bun reachable by the gateway and AI-DLC sessions; its guide recommends 1.4.4 or newer. Bun was not on the research shell's PATH; configured paths were not exhaustively checked. Node/npm may be needed for a one-time UI build; inspect the pinned package/installer before choosing commands or assuming prebuilt files exist.
- It already has gateway startup/shutdown hooks, a Crew session bridge, approval evidence and transactional per-project installation. Reuse these; do not write an alternative app loader, approval UI or lifecycle engine.
- Crew already has backend capability cards, live model/effort data, optional model derivation, usage sources and spec-hook handling. Use those. The missing native ACP hook advertisement alone does not prove incompatibility or require changing Crew.
- Studio's model/effort pickers do not establish dynamic worker routing. Its AI-DLC usage module lacks a Kiro/Codex producer. Current extension phase/child attribution and cross-backend worker mapping remain unknown.
- Older upstream Docker installation checks explicitly excluded model calls; they do not prove this combined version works locally.

## A. Record the exact extension decision

Read AGENTS, README, WORK_PLAN, RESEARCH_ALIGNMENT and the extension research. Preserve unrelated changes; use ordinary Git here, no worktrees. Keep credentials, account identifiers, raw sessions and runtime data out of commits.

Create `docs/COMPONENT_DECISIONS.md`: selected app/source/pin, actual payload version/patches, licenses/notices, necessary dependencies/assets, verified installation method and changed paths. Note native Spec Builder plus a minimal portable specialist set as the fallback to consider if this trial fails, without installing it now.

Create a compact `docs/CAPABILITIES.md` referencing Crew's native cards/model/effort/usage surfaces. Add only relevant local account/version observations and unknowns; do not hand-copy its whole capability matrix. Distinguish role/persona, backend, model, effort and skill.

Inspect the pinned installer/manifest and supplied bridge before choosing commands. Do not invent flags, silently use `latest`, replace Studio's payload with a newer upstream release, or apply a second framework's global setup. Missing required source/license/assets is a mandatory blocker.

## B. Prepare the existing app and harmless fixture

Use the pinned checkout in `.runtime/pilots/aidlc-studio-2.0.1/` and the registered `.runtime/CrewLab/` project with its existing harness. Record the starting revision and keep generated outputs ignored.

Use the installed Crew app contract and exact selected version. Verify the UI is available, Studio reports healthy, and Bun is reachable from the actual extension sessions. Check CrewLab's existing harness receipt, `.kiro` paths and permissions. The user handles native project hook consent in Crew. Keep it limited to CrewLab and verify it before the trial.

Keep normal startup behind **VS Code → Tasks: Run Task → Kiro Crew: Start**. Integrate only necessary repeatable environment/configuration preparation into its existing launcher. One-time installation/authentication is setup, not another normal start command. Do not start a second gateway or separate daemon. If the executor cannot operate the VS Code UI, identify that user action and wait for evidence; do not substitute a shell-launched gateway or claim the task was clicked.

## C. Exercise only planning, review and its user gate

1. Use the registered CrewLab project and its `tasks/01-fix-oversell.md` exercise as input for a fresh planning intent. The task provides source and acceptance criteria. This trial ends at planning approval. The final product's intake remains an approved GitHub issue.
2. Select the smallest supported lifecycle scope that retains technical planning, independent specialist review and a human gate. Preview actual stages/artifacts. Do not force all 33 stages onto a tiny issue, skip a required gate, or let a Quick/Express path bypass the two-plan target. Record the future mapping to detailed implementation planning and its separate approval.
3. Verify the extension's actual hook owner, project-agent resolution and human-turn recording on the selected route. Use existing Crew spec-hook handling and Studio's compatibility patches. At a checkpoint, a harmless attempted premature transition must be refused and leave the fixture unchanged. Never fabricate approval, auto-send a human answer, flip handshake flags or bypass the guard. Stop if the required behavior fails.
4. Run its real code-grounded technical planning and obtain a different specialist worker/session's plan review, with scoped context and observed completion. Use one active worker at a time where the supported configuration allows it. If a smaller review configuration needs a patch, document it before the trial; do not quietly replace independent review with planner self-review. A rejected plan ends this run without automatic correction.
5. Record the chosen model/effort and why, what was actually applied/exposed, context/artifact handoffs, parent/child identities and native usage with source/units/freshness/coverage. Native Kiro children may be accepted for this first extension slice if their identity and review independence are evidenced; explicitly record that this does not establish Crew-wide Kiro/Codex dispatch or per-child accounting. Parent-only accounting is partial coverage, not full worker metering. A missing native parent usage record or unidentifiable reviewer is a mandatory blocker; missing price/quota or unavailable per-child fields remain named gaps for step 2.
6. Compare fixture code before/after. Only designated planning/state artifacts may change. Stop **awaiting technical-plan approval**; do not send that approval yourself, generate the detailed implementation plan or start construction. Confirm no host notice or automated continuation was mistaken for the user's approval.
7. Stop/restart using the same VS Code task. Confirm extension/library/artifact availability and the pending checkpoint without rerunning paid planning. This is an extension persistence check; it does not establish whole-system recovery or another-project portability.

This trial does not certify complete hostile-agent write isolation, full smart routing, both planning gates or cross-project support. The production system still requires those relevant acceptance checks. Record a native-review/dispatch/telemetry limitation explicitly rather than calling it solved because the app opened.

## D. Record results, commit the checked slice and stop

Write `docs/STEP_1_RESULTS.md`: baseline commit, pins/dependencies/licenses, exact changed paths, startup/app health, payload checks, fixture issue, actual plan/review identities, hook/approval evidence, settings/context/usage, persistence, failures/unrun checks and remaining adapter work. Keep a concise sanitized plan/review summary, not raw transcripts.

Decide **continue extension / integration blocked / trial incomplete** from evidence. Mark only this slice complete if all mandatory checks pass; not all of step 1 or the whole system. Commit checked changes locally on success and report the commit. Do not advance automatically or install a fallback in this run. Push only if requested for that implementation run.

## Mandatory success checks

- Exact Studio 2.0.1 pin, payload/patches/notices and supported installation established; UI/backend/payload and extension-session Bun checks pass.
- Real fixture planning and independent specialist review occur through the app/Crew integration.
- Hook ownership and genuine human checkpoint evidence are established; a premature transition is refused without code changes.
- Settings/context/identities and actual native parent usage are recorded; partial child attribution is disclosed as remaining work.
- Planning stops awaiting the user's technical-plan approval; no construction, merge or impersonated approval runs.
- Extension/pending-artifact availability survives normal VS Code task restart; no second startup command is required.

## Stop and rethink rule

**At the first mandatory failure or missing required evidence, stop dependent work.** No automatic retry, candidate/provider switch, suppression, permission weakening, upgrade or workaround in the same run. Independent inspection of the failing check and writing its result report are allowed.

Report expected/actual behavior and exit code, redacted evidence, changed state, anything running, and later checks not run. Preserve unrelated work. Label hypotheses and propose the simplest next experiment. A needed user action not performed is **NOT RUN / awaiting evidence**, not FAIL or PASS. Revise the plan with the user before a replacement trial.

## Copyable prompt for the next Codex session

```text
Work in /home/zsom/MultiAgenticSystem. Read docs/UPGRADE_0.13.0.md and
docs/STEP_1_RESULTS.md. Reuse Crew 0.13.0, Studio 2.0.1, local Bun and the
installed CrewLab harness. Verify live Studio health and CrewLab hook consent,
then start section C with CrewLab's tasks/01-fix-oversell.md exercise.
Read AGENTS, README, WORK_PLAN, RESEARCH_ALIGNMENT and the extension research.

Crew is our fixed, trusted foundation. Reuse native features and the supplied
extension/bridge first, adapt existing components for real gaps, then implement
only what is missing. Do not benchmark or replace Crew or install several
lifecycle systems. Preserve both planning approvals, smart multi-tool worker
selection, context handling, credit-aware decisions and independent review.

This prompt authorizes the bounded planning/reviewer sessions in the plan.
Preserve the installed app, harness, payload versions and notices;
no blanket trust, unrelated upgrade, global agent replacement or Crew patches.
Use ordinary Git here, no worktrees. All normal startup/restart uses the
existing VS Code task Kiro Crew: Start. If UI/auth action is needed, identify
it and wait for evidence; do not launch a substitute gateway.

Use the CrewLab exercise, actual planning and a separate review. Verify the
extension's hook/human-gate behavior, native usage, settings and context.
Stop awaiting technical-plan approval; do not approve for me, implement,
advance stages or pretend partial attribution proves complete metering.

At the first mandatory failure, stop dependent work, write expected/actual
behavior and changed state in docs/STEP_1_RESULTS.md, propose the next
experiment and end the run. Do not auto-retry or switch candidates. If all
checks pass, commit the bounded result locally, report remaining gaps and
stop. Do not declare the whole step/system complete or push unless requested.
```
