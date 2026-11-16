# Contributor instructions

Read `README.md` and `WORK_PLAN.md` before working in this repository. The work plan defines the system, its execution procedure, and the concrete build steps. Follow those steps and their deliverables; update their status only when supported by evidence. Keep the product reusable across target repositories and preserve each target's own instructions, permissions, and CI.

Keep **Kiro Crew: Start** in `.vscode/tasks.json` as the single normal startup entry point. Integrate any required startup configuration or supporting processes with its launcher; do not require the user to run additional startup commands or tasks for normal operation. Preserve necessary first-time setup, login, and approval prompts, and verify the task after startup-related changes.

Develop this project directly in this repository with ordinary Git commits for completed steps. Do not create a Git worktree for work on this repository. Respect the target project's own Git conventions when testing the workflow elsewhere.

Prefer existing Kiro Crew capabilities and compatible, reviewed components. Keep additions small, and distinguish observed results from proposals. Preserve historical research as context rather than treating its dated claims as current requirements. Do not commit credentials, runtime data, agent transcripts, or generated test artifacts.
