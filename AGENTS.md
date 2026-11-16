# Contributor instructions

Read `README.md`, `WORK_PLAN.md`, and `docs/RESEARCH_ALIGNMENT.md` before working here. They define the user's intended system, the research behind it, and the build order. Follow the current user's clarified requirements over older research recommendations; do not silently simplify away core capabilities. Update progress only with evidence.

The normal workflow starts with ideas discussed in ChatGPT and an approved strategic GitHub issue created through the GitHub plugin. Crew then produces a technical plan for review/approval, a detailed implementation plan with proposed code changes for approval, and coordinated implementation, checks, independent review, and delivery. Smart selection of backend/agent/model/effort/skills/tools, tool capability knowledge, credit/usage-aware decisions, and smart context handling are core requirements in planning and execution. Monitoring is not merely a later optional report.

Minimize custom work by using Crew's existing capabilities, importing/adapting reviewed existing components, and adding only demonstrated missing glue. Do not replace the user's intended agent/skill system with a generic fixed pipeline. Keep the product reusable across projects and preserve each target's instructions, permissions, Git conventions, and CI. TARS is the architectural inspiration; do not assume an available TARS package.

Keep **Kiro Crew: Start** in `.vscode/tasks.json` as the single normal startup entry point. Integrate shared library/configuration and any required supporting startup with its launcher; normal operation must not require additional startup tasks or commands. Preserve necessary first-time setup, login, and approvals, and verify startup-related changes.

Develop directly in this repository with ordinary Git commits for completed, checked steps. Do not create a Git worktree for work here. Distinguish proposals, documented capability, and observed behavior. Preserve historical research and attribution. Do not commit credentials, runtime data, raw agent transcripts, or generated test artifacts.
