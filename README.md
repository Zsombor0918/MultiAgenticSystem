# Intelligent Crew Development Workflow

A reusable, TARS-inspired AI development system built by assembling existing Kiro Crew capabilities and compatible skills, agent profiles, routing policies, and monitoring components. It should work across software projects, including KovacsTrader.

**Status:** research and repository preparation. The integrated system is not built yet. Earlier local tests demonstrated Kiro/Codex delegation and partial usage records; they do not prove the complete workflow.

## The intended experience

Discuss your ideas in **ChatGPT**, agree the goal, and create the strategic issue through the **GitHub plugin**. Give that issue and the target project to **Kiro Crew**. Crew then coordinates:

`technical plan → your review/approval → detailed implementation plan with proposed code changes → your approval → implementation → tests/CI → independent review → PR/report → your merge decision`

During both planning and implementation, Crew selects suitable agents, skills, Kiro/Codex backends, models, supported reasoning effort, native tools, and context. It knows the tools' verified capabilities and uses available credit/usage information to guide decisions. You should not have to dispatch each worker or choose every model yourself.

The reusable agent/skill library, smart delegation, credit monitoring, and smart context handling are core capabilities. We build them incrementally by importing or adapting proven components and filling demonstrated integration gaps with small amounts of code.

The research guides the initial choices, but we can try alternatives or write a focused component when that is simpler and more reliable. Meaningful changes in approach will be explained. We aim for a usable first integrated version in about one week; the tentative daily goals and early checkpoint are in the work plan.

## Plan and research

- [System and build plan](WORK_PLAN.md) — the complete workflow, core capabilities, implementation order, deliverables, and progress.
- [Research alignment](docs/RESEARCH_ALIGNMENT.md) — how the existing findings and candidate components support each requirement, including known gaps.
- [Earlier Crew research](docs/history/RESEARCH_KIRO_WORKFLOW.md) and [usage/routing findings](docs/history/RESEARCH_COST_NOTES.md) — dated evidence and limitations.
- [Supplied component research](docs/research/EXTERNAL_RESEARCH.md) — the existing-system shortlist; embedded citation IDs need resolving before adoption.
- [KovacsTrader workflow reference](docs/history/KOVACS_WORKFLOW.md) — project-specific origin of the workflow, rather than universal project rules.
- [Earlier local setup](docs/history/SETUP_AND_DELEGATION.md), [test guide](docs/history/TEST_GUIDE.md), and [results](docs/history/RESULTS.md) — historical setup and delegation evidence.

## One start button

Open this repository in VS Code and choose **Tasks: Run Task → Kiro Crew: Start**. It runs `scripts/start-kirocrew.sh`; follow the terminal output for the dashboard and any necessary first-time setup or login. Stop it with `Ctrl+C` in that terminal.

Every addition must fit behind this normal startup entry point. The future shared library and configuration must be available when selecting other target projects too. The task/launcher exist; the final integrated startup behavior still requires verification.

## How we build it

1. Establish the capability catalogue and exact reusable component choices.
2. Connect existing usage monitoring and controlled context handoffs to Crew.
3. Assemble the reusable agent/skill library and smart model/effort delegation.
4. Connect GitHub issue intake, technical planning/review, and implementation planning/approval.
5. Connect implementation, checks, independent review, and reporting.
6. Use a real issue and confirm the workflow works with another project; improve from measured results.

Develop directly here and commit completed, checked steps. No Git worktree is needed for developing this repository. Each target project retains its own instructions, Git conventions, permissions, and CI.

## Repository contents

| Path | Purpose |
| --- | --- |
| `WORK_PLAN.md` | Agreed system scope and incremental build plan |
| `AGENTS.md` | Instructions for future contributors and AI agents |
| `docs/RESEARCH_ALIGNMENT.md` | Requirements mapped to research and integration choices |
| `docs/history/`, `docs/research/` | Preserved research and prior evidence |
| `scripts/`, `.vscode/` | Existing local launcher, startup task, and artifact check |
| `demo/` | Small fixture from the delegation investigation |

Local `.runtime/` installations, session data, and generated worker artifacts stay outside Git. Version-specific setup details are historical until rechecked for the environment being used.
