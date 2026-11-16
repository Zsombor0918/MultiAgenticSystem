# Extensions for our existing Kiro Crew foundation

Research date: 2026-11-16. **Current recommendation after the user's clarification.** Crew is already selected and trusted. This document researches the remaining capabilities; it does not reopen the runtime choice. No apps, libraries, or dependencies were installed, enabled, or run during this research.

## The reuse order

For each requirement: **use native Crew → use an existing Crew extension → adapt a compatible external component → implement only the uncovered gap**. An extension's compatibility still needs an acceptance check; that is different from re-benchmarking Crew or trying to replace it.

The [complete-system survey](COMPLETE_SYSTEMS_2026-11-16.md) remains useful background, including BMAD, AgentSys, GSD, metaswarm, Workgraph, and ADW. Its earlier BMAD-first trial recommendation is superseded by the Crew-specific findings here. A framework can supply its library/procedures without becoming another runtime.

The required product stays:

`ChatGPT + GitHub issue → Crew actionable plan/review → your approval → intelligently delegated implementation → tests + independent review → PR/report → your merge decision`

**Scope clarification (2026-11-16):** A second, separately approved detailed implementation plan is available for complex/high-risk tasks, but is not a mandatory phase. One plan must be concrete enough to authorize implementation safely. This clarification supersedes the earlier two-plan wording in this dated research.

Planning and execution both need specialist/skill selection, backend/model/effort choices, real capability knowledge, resource-aware decisions, and focused context. Normal startup is always **VS Code → Kiro Crew: Start**. No worktree requirement for this repository.

## 1. What is already available for Crew

Inspected the installed 0.12.2 sources, Crew's official app registry, and actual extension repositories. The registry and current main can describe apps moved out of later Crew releases; that does not require upgrading our installation. Use the installed version's app contract and exact selected extension pin.

| Requirement | Existing Crew feature / extension | What we should reuse | Remaining integration |
| --- | --- | --- | --- |
| Reviewable technical and implementation planning | **Spec Builder**, shipped in installed Crew | Requirements → Design → Tasks artifacts, phase review, recorded document hashes, execution handoff | Map the approved issue to requirements; design to technical plan; tasks to implementation plan with explicit proposed code changes. Add separate specialist review and smart worker dispatch |
| A coherent specialist lifecycle already packaged for Crew | **AI-DLC Studio**, real third-party Crew App | AI-DLC specialists/stage engine, Action Center, approval evidence, transactional per-project installation, recovery and cross-project overview | First extension trial candidate. Verify genuine pre-code approval and optional second-plan support, native hooks, scope selection, worker ownership, and cross-backend adaptation |
| Independent final code review | **Code Review Sage**, shipped in installed Crew | Separate PR session, risk-weighted diff review, model/effort/concurrency controls, findings before publication | Link reviewed revision to acceptance/checks; keep the implementer separate; do not auto-publish or merge. Pre-PR local review can use a separate Crew worker with a compatible review skill |
| Worker sessions, completion, models and supported effort | **Crew spawn/run controls** | Existing Kiro/Codex dispatch and explicit selection, existing run IDs | The selected lifecycle must use/map to these controls when we require cross-backend decisions; native Kiro grandchildren alone do not establish that |
| Know tool/backend capabilities | **Crew backend capability cards**, live model/effort lists | Read native capability data rather than manually duplicating the entire backend matrix | A compact coordinator view adds task-specific constraints and actual account/version observations, preserving unknowns |
| Economical model selection | **Crew Decisions/Jev**, including optional `model_route_derive` | Native skill/model selection; derivation from live offered models and credit multipliers; eligible unpinned subagent starts | Explicit backend/role/effort/context and remaining-allowance policy where native behavior does not cover it. Respect manual pins and native consent/settings |
| Credit/token visibility | **Crew usage/session/account sources**; Issue Radar's existing pipeline views where relevant | Native Kiro credits, available Codex token/cache data, account freshness, parent/run links | Expose a concise coordinator-readable summary; link selected lifecycle phases and any nested workers. Missing data remains unknown |
| Context and learning | **Crew memory/inheritance, skill lazy loading, checkpoints and optional memory decisions** | Existing controls and compact selected-library artifacts | Role-specific handoffs, explicit inheritance and measured recovery; add external indexing only for an observed gap |
| Durable work/acceptance | **Crew work ledger and saved workflows** | Existing work/session/acceptance records and repeatable native execution | Link issue, applicable plan revision(s)/approval(s), worker IDs, checked revision, independent review and usage. Add only missing fields/links |

Sources: [Crew apps guide](https://github.com/kirodotdev/KiroCrew/blob/v0.12.2/src/kiro_crew/docs/apps.md), [Spec Builder procedure](https://github.com/kirodotdev/KiroCrew/blob/v0.12.2/src/kiro_crew/apps/builtins/spec_builder/skills/spec-workflow/SKILL.md), [Spec Builder approval handling](https://github.com/kirodotdev/KiroCrew/blob/v0.12.2/src/kiro_crew/apps/builtins/spec_builder/backend/parsers.py), [Code Review Sage manifest](https://github.com/kirodotdev/KiroCrew/blob/v0.12.2/src/kiro_crew/apps/builtins/code_review_sage/app.json), [backend cards](https://github.com/kirodotdev/KiroCrew/blob/v0.12.2/src/kiro_crew/agent_sdk/backend_cards.py), [native routing implementation](https://github.com/kirodotdev/KiroCrew/blob/v0.12.2/src/kiro_crew/decisions/points/model_route.py), [routing configuration](https://github.com/kirodotdev/KiroCrew/blob/v0.12.2/src/kiro_crew/config/sections_decisions.py), [usage routes](https://github.com/kirodotdev/KiroCrew/blob/v0.12.2/src/kiro_crew/dashboard/routes/system.py), [work ledger](https://github.com/kirodotdev/KiroCrew/blob/v0.12.2/src/kiro_crew/docs/work-ledger.md), [workflows](https://github.com/kirodotdev/KiroCrew/blob/v0.12.2/src/kiro_crew/docs/workflows.md).

These are existing implementations, not claims that our final combined workflow is already configured. In particular, Spec Builder's normal handoff executes in the same session; it is not yet the user's dynamic multi-tool specialist team. Its approval data can identify stale document hashes, but its agent-writable index is not an adversarial security boundary.

### A useful correction about native model routing

Crew's installed `model_route_derive` can derive empty difficulty tiers from the live offered model list and credit multipliers. With its prerequisites enabled, eligible subagents started without a model can also be routed. Thus “Crew never routes subagents” is too broad, and building a replacement model ladder first would duplicate existing work.

This still does not establish the full requested choice of **backend + specialist + skill + effort + context + current allowance**. Credit multipliers describe relative model pricing, not remaining account balance. Explicit profile settings and usage-aware phase decisions remain necessary. The general Decisions guide is narrower than the optional derivation source; use the exact inspected implementation and configuration rather than resolving that discrepancy by assumption.

## 2. AI-DLC Studio: the most relevant newly found Crew extension

[AI-DLC Studio](https://github.com/warren830/kirocrew-app-aidlc) is explicitly a Kiro Crew app, not a hypothetical port of upstream AI-DLC. The [official Crew catalog](https://github.com/kirodotdev/KiroCrewApps/blob/50d8fd36e64a878e6aec853530c5e7f4c3ec279a/catalog/official-registry.json) lists `aidlc-studio`. The app gives a shared queue of gates/questions/recovery decisions, artifacts and reviewer evidence, stage maps, repository registration, and receipt-backed harness installation/rollback. It uses Crew's own conversations and lifecycle hooks.

**Version distinction matters:**

| Variant | Checked source | Crew minimum | Bundled AI-DLC | How to interpret it |
| --- | --- | --- | --- | --- |
| Official catalog entry `v1.0.1` | `26b36c4a4ab0a73088a09c5a0e93a60260699e30` | 0.3.0 | 2.7.1 | Store listing is real, but it is the older package |
| Current release `v2.0.1`, also main/v2 at inspection | `8b3881d4737399c3394d8d187f102a5c95d6e528` | 0.11.0 | **2.11.3 + four documented local patches** | Proposed trial pin for our installed Crew 0.12.2; do not confuse it with catalog 1.0.1 or upstream AI-DLC 2.11.4 |

Sources: [catalogued manifest](https://github.com/warren830/kirocrew-app-aidlc/blob/v1.0.1/app.json), [2.0.1 manifest](https://github.com/warren830/kirocrew-app-aidlc/blob/v2.0.1/app.json), [payload provenance](https://github.com/warren830/kirocrew-app-aidlc/blob/v2.0.1/payload/manifest.json), [retained licenses and patches](https://github.com/warren830/kirocrew-app-aidlc/blob/v2.0.1/THIRD_PARTY_NOTICES.md).

The app is Apache-2.0; its bundled AI-DLC is MIT-0. The four local patches include Crew host-turn/host-notice handling. This matters to human approvals: a host notification must not become evidence that the user approved a stage. Reuse the supplied bridge and patches first rather than writing our own approximation.

The [backend lifecycle module](https://github.com/warren830/kirocrew-app-aidlc/blob/v2.0.1/backend/hooks.py) starts/stops its services with the gateway. Its [session bridge](https://github.com/warren830/kirocrew-app-aidlc/blob/v2.0.1/backend/studio/sessions.py) observes Crew state and binds intent/session records. Human confirmations are sent by the browser through the normal chat API; the backend does not privately impersonate user turns. Its documented checks for delivery/state evidence are useful existing robustness work.

**What it does not settle for us:**

- It needs **Bun** reachable both by the gateway and AI-DLC conversations. The current guide recommends 1.4.4 or newer. Bun was not found on the research shell's PATH; that alone does not establish every possible configured path. Verify/install the selected dependency during the trial, not during research.
- The selected app source/installed artifact must contain the correct UI bundle. Its source build uses Node/npm; inspect the actual installation path and artifact rather than assuming `--no-build` works. First-time setup is acceptable; no additional normal startup is needed.
- Its README explicitly provides **no unattended mode** and stops for human checkpoints. That fits required approvals, but do not enable an auto-continue loop that could masquerade as a human answer. Configure necessary stages/reviews; do not force all 33 stages on every tiny issue.
- The current bundle's [usage module](https://github.com/warren830/kirocrew-app-aidlc/blob/v2.0.1/payload/aidlc-kiro/.kiro/tools/aidlc-usage.ts) still has only a Claude producer, not Kiro/Codex metering. We must retain Crew's sources and map phase/run attribution.
- Model/effort pickers for a conversation or Advisor do not prove dynamic Kiro/Codex specialist routing. Its bundled native Kiro delegation needs a supported Crew dispatch mapping for the final multi-tool behavior.
- The [older Docker installation verification](https://github.com/warren830/kirocrew-app-aidlc/blob/v2.0.1/docs/verification/2026-09-17-docker-install/README.md) covers an older app/host and explicitly excludes model calls. It is not a local end-to-end PASS for this version.

### The hook question is narrower than the earlier survey suggested

Crew's source deliberately omits the native ACP `hooks` advertisement to avoid duplicate execution. Further inspection found its existing [spec-hook runner](https://github.com/kirodotdev/KiroCrew/blob/v0.12.2/src/kiro_crew/agent_sdk/spec_hooks.py): it runs supported agent-spec hooks in Crew's turn loop for backends that need it; ordinary kiro-cli can run its own. This is an existing integration surface, so the missing advertised flag is **not** sufficient reason to reject AI-DLC Studio or demand a new hook bridge.

The app bundles agent-spec hooks plus its own Crew compatibility patches. Verify the selected route's actual hook ownership, project-agent resolution, human-turn recording, and write-denial result. Reuse native handling; do not flip handshake flags or patch Crew speculatively. If this acceptance check fails, report the concrete extension incompatibility and stop the trial.

**Recommendation:** evaluate this ready-made Crew extension before porting a whole external framework. Keep Spec Builder as the lighter native planning option if Studio's ceremony or integration costs outweigh its reusable lifecycle machinery. Use one primary lifecycle; do not make both control the same task.

## 3. Other Crew extensions checked

| Extension | Evidence | Reuse decision |
| --- | --- | --- |
| [Agent Dashboard](https://github.com/brunokktro/agent-dashboard) | Real Crew app, official catalog pin `f206d494d7edd9811f3bc9f3f02eefe9a74918cf`, MIT; app manifest 3.3.5 | Optional operations view. It reads its ecosystem's runs.db/queue/scheduler data; an adapter would still be needed. It is not our missing native credit meter or smart router. Avoid a second dashboard initially |
| [Crew Manager](https://github.com/xuejinT/crew-manager-app) | Real Crew UI package; catalog entry exists, while README still calls it a beta and describes provisional Done results | Optional later intervention overview. Do not use its Done category as acceptance proof or add it just for another control panel |
| [Skill Genie](https://github.com/Fei2-Labs/skill-genie) | MIT; explicitly installs to Crew's skills path as well as other tools | Genuine Crew-aware library distribution option. Prefer native extra paths/imports for our custom `KIROCREW_HOME`; broad global setup is unnecessary for the pilot |
| [Kirometer](https://github.com/nicholas-c/kirometer) | Real Crew app reads approvals/activity/credits and drives an ESP32 display | Evidence that Crew data can be consumed by an app, not a needed dependency. Hardware is irrelevant here, and README explicitly grants no project license; do not copy its code |
| [Everything Kiro](https://github.com/iamaanahmad/everything-kiro) | Kiro IDE configuration/agent/steering collection, not a demonstrated Crew package | Reference only. IDE schema compatibility and redistribution permission were not established for Crew; don't install its entire configuration |
| Native **Dev Fleet** and `kirocrew-dev` prepare-PR/worktree skills | Installed app explicitly serves development of Crew itself; prepare-PR says it is for the Crew repo and includes merge automation | Do not adopt wholesale into this reusable product. Repo-specific release/CI rules and worktree defaults are not our workflow |

The focused search used GitHub repository/readme queries, the official registry's 35 authored entries at the checked revision, installed manifests and source, and selected extension files. It did not establish a ready Crew extension implementing the complete cross-backend, effort-, context-, and remaining-credit-aware worker policy. This is a bounded negative finding, not a claim that no such project exists anywhere.

## 4. Portable components to use only for remaining gaps

| Gap after native/Crew-extension reuse | Existing component worth trying | Actual adaptation boundary |
| --- | --- | --- |
| Additional planning/engineering specialist procedures | **BMAD 6.12.4** | Coherent library with explicit Kiro/Codex targets; preserve renderer/configuration assets and map worker tools. Disable approval-bypassing oneshot defaults |
| Lean implementation/TDD/debugging/review discipline | **Superpowers** and selected existing engineering skills | Translate host dispatch and exact review context to Crew; don't import another autonomous controller |
| Role model maps and escalation/reference team behavior | **metaswarm** | Reuse selected policy/procedures if licensed and useful; its BEADS/team runtime need not be installed |
| Backend-local quota/failure routing | **ADW model router** | Adapt only policy not covered by Crew; current inspected probes do not establish Kiro, and failed probes are not a budget guarantee |
| Focused phase/review handoffs | **GSD / Workgraph** | Reuse compact-context and task/risk principles without importing unsupported host commands, Linear, automatic merges, or a worktree mandate |
| Missing usage parser/data shape | **agentic-coding-harness** | Inspect only a proven telemetry gap; its Kiro proxy calibration warns estimates can differ sharply from session credits. Keep native accounting first |
| Older full next-task procedures | **AgentSys legacy** | Historically relevant, but a required pinned plugin repository returned 404; no critical dependency until complete source access is reproducible |

Exact evidence and pins are in the [broader comparison](COMPLETE_SYSTEMS_2026-11-16.md) and its inventory. Do not import every candidate. If Studio already supplies suitable specialists and artifacts, an additional whole BMAD lifecycle is unnecessary. Add only the procedure the chosen library actually lacks.

## 5. Small custom pieces only if existing surfaces leave these gaps

**First: a worker-selection policy.** Use native capabilities, live models/effort, task risk/role, recent usage/allowance and context needs to choose a supported Crew spawn combination and record why. Preserve review quality. Prefer native Decisions/configuration; adapt a small reviewed policy only for uncovered backend/effort/resource decisions. A rule table is enough initially; no trained router or second scheduler is needed.

**Second: usage and lifecycle linkage.** Read Crew's existing records and give the coordinator a concise phase/run summary with source, units, freshness, coverage and available allowance. Join the chosen extension's intent, the issue, required plan approval (and an optional second approval), worker IDs and checked revision using existing work/session records first. Add a small linking record or read-only tool only if those surfaces cannot express it. Unknown cost/quota stays unknown and affects the next decision.

**Third: any demonstrated gate/dispatch mismatch.** Reuse the chosen app's approvals, native spec hooks and separate-worker tools. If a versioned approval or independent reviewer is lost at a handoff, fix that specific adapter boundary. Do not build another lifecycle engine merely because adaptation is possible.

Context profiles and shared skill registration should primarily be configuration and concise instructions. No vector database, custom memory service, replacement dashboard, or automatic learning infrastructure is justified by the current evidence.

## 6. The practical sequence

1. **Trial the existing Crew extension:** AI-DLC Studio 2.0.1 at the checked pin, against a harmless fixture, through the current VS Code start path. Confirm its exact payload/dependencies, real specialist planning/review and user gate behavior. Stop before implementation. This tests extension fit, not whether Crew is a good runtime.
2. **Connect native intelligence and accounting:** use native capability/model data, Decisions where applicable, real usage/allowance and focused context; expose only the missing coordinator view/policy. Establish whether extension-native children can be attributed/controlled or must map to Crew workers.
3. **Complete right-sized planning and implementation:** approved issue → actionable plan/review → owner approval → workers/tests/independent review → PR/report, with human merge. Insert a second technical-to-implementation planning gate only when the task warrants it. Reuse Code Review Sage or a separate native reviewer path as appropriate.
4. **Exercise one real issue and another project**, including changed-plan approval, cancellation/restart, telemetry gaps and rejected review. Commit each checked step.

If Studio fails a mandatory acceptance check, record it and stop. The next considered option is native Spec Builder plus the smallest needed portable specialist set, potentially BMAD. Do not automatically switch in the same failed run. [NEXT_STEP.md](../NEXT_STEP.md) contains the bounded prompt and failure rules.

Keep **5–7 focused working days** as a conditional usable-pilot target, not a measured promise. Day 2 should reveal whether native extensions avoid major host/dispatch changes. If they do not, revise the estimate or approach explicitly while preserving the core requirements. This research makes the reuse choices concrete; it does not prove adapter effort is small.
