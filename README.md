# Crew Development Workflow

A reusable, Kiro Crew-based workflow for developing software with AI across multiple projects. The goal is to turn a well-defined issue into a reviewed, tested change while keeping the human in control of the important decisions.

**Status: preparation and research. The workflow described below is the target, not a completed implementation.** Kiro and Codex delegation have been demonstrated locally; the complete workflow and its security boundaries have not yet been verified.

## Intended result

1. Give Crew an issue and a target repository.
2. Crew reads the relevant code and prepares a practical implementation plan.
3. A person reviews and approves that plan.
4. Crew selects an appropriate available worker, implements the approved scope, and runs the relevant checks.
5. A separate reviewer examines the actual changes and test evidence. The result is a pull request or a report with remaining blockers.
6. The repository's CI and human merge decision complete the process.

The aim is to use Crew's existing capabilities and proven external practices, with as little custom code and operational overhead as the evidence permits. The first version supports a single bounded task and one active worker at a time; it should be adaptable to different projects without imposing KovacsTrader-specific rules on them.

## Start here

- [Work plan](WORK_PLAN.md) — scope, decisions, milestones, and acceptance criteria. This is the guide for future work in this repository.
- [Historical research](docs/history/RESEARCH_KIRO_WORKFLOW.md) and [cost findings](docs/history/RESEARCH_COST_NOTES.md) — what was investigated and what remains uncertain.
- [External research](docs/research/EXTERNAL_RESEARCH.md) — supplied research, preserved as a historical input; its embedded citation identifiers are not portable links and its package descriptions require verification.
- [KovacsTrader workflow](docs/history/KOVACS_WORKFLOW.md) — a project-specific reference, not a universal contract.
- [Previous local setup](docs/history/SETUP_AND_DELEGATION.md), [test guide](docs/history/TEST_GUIDE.md), and [results](docs/history/RESULTS.md) — historical environment and delegation evidence, not a current installation guarantee.

## Start Kiro Crew

Open this repository in VS Code, then choose **Tasks: Run Task → Kiro Crew: Start** from the Command Palette. This is the single normal startup entry point for the workflow. The task runs `scripts/start-kirocrew.sh`; follow its terminal output to open the dashboard or complete any necessary setup or login. Stop it with `Ctrl+C` in that terminal.

Future workflow changes must remain compatible with this task and include any necessary supporting startup in the same entry point. First-time setup and authentication may still require user action. The existing task and launcher are in place; their behavior with the future workflow still needs end-to-end verification.

## Repository layout

```text
WORK_PLAN.md        Product direction and staged implementation
AGENTS.md           Instructions for contributors and AI agents
scripts/            Existing local Crew launcher and artifact check
demo/              Small fixture from the delegation investigation
docs/history/      Previous research, setup, results, and project reference
docs/research/     Research supplied for this project
```

The local `.runtime/` installation and generated agent data are ignored by Git. They are specific to this machine and are not needed to read or contribute to the project. Existing scripts are experimental local tools; their documented Kiro Crew 0.12.2 setup must be checked against the current environment before use.

## Working on the project

Read [WORK_PLAN.md](WORK_PLAN.md), select the next unfinished milestone, and verify each capability before relying on it. Develop in this repository and use ordinary Git commits to record completed steps. Test approval, permissions, and restart behavior using designated harmless test files here. After those controls are demonstrated, exercise the workflow with one real, low-risk issue in a target repository.

This repository is the development home for the reusable workflow. Each target project keeps its own instructions, access rules, issue tracking, and CI; the workflow must respect them.
