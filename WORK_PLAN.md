# Work plan: reusable AI development workflow

Status: research and repository preparation. Last updated: 2026-11-16.

## Goal

Build a minimal, reusable development workflow around Kiro Crew that can work with different repositories and help a person take an issue from planning through implementation, verification, independent review, and a reviewable result. The person approves the technical plan and controls merging. Crew coordinates the work and chooses suitable available agents and tools within the project's rules.

The work is complete when a real, small issue has passed the workflow with verifiable evidence, and another project can configure and repeat it without adopting KovacsTrader-specific infrastructure.

## Working principles

- Use the installed Crew's supported features first. Reuse compatible, reviewed external practices or components where they reduce total work; pin any adopted dependency and respect its license.
- Keep one orchestrator, one active worker at a time, a small context, and at most one correction round for the first pilot. Increase limits only after evidence justifies it.
- Project instructions, permissions, GitHub settings, CI, and existing state conventions take precedence for that project. GitHub is the intended issue/PR record where available; do not require it for local fixture tests.
- Distinguish documented capability, observed local behavior, and verified end-to-end behavior. Record unknowns rather than treating them as success.
- Never treat a skill, prompt, worktree, or an agent's claim as proof that permissions, approvals, tests, or review were enforced.
- Prefer a small amount of maintainable configuration and code. Add a custom guard, router, report, or integration only when a specific gap is demonstrated.

## Target flow

`Issue → repository-based plan → owner approval → implementation → checks → independent review → PR/CI → owner merge decision`

A complex issue may need decomposition or two planning stages. Scope changes require a new decision. The first version runs planning and execution as separately initiated phases unless a native, tested Crew gate provides the same guarantee. Human approval refers to a specific plan, scope, and starting repository state. A separate reviewer examines the actual final diff and evidence. Re-run relevant checks and review when subsequent changes invalidate them.

Routing starts with a small set of verified profiles and an understandable choice based on task and risk. Record requested and actual backend/model/effort when available. Keep Kiro credits, token counts, unknown subscription costs, and estimates in their own units. A shared financial hard cap and self-improving routing are future possibilities, not current capabilities.

## Milestones

### 1. Establish the reusable baseline

- [x] Organize historical research, setup notes, test evidence, and the external research document.
- [x] Define the intended result, this work plan, and contributor guidance; initialize Git.
- [ ] Confirm current Crew, Kiro and Codex versions and available capabilities for the environment used in the pilot. Do not assume historical versions or login state are current.
- [ ] Inspect the target project's instructions, repository state, test commands, and CI before selecting a pilot issue.

### 2. Prove the control boundaries in a disposable Git fixture

- [ ] Exercise a planning run that ends before implementation. Test actual write denial for each backend used, including a deliberate harmless prohibited write and unchanged file hash. Keep plan output in an allowed location.
- [ ] Verify that execution requires an owner decision tied to the specific plan, scope, and base revision; changed inputs must stop for a new decision. The worker must not be able to forge that approval. Prefer an existing Crew mechanism, adding only the smallest necessary guard if it cannot enforce this.
- [ ] Verify real Git worktree or branch behavior, absolute paths, and isolation. A worktree alone is not a security boundary.
- [ ] Exercise failure, cancellation, restart, and stale-input cases. Confirm no duplicate running work and no reuse of invalid prior results.
- [ ] Record each result as passed, failed, blocked, or not tested with evidence. Investigate failures before treating the workflow as ready.

### 3. Assemble the smallest workflow

- [ ] Add a short project-neutral workflow instruction or skill using Crew's supported format, with plan, execution, and review handoffs. Inspect candidate external components and their dependencies and licenses before reuse; do not assume an external skill works unchanged.
- [ ] Define a small, tested profile list using supported Crew spawn parameters. Select a profile automatically from task and risk, record the reason, and stop or report when the requested capability is unavailable.
- [ ] Link the issue, approved plan revision, base commit, run IDs, changed revision, checks, and independent review using existing records where possible. If necessary, add a small deterministic check rather than a new orchestration service.
- [ ] Use target-project test commands; capture exit status and evidence. Review the actual diff in a separate context. Failed tests, unavailable review, or missing evidence must not become a success.
- [ ] Limit retries; stop for an owner decision on scope changes or repeated failures.

### 4. Complete one real pilot

- [ ] Choose one small, low-risk, independently verifiable issue in a Git repository, following its existing governance.
- [ ] Produce a code-grounded plan, obtain owner approval, implement in an isolated branch/worktree, run checks, obtain independent review, and prepare a PR or explicit blocker report.
- [ ] Verify CI and review against the final commit and preserve issue-to-result evidence. The owner decides whether to merge.
- [ ] Record what worked, what failed, operator effort, and resource use for the entire task. Do not claim the system is generally proven from a single pilot.

### 5. Simplify and generalize

- [ ] Remove unnecessary steps found during the pilot and document how another repository supplies its own instructions, verification commands, and permissions.
- [ ] Add a read-only usage summary only if existing Crew views cannot answer the pilot's questions reliably. Mark missing costs unknown and avoid double-counting.
- [ ] Consider more skills, parallelism, backends, model routing, or a saved dynamic workflow only when a measured need and an integration test justify them.

## Success criteria

A new user can understand the target and current state from the README; run the documented setup appropriate to their environment; supply a target repo and issue; review a code-grounded plan; explicitly approve it; and obtain a scoped change with reproducible tests, independent review, traceable run IDs, and a clear PR or blocker report. Approval, permissions, and resume behavior have negative tests. Required CI and the human merge decision remain effective.

## Decisions and open questions

- Crew remains the orchestration runtime. Current delegation evidence is in [historical results](docs/history/RESULTS.md); full issue-to-PR execution is not yet proven.
- Native approval and backend sandbox enforcement, actual worktree behavior, and current provider/model/effort availability must be established in milestone 2.
- Crew's optional subagent model routing is limited and requires configuration; it is not a verified cross-provider optimizer. The pilot should begin with simple profiles.
- The current Workgraph package has changed from the external research description and depends on Linear and other components. Agent-pipeline is Claude-oriented, and ADW routing is within a backend. Treat each as a donor to inspect, not a drop-in dependency.
- The first real pilot issue and target repository have not been selected. KovacsTrader is one possible target, not the definition of the product.
