# System and build plan: intelligent Crew development workflow

Updated: 2026-11-16. Status: research and repository preparation complete; component integration has not started.

This plan follows the user's clarified workflow. Smart delegation, model/effort selection, a reusable skill and agent system, credit monitoring, and context handling are core requirements. “Minimal work” means assembling existing working components with the least necessary adaptation while preserving those requirements.

## 1. The intended workflow

```text
User + ChatGPT discussion
  → agreed strategic GitHub issue through the GitHub plugin
  → issue handed to Kiro Crew for the selected repository
  → repository-based technical/solution plan
  → user review and approval
  → detailed implementation plan with proposed code changes
  → user review and approval to implement
  → intelligently delegated implementation
  → shell tests / CI + independent code review
  → PR and evidence / resource-use report
  → human merge decision
```

ChatGPT is where the user explores ideas, weighs options, and agrees what should be built and why. ChatGPT uses the GitHub plugin to create the approved issue using the target project's templates and conventions. The issue describes the goal, scope, risks, dependencies, and acceptance criteria; Crew determines the code-level solution from the actual repository. The normal handoff is an issue URL and target project, not the whole ChatGPT conversation. This repository does not need to build a replacement ChatGPT interface or GitHub plugin.

Crew prepares the technical plan and can delegate repository research, architecture, and plan checking to appropriate specialists. After review of that direction, it produces the implementation plan: affected files and interfaces, proposed code changes or sketches, task order/dependencies, verification commands, agent/skill assignments, and assumptions. Planning does not apply the proposed changes. The latest user clarification makes both planning stages part of the target flow; combining them for trivial work would be an explicit later simplification, not a silent omission.

The user decides goals, approvals, scope changes, and merge. Crew handles routine selection and coordination of agents, backends, models, supported effort levels, skills, tools, and context in both planning and implementation. TARS is the inspiration for the reusable specialist/skill system. Kiro and Codex are the initial coding tools. The product must work across projects, with KovacsTrader as one possible user.

## 2. The system we assemble

| Layer | Existing foundation | Integration we need |
| --- | --- | --- |
| Startup | VS Code task and current Crew launcher/dashboard | Keep all normal startup behind **Kiro Crew: Start**, including shared skills/configuration |
| Orchestration | Crew delegation, run/completion records, Task Runner / Dynamic Workflows where appropriate | Connect the approved lifecycle using supported native mechanisms and adapted workflow procedures |
| Capability catalogue | Actual Kiro/Codex models, tools, session settings, permissions, and telemetry | Give Crew an evidence-backed description of what each tool can actually do |
| Agent and skill library | Crew skill search/loading, existing profiles, researched engineering skills | Curate, pin, adapt, and test compatible specialists and skills; let Crew select and apply them |
| Smart delegation | Supported spawn parameters, Crew decision mechanisms, researched routing policies | Choose backend + agent + model + effort + skills + context per task using capabilities, risk, usage, and prior results |
| Context management | Crew memory/project inheritance, lazy loading, compaction, checkpoints | Define and verify role-specific context packs, context budgets, and restart/handoff behavior |
| Credit and usage monitoring | Crew usage ledger and available account-usage views | Expose per-phase/per-run usage and available remaining allowance to both user and coordinator |
| Quality and delivery | Target project's tests, GitHub/CI, separate review worker | Connect final code revision to acceptance criteria, checks, review, and PR/report |

Crew remains the runtime. The repo contains reusable configuration, selected upstream skills/profiles, workflow instructions, and the small adapters proven necessary. Prefer native capability, then configuration, then a compatible existing component, then a thin adapter. Reuse actual files/code when they fit; do not rewrite working components merely to give them local names. Inspect dependencies, permissions, and licenses and pin adopted revisions. Do not install several complete orchestrators together.

Use Crew's existing records and target-project conventions for durable state. Add a small linking record only when needed to associate the issue, plan versions/approval, parent/worker runs, revision, verification, and resource use. Credentials and raw local sessions stay out of Git.

## 3. What makes delegation smart

### Capability knowledge

Before relying on a backend, record its verified version and route, available model IDs, supported/applied effort controls, native tools, permission behavior, context limits where exposed, usage metrics, quota visibility, and important limitations. Distinguish observed, documented, untested, and unsupported behavior. Refresh capabilities when versions, account access, or configuration change.

An agent role such as researcher, architect, planner, implementer, debugger, reviewer, or documentation specialist is separate from the backend running it. A skill supplies a procedure; the worker supplies tools and model capabilities. Build a curated library from the research and grow its coverage incrementally. The first pilot may run specialists sequentially, but that does not limit the target to three fixed agents or three permanently hardcoded skills.

### Model, effort, tool, and skill selection

For every delegated planning or implementation task, the coordinator evaluates task type, complexity, risk, required tools, context size, available allowance, and known results. It selects a supported combination and records a short reason. The user should not assign each model or effort manually.

Start with understandable rules over verified profiles, adapting the researched Workgraph/ADW policies. Use Crew's own routing where it covers the need. If it cannot choose the required worker combination, adapt a small policy before the existing spawn operation; do not build another scheduler. Role names in this plan are not invented Crew configuration keys.

Prefer an economical capable option for clear work; use stronger reasoning where ambiguity/risk requires it. Separate environment/permission failures from reasoning failures before escalating. A low remaining allowance can lead to a suitable alternative profile/backend, smaller work units, or a pause. Preserve the required capability and review quality. Never treat missing price/quota data as free or unlimited usage. Log requested and actual backend/model/effort where exposed, including unsupported or unapplied settings.

Begin with one active worker and at most one correction round per task. Later parallelism and automatic policy tuning are improvements to a working system. Feedback from success, review findings, retries, time, context, and resource use should inform profile changes from the first pilot; a trained/self-learning router needs more evidence.

## 4. Smart context handling is part of the core

- Keep shared project rules, issue scope, approved decisions, and acceptance criteria available to every relevant role. Load role/path-specific material only when needed; do not copy KovacsTrader's particular context limit into all projects.
- Give each worker a compact handoff: issue reference, absolute project root, current revision, phase, approved plan/task, relevant files, constraints, skills, and verification expectations. Inspect actual prompt/session evidence to check what was inherited.
- Keep the coordinator's working context focused on decisions and progress. Workers return findings and evidence summaries rather than entire file dumps or chat histories. Use Crew's native memory/project/lessons controls and lazy skill loading deliberately.
- Keep the implementer's session for a bounded fix when useful; give reviewers a fresh context with the requirements, diff, and test evidence. Do not pass the implementer's reasoning as proof.
- Use checkpoints and measured context pressure to decide when to split work or start a fresh session. Preserve approvals and scope across compaction/restart, and invalidate stale plans/results when inputs change.
- Record available context/token metrics alongside handoff size. Document bytes, model tokens, and cache reads are different measurements. Verify backend-specific compaction rather than assuming the same control works everywhere.

Start with native Crew context facilities. Evaluate the researched Repomix or Aider repo-map approach only if relevance or context volume remains a demonstrated gap; adapt an existing solution before writing an indexer.

## 5. Credit monitoring and usage-aware decisions are part of the core

Our local research already records Kiro credits and partial Codex token/cache data in Crew logs, plus code for a Kiro account-usage view. Build on those first. Per-task metering and remaining account allowance are different inputs, and account usage can include other sessions.

From the first integrated planning run, collect the coordinator, planning/research, implementation, review, failed attempts, and corrections. Link usage to issue, phase, parent/worker run, requested/applied profile, time, result, and retries. Join backend identity from run records when the usage row says only `acp`. Avoid summing cumulative and incremental records twice. If some phases cannot be measured, label the coverage as partial.

Before a new phase or delegation, consult available recent usage/allowance and the configured resource policy. Show source, unit, freshness, and missing data. At phase boundaries, report consumed resources and decide whether to continue, change to a suitable supported option, split work, or ask the user. This makes monitoring an input to routing, not just a final dashboard number.

Keep Kiro credits, Codex input/output/cache tokens, available quotas, measured currency costs, and estimates distinct. Unknown financial costs stay unknown. Use native views when sufficient; adapt an existing parser/data model or add a small read-only summary when needed. The monitoring requirement is mandatory; a separate reporting service or new UI is not.

Start with visible thresholds, bounded runs, and phase decisions. Our research does not prove a shared cross-provider financial hard cap, complete subscription pricing, or a ready learning optimizer. Do not promise those guarantees or copy ADW's budget behavior without compatible metering and enforcement.

## 6. Reuse decisions from the research

The detailed [research alignment](docs/RESEARCH_ALIGNMENT.md) connects each requirement to prior findings and candidate components. It is the component integration shortlist, not a claim that everything is installed or Crew-compatible.

- **Lifecycle and planning:** inspect reusable parts of agent-pipeline, Superpowers/GSD, and Workgraph/Lousy issue decomposition. Start with the smallest compatible set that supports the two plans and review boundaries.
- **Agents and engineering skills:** use Crew profiles/discovery and researched sources such as agent-crew, Sentry, and the focused planning/testing/debugging libraries. Build a curated library and verify selection and actual use.
- **Routing:** Crew decisions plus Workgraph task/risk/model/effort policy and ADW's usage/failure model ladder. The researched ADW router is within a backend; Crew-wide selection needs adaptation where native behavior falls short.
- **Monitoring:** Crew ledger/account views first; inspect agentic-coding-harness parsing/normalization if native reporting leaves a real gap. Keep Crew in charge of workers.
- **Context:** Crew inheritance/lazy loading/checkpoints first; Repomix/Aider are researched fallback candidates for repo mapping.

Workgraph's current package differs from the five-skill version in the attachment and carries Linear/other host dependencies. Inspect or pin a suitable version/component rather than blindly importing its current runtime. External research citation identifiers are not portable evidence. Resolve exact source/revision, file, dependencies, license, and compatibility before adopting a component; mark unresolved candidates as such. TARS is an architectural reference, not an assumed available installation.

## 7. Incremental implementation order

Develop directly here. For each step: assemble one useful capability, check it in the real Crew path, update the evidence/status, and commit. No Git worktree is needed for this repository. Every step preserves the single VS Code startup task. First-time setup, login, and genuine approval decisions may require user action.

### Step 1 — Establish the capability and component foundation

Confirm installed versions and what Crew can already expose for Kiro/Codex, skill discovery, context, and usage. Turn the research shortlist into exact adopt/adapt/native/defer choices for the first integrated path, with pinned sources and licenses for imports. Create the initial capability catalogue, including unknowns, without another broad research project. Keep shared configuration and library loading behind the existing startup task, including when another target project is selected.

**Deliverable:** Crew can access its known tool capabilities and chosen component library through the one start path. Remaining adaptation work is specific and recorded. Check actual loading and task start/stop/restart.

### Step 2 — Connect usage and context to the coordinator

Expose native per-run usage and available allowance with their provenance and coverage. Add only necessary reporting glue. Establish the role-specific handoff/context policy, inheritance settings, and context measurement. Record usage for the first trial runs and demonstrate a resource threshold or unavailable-telemetry decision before further delegation.

**Deliverable:** the coordinator can inspect resource/capability information and prepare focused context before choosing workers. The user can see measured usage and missing data. This precedes the full planning/implementation pipeline so its decisions can use these inputs.

### Step 3 — Assemble the agent/skill library and smart delegation

Install/adapt the selected existing profiles and skills for the first issue's research, planning, plan checking, coding, testing/debugging, and review needs. Connect Crew discovery and selection. Adapt routing policy for backend, agent, model, supported effort, skills, tools, and context. Test distinct representative assignments, including a usage-pressure or unavailable-capability case, without a large benchmark.

**Deliverable:** Crew selects and actually applies suitable components and model/effort settings for planning and execution tasks; the user does not manually dispatch every worker. Decisions, context, usage, and completion IDs are traceable. Verify native tools and permissions through the worker path.

### Step 4 — Connect the two planning stages and GitHub handoff

Document the ChatGPT → approved strategic GitHub issue → Crew handoff. Assemble code-grounded technical planning, plan review/owner approval, then detailed implementation planning with proposed code changes and approval to execute. Reuse the selected planning/audit skills and native gates. If gates need glue, add only the missing enforcement.

**Deliverable:** an issue produces the two distinct, reviewable plans with appropriate specialist/skill/model choices and resource records. Check that unapproved or materially changed plans cannot start implementation and that planning cannot apply project code changes. Keep tests on designated harmless files here.

### Step 5 — Connect implementation, checks, independent review, and delivery

Execute approved tasks using smart routing and focused handoffs, run actual project verification commands, and obtain a separate review of the final diff. Support one bounded correction round with renewed relevant checks/review. Keep the issue, plans, approvals, worker runs, changed revision, CI, review, and whole-task usage linked. Respect target-project Git conventions and human merge control.

**Deliverable:** one small task completes the integrated workflow with all core capabilities active. Exercise failed checks, review rejection, cancellation, and restart to prevent duplicate work, stale evidence, and false success.

### Step 6 — Use one real issue, then verify project portability

Take an approved issue created through the intended ChatGPT/GitHub process and run the full Crew workflow against its project. Record missing capabilities and actual integration gaps, fix those, and check another project's configuration. Preserve each project's rules, templates, and CI rather than imposing KovacsTrader conventions.

**Deliverable:** a real reviewable PR or explicit blocker report, both planning stages, usage/context/routing evidence, and repeatable instructions for another project. Compare operator effort, quality, resource use, and retries to decide the next improvements.

### Step 7 — Improve from measured work

Grow the curated specialist/skill library, tune routing and context, and add parallelism or another backend when useful and proven. Reuse better components as needed. Automatic learned routing and financial hard caps are later capabilities to evaluate; smart rules and usage-aware decisions already belong to the integrated core.

## 8. Progress and acceptance

- [x] Earlier research and supplied research preserved; local Git repository prepared.
- [x] Clarified target: ChatGPT/GitHub intake, two planning stages, smart multi-tool delegation, reusable agents/skills, monitoring, and context handling.
- [x] Single VS Code startup and direct Git commits established as project requirements.
- [ ] Step 1: capability catalogue, exact component choices, and shared library availability.
- [ ] Step 2: coordinator-visible usage/allowance and controlled context handoffs.
- [ ] Step 3: skill/agent selection and capability/usage-aware model/effort routing.
- [ ] Step 4: GitHub issue handoff, technical plan/review, implementation plan/approval.
- [ ] Step 5: implementation, checks, independent review, delivery, and recovery.
- [ ] Step 6: real issue and portability evidence.
- [ ] Step 7: improvements from measured results.

The first integrated version is complete after step 5 only if it includes agent/skill selection, model/effort decisions, context handling, and credit/usage monitoring during planning and implementation. Those requirements cannot be moved out of scope merely to simplify a demo. Step 6 demonstrates real-project usability. Missing backend telemetry/settings must be disclosed and handled explicitly rather than presented as supported.
