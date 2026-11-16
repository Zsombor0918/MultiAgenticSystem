# Next run: integrate the existing AI-DLC Studio Crew extension

Prepared: 2026-11-16. Status: **STOPPED after the first actual VS Code task failed (exit 1)**. The launcher's nonexistent custom embedding path makes doctor fail. Studio remains installed/recorded enabled; offline checks passed, but live section C is NOT RUN. Read the failure and proposed minimal correction in [STEP_1_RESULTS](STEP_1_RESULTS.md). Agree that correction with the user before applying it or retrying; do not reinstall components or repeat passed checks without cause.

**Kiro Crew is fixed and trusted.** This run checks a ready-made extension against our workflow; it does not reconsider or benchmark Crew. Read the [current extension research](research/CREW_EXTENSIONS_2026-11-16.md), [extension source inventory](research/CREW_EXTENSION_SOURCES_2026-11-16.json), and [system plan](../WORK_PLAN.md). This supersedes the earlier diagnostic-skill and BMAD-first experiments.

Reuse order: native Crew → existing Crew extension → portable/adapted component → implement only the remaining gap. The proposed first extension is **AI-DLC Studio 2.0.1**, commit `8b3881d4737399c3394d8d187f102a5c95d6e528`. It bundles **AI-DLC 2.11.3 plus four documented patches**; it is not upstream 2.11.4. The official store currently lists older Studio 1.0.1, so do not accidentally test that while reporting 2.0.1.

## The bounded outcome

**Resume point after agreement:** correct the launcher configuration as recorded in the results, verify that change, then obtain a new actual VS Code task result before extension backend/Bun health and section C. Component/capability records already exist. The fixture is prepared but its AI-DLC harness is not installed yet. Keep the source/payload pins; no alternative candidate has been installed.

Use the actual extension to produce a code-grounded technical plan and separate specialist review for a tiny fixture issue. Verify a real human approval checkpoint, then stop **awaiting the user's technical-plan approval**. Record precisely what remains to connect Crew's backend/model/effort choices, context and usage to the extension.

The detailed implementation plan, second approval, code changes, CI, independent code review, delivery and portability remain required later steps. No mock plan, mere installation, or discovery response counts as a successful planning/review integration.

## Facts and unknowns

- Installed Crew 0.12.2 meets Studio 2.0.1's declared minimum 0.11.0. Existing Kiro/Codex delegation is trusted; do not repeat its old benchmark. Check only changed or extension-specific prerequisites.
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

Use ignored `.runtime/pilots/aidlc-studio-2.0.1/` for the pinned checkout and a small separate fixture project. This is not a worktree. Record a sanitized fixture/asset manifest so the experiment can be reproduced. Keep raw generated outputs ignored.

Running the execution prompt below authorizes the bounded app/dependency installation, per-app enablement/trust, fixture harness installation and planning/reviewer sessions described here. **The research turn does not perform them.** Prefer project-local dependency placement where supported; inspect the exact changes before invoking installation. No blanket third-party trust, unrelated upgrade, sandbox weakening, global agent replacement, or patching installed Crew/adapter code.

Use the installed Crew app contract and exact selected version. Preserve existing configuration and back up local changes. Verify the declared UI entry/build, backend health, bundled payload hashes and Bun reachability from the actual extension sessions. Use Studio's supplied transaction/receipt flow to install into the fixture; inspect the affected `.kiro` paths, settings and optional MCP dependencies. Do not silently enable unrelated integrations just because the payload lists them.

Keep normal startup behind **VS Code → Tasks: Run Task → Kiro Crew: Start**. Integrate only necessary repeatable environment/configuration preparation into its existing launcher. One-time installation/authentication is setup, not another normal start command. Do not start a second gateway or separate daemon. If the executor cannot operate the VS Code UI, identify that user action and wait for evidence; do not substitute a shell-launched gateway or claim the task was clicked.

## C. Exercise only planning, review and its user gate

1. Register the harmless fixture through Studio's supported flow. Use a tiny issue with actual source, acceptance criteria and one design decision, such as proposing validation for a small command-line parser. It is an input fixture, not permission to implement. The final product's intake remains an approved GitHub issue; no dummy remote issue is required here.
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
Work in /home/zsom/MultiAgenticSystem. Read docs/STEP_1_RESULTS.md and resume
only with the user's agreement on the proposed correction after the recorded
startup failure. Without that agreement, report the failure and proposed change;
do not apply it, retry startup or advance to section C. Once agreed, correct and
verify startup, obtain actual VS Code task evidence, then resume section C and
results/commit. Reuse the prepared Studio 2.0.1 installation,
local Bun and fixture; do not reinstall or rerun passed checks without cause.
Read AGENTS, README, WORK_PLAN, RESEARCH_ALIGNMENT and the extension research.

Crew is our fixed, trusted foundation. Reuse native features and the supplied
extension/bridge first, adapt existing components for real gaps, then implement
only what is missing. Do not benchmark or replace Crew or install several
lifecycle systems. Preserve both planning approvals, smart multi-tool worker
selection, context handling, credit-aware decisions and independent review.

Inspect the pinned manifest/installer first. This prompt authorizes bounded
app/dependency setup, per-app trust/enablement, fixture harness installation
and planning/reviewer sessions in the plan. Preserve payload versions/notices;
no blanket trust, unrelated upgrade, global agent replacement or Crew patches.
Use ordinary Git here, no worktrees. All normal startup/restart uses the
existing VS Code task Kiro Crew: Start. If UI/auth action is needed, identify
it and wait for evidence; do not launch a substitute gateway.

Use a harmless fixture, actual planning and a separate review. Verify the
extension's hook/human-gate behavior, native usage, settings and context.
Stop awaiting technical-plan approval; do not approve for me, implement,
advance stages or pretend partial attribution proves complete metering.

At the first mandatory failure, stop dependent work, write expected/actual
behavior and changed state in docs/STEP_1_RESULTS.md, propose the next
experiment and end the run. Do not auto-retry or switch candidates. If all
checks pass, commit the bounded result locally, report remaining gaps and
stop. Do not declare the whole step/system complete or push unless requested.
```
