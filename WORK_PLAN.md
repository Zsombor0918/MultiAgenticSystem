# System and implementation plan: Crew Development Workflow

Status: repository prepared; system assembly has not started. Updated: 2026-11-16.

## 1. The system we are building

A reusable AI development assistant, coordinated by Kiro Crew, that works on whichever software project the user selects. The user explains a feature or bug, or supplies a GitHub issue. Crew investigates the actual repository, plans the work, waits for approval, selects suitable workers and skills, implements the change, runs checks, arranges an independent review, and reports the result.

The intended experience is a small development team behind the existing Crew dashboard. The user handles goals, important choices, plan approval, and merging. Crew handles routine technical coordination and selection of agents, backend, model, supported reasoning effort, skills, tools, and relevant context.

KovacsTrader is one potential target project. Its particular rules do not become requirements for other projects.

## 2. How the user will use it

1. Open this repository in VS Code and run **Kiro Crew: Start**.
2. In the Crew dashboard, select the target project and give it a request: for example, “Plan this issue” or “Investigate and fix this bug.” An issue URL is optional for local work.
3. Crew inspects the project and presents a plan: intended changes, acceptance criteria, checks, risks, and proposed work assignments. If the task is too large, it proposes smaller tasks. A second planning stage is reserved for work that needs it.
4. The user approves or revises that specific plan. Crew then runs implementation and verification within the approved scope.
5. Crew returns the change, test results, independent review, run information, available resource usage, and a PR or a clear explanation of what is still blocked. The user decides whether to merge.

These phrases describe the intended interaction, not already implemented slash commands. Routine use must not require the user to select a model or coordinate every worker manually.

## 3. What the system consists of

| Piece | Implementation choice | What we add here |
| --- | --- | --- |
| Startup and dashboard | Existing VS Code task, launcher, and Crew dashboard | Keep configuration and any required supporting startup behind the same task |
| Coordinator | Crew's existing chat, delegation, and run records | One reusable development workflow skill with focused planning, implementation, and review instructions |
| Project context | Crew's selected project, its instructions, and relevant repository files | A short handoff containing the request, project root, scope, acceptance criteria, and approved plan |
| Workers and specialists | Native Kiro/Codex workers through supported Crew delegation | A small catalogue of verified execution profiles and approved skills, expanded only as tasks require |
| Worker selection | Coordinator chooses from the catalogue and passes supported spawn parameters | A clear policy for task type, risk, complexity, capability, and available resources |
| Verification | The target project's shell commands and CI | Capture actual command exit status and connect evidence to the changed revision |
| Independent review | A separate Crew worker/context | Give the reviewer the requirements, final diff, and test evidence; return actionable findings |
| Progress and recovery | Existing Crew run records and project/GitHub records | Link request, plan version, approval, runs, changed revision, checks, and review; add a small local record only if needed |
| Usage report | Crew's existing usage records | Summarize the whole task; add a read-only reporter only if native views are insufficient |

The initial coordinator works with one active worker at a time. Planning, implementation, and review are responsibilities; they do not require three permanently running agents. Tests run through shell/CI, without an extra model call merely to execute a command.

The first workflow can be a short skill with reference procedures rather than a custom runtime. Use a saved Crew dynamic workflow only if it makes the demonstrated process easier to repeat. Check its actual supported approval and restart behavior before adopting it.

## 4. The execution procedure

| Phase | Crew does | Result and next action |
| --- | --- | --- |
| Intake | Reads the request, project instructions, repository state, and acceptance criteria | A bounded task; missing decisions are raised with the user |
| Plan | Inspects relevant code, chooses an approach, names checks and required capabilities | A versioned technical plan; stops for owner approval |
| Approve | Associates the owner's decision with the plan, scope, and starting code state | Execution may start for that approved work; material changes require a new decision |
| Implement | Selects an allowed profile and skills, starts a worker, and supplies a focused handoff | Scoped code changes and a worker result |
| Check | Runs relevant project checks against the actual changes | Command results; failure can trigger one correction round |
| Review | Starts a separate reviewer to examine the diff, requirements, and check evidence | Findings or a passing review; fixes require relevant checks and review again |
| Deliver | Checks evidence, prepares the permitted PR/report, and summarizes usage and open items | Reviewable result; human merge decision |

For the first version, the planning run ends and the owner initiates execution of the approved plan unless a tested native Crew approval gate can enforce that boundary. This still uses the same dashboard and startup task. Scope expansion, unavailable permissions, repeated failure, or exhausted run limits stop the task for a decision. Failed or missing verification/review must not become “done.”

For recovery, use existing run IDs and checkpoint behavior. Before resuming, confirm the project, approved plan, current code state, and whether work is already running. Never replay cached results that the changed inputs invalidate.

## 5. Selection of agents, skills, models, and effort

Start with a few profiles whose backend, actual model, supported effort, tools, and permission behavior have been checked locally. Planner, implementer, and reviewer are workflow roles, not invented Crew configuration keys. Use supported per-run parameters to apply the chosen profile.

- Small, clear tasks use a capable economical profile that has passed the relevant checks.
- Ambiguous or risky work uses a stronger suitable profile; explain the choice in the run report.
- The reviewer always has a separate context; another provider is useful when justified but is not required for independence.
- Confirm requested versus applied model/effort where the backend exposes it. Unsupported settings are reported rather than assumed to have worked.
- Diagnose environment and permission failures before escalating the model. Keep at most one correction round in the first pilot. Resource pressure does not silently lower the capability required for risky work.

Keep the initial approved skill set small: planning, scoped implementation, and independent review. Use Crew's existing discovery/loading mechanism; verify that the shared workflow is actually available when a different target project is selected. Add specialist skills in response to real work rather than importing an entire catalogue at once.

## 6. Existing concepts we will reuse

Research is already available in [the local findings](docs/history/RESEARCH_KIRO_WORKFLOW.md), [cost notes](docs/history/RESEARCH_COST_NOTES.md), and [the supplied research](docs/research/EXTERNAL_RESEARCH.md). The next work is assembly and focused compatibility checks.

| Source | Practice to reuse | Integration decision |
| --- | --- | --- |
| Kiro Crew | Dashboard, project context, skill loading, spawn/completion, permissions, and existing logs | Primary runtime; use native features before writing replacements |
| Workgraph | Small acceptance-based tasks, bounded handoffs, and review tied to a specific revision | Adapt selected procedures; its current Linear-based package is not selected as a runtime dependency |
| agent-pipeline | Code-grounded planning, plan checking, and bounded correction | Adapt useful instructions; final checks/review must follow the last code modification |
| ADW | Explicit approval, fresh review context, and understandable escalation rules | Start with the rules; reuse router code only if a concrete need and compatible data justify it |

Before adopting external files or code, inspect their dependencies, license, current version, and actual behavior in Crew. Preserve attribution and pin the adopted revision. A small adapted workflow is acceptable; a second orchestrator is unnecessary.

## 7. Steps to build it

Work directly in this repository. Complete a small step, check its result, and commit it so progress can be inspected or returned to. No Git worktree is needed for developing this repository. Follow each target project's Git conventions when operating there.

### Step 1 — Connect the reusable workflow to the existing start task

Confirm the installed Crew/Kiro/Codex versions and supported configuration. Add the initial development workflow skill and arrange for Crew to load it through a supported mechanism when the task starts, including when another target project is selected. Keep installation/update behavior explicit and repeatable; ordinary starts should not reinstall dependencies.

**Deliverable:** one startup path and a workflow that Crew can find and read. Verify the existing task launches it, stops cleanly, and restarts. Use the current dashboard rather than building another UI.

### Step 2 — Make request → project investigation → plan → approval work

Add the intake and planning procedure, a short plan format, and the execution handoff. Use a small local task with designated harmless test files. Establish the owner's approval boundary using Crew's existing facilities; only add a minimal guard if native behavior cannot provide it.

**Deliverable:** a real code-based plan produced in Crew, with implementation stopped until approved. Check actual write denial during planning and refusal to execute an unapproved or materially changed plan. Keep permitted plan output separate from protected project code.

### Step 3 — Connect approved plans to selected workers

Add the initial verified Kiro/Codex profile catalogue and selection rules. Delegate approved work through Crew, pass the correct absolute project path and focused context, and collect completion IDs and actual changes. Keep one active worker and prevent repeated starts from duplicating it.

**Deliverable:** Crew chooses and runs a suitable worker for an approved small task; the user does not manually coordinate it. Confirm native tools and permissions work through the actual worker path. Report unavailable capabilities honestly.

### Step 4 — Connect checks, independent review, and delivery

Run the project's actual verification commands after implementation. Add the independent review procedure and one bounded correction round. Assemble a short report linking plan, approval, worker runs, changed revision, test output, review, and available resource usage. Use native records first. Prepare a PR when permitted by the target project's process; preserve human merge control.

**Deliverable:** a complete small local task passes through plan, approval, implementation, tests, review, and a report. Exercise a failing check, review rejection, cancellation, and restart as part of this integration, so incomplete work cannot be reported as success.

### Step 5 — Use it on one real issue, then another project

Select a small real issue and follow the target project's instructions and CI. Run the whole workflow, correct only demonstrated gaps, and record the result. Then configure another repository and confirm the workflow does not depend on KovacsTrader-specific paths, labels, or state files.

**Deliverable:** a real PR or documented blocker report, plus short instructions for applying the same workflow to another project. Evidence and CI must refer to the final changed revision. Report the operator effort and known limitations.

### Step 6 — Improve only the parts that need it

Use completed runs to decide whether more skills, specialist profiles, parallelism, a saved dynamic workflow, a usage reporter, or more advanced routing would save work. Compare the whole task, including planning, review, and retries. Keep unknown subscription costs unknown, and Kiro credits and token metrics in their own units.

**Deliverable:** measured improvements to the working core. Automatic learning and cross-provider financial hard limits remain optional future work requiring their own evidence.

## 8. Progress and completion

- [x] Research collected and organized; Git initialized; README and contributor instructions present.
- [x] Single VS Code startup task and direct Git development recorded as requirements.
- [ ] Step 1: reusable workflow available through the existing start task.
- [ ] Step 2: project-based planning and actual approval boundary.
- [ ] Step 3: automatic selection and execution of verified workers.
- [ ] Step 4: checks, independent review, bounded correction, and delivery report.
- [ ] Step 5: real issue completed and workflow exercised on another project.
- [ ] Step 6: improvements selected from actual results.

The first useful version is complete after step 4; real-project usability is demonstrated in step 5. Every step must preserve **VS Code → Kiro Crew: Start** as the single normal startup path. First-time setup, authentication, and genuine approval decisions can require user action. Normal use must not require extra startup tasks or commands.
