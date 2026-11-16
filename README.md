# Intelligent Crew Development Workflow

A reusable, TARS-inspired AI development system built by assembling existing Kiro Crew capabilities and compatible skills, agent profiles, routing policies, and monitoring components. It should work across software projects, including KovacsTrader.

**Status:** Studio 2.0.1 is installed locally; 373 payload files verify, and 89 selected upstream tests and three launcher tests passed. The first actual VS Code task failed before gateway startup because the launcher sets a nonexistent embedding model path. The trial is stopped pending agreement on the documented correction; live planning/review/approval remains unrun. See [step 1 results](docs/STEP_1_RESULTS.md).

**Kiro Crew is our chosen foundation.** Reuse native features first, then existing Crew apps/extensions, then compatible external components, and add custom code only for uncovered gaps. AI-DLC Studio is the first extension being trialled; native Spec Builder/Code Review Sage and portable specialist libraries remain alternatives for demonstrated gaps.

## The intended experience

Discuss your ideas in **ChatGPT**, agree the goal, and create the strategic issue through the **GitHub plugin**. Give that issue and the target project to **Kiro Crew**. Crew then coordinates:

`technical plan → your review/approval → detailed implementation plan with proposed code changes → your approval → implementation → tests/CI → independent review → PR/report → your merge decision`

During both planning and implementation, Crew selects suitable agents, skills, Kiro/Codex backends, models, supported reasoning effort, native tools, and context. It knows the tools' verified capabilities and uses available credit/usage information to guide decisions. You should not have to dispatch each worker or choose every model yourself.

The reusable agent/skill library, smart delegation, credit monitoring, and smart context handling are core capabilities. We build them incrementally by importing or adapting proven components and filling demonstrated integration gaps with small amounts of code.

The research guides the initial choices, but we can try alternatives or write a focused component when that is simpler and more reliable. Meaningful changes in approach will be explained. We aim for a usable first integrated version in about one week; the tentative daily goals and early checkpoint are in the work plan.

## Plan and research

- [Crew extension research and reuse plan](docs/research/CREW_EXTENSIONS_2026-11-16.md) — current recommendation: native features, actual Crew apps, adaptable libraries, and remaining custom gaps.
- [Broader system/library comparison](docs/research/COMPLETE_SYSTEMS_2026-11-16.md) — BMAD, AI-DLC, metaswarm, AgentSys, GSD, and others as possible sources for Crew extensions.
- [Next step and copyable execution prompt](docs/NEXT_STEP.md) — bounded AI-DLC Studio integration trial, with stop-on-first-failure instructions.
- [Component decisions](docs/COMPONENT_DECISIONS.md), [capability evidence](docs/CAPABILITIES.md), and [step 1 results](docs/STEP_1_RESULTS.md) — exact pins, observed checks and remaining live evidence.
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

1. Reuse native Crew features and trial the selected ready-made extension's planning/review gates; record exact remaining adaptations.
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

## License

Copyright (C) 2026 Zsombor Kovács.

This repository's original work is licensed under the **GNU Affero General Public License, version 3 only** (`AGPL-3.0-only`). See [LICENSE](LICENSE) for the full terms.

The goal is to keep covered derivatives open source: distribution must comply with the license's corresponding-source requirements, and modified versions used over a network must offer their corresponding source to the users interacting with them. Purely private modifications do not have to be published. Commercial use is permitted under these terms. See the [GNU AGPLv3](https://www.gnu.org/licenses/agpl-3.0.html).

Separately licensed dependencies and any adopted third-party components retain their applicable licenses and attribution. This license does not relicense Kiro Crew, the coding backends, or separate target projects merely because this workflow is used to develop them.
