# Requirements mapped to existing research

Updated: 2026-11-16. This is a synthesis of the supplied and local research reread for the user's clarified workflow. It does not claim new runtime tests, fresh upstream verification, or completed imports. The current [work plan](../WORK_PLAN.md) is authoritative for scope and build order.

## What each input contributes

- [KovacsTrader workflow](history/KOVACS_WORKFLOW.md): ChatGPT strategic discussion and approved GitHub issue, Crew repository-based planning, approvals, dynamic multi-backend specialists, independent review, context, and resource accountability. Project-specific labels, paths, and rules remain specific to KovacsTrader.
- [Earlier Crew investigation](history/RESEARCH_KIRO_WORKFLOW.md): native building blocks, observed delegation, context inheritance and compaction limitations, permission gaps, focused handoffs, and a minimal integration approach.
- [Cost and routing investigation](history/RESEARCH_COST_NOTES.md): actual Kiro credit/Codex token examples, available account-usage code, supported spawn settings, Jev routing limits, and the difference between measured usage, estimated cost, and remaining allowance.
- [Supplied component research](research/EXTERNAL_RESEARCH.md): existing lifecycle skills, agent libraries, model/effort routing policies, context tooling, and metering implementations to import/adapt rather than rebuild.
- Latest user clarification: explicitly restores the complete ChatGPT/GitHub → technical plan/review → detailed implementation plan → execution workflow. Smart agents/skills, multi-tool/model/effort selection, credit-aware decisions, and context handling are core. Prior advice to combine planning or postpone usage does not override this.

## Requirement coverage

| Requirement | Research finding | Planned reuse/integration | Build step |
| --- | --- | --- | --- |
| Ideas → strategic issue | Original workflow separates ChatGPT strategy from repository-specific Crew planning | Existing ChatGPT GitHub plugin and target issue templates; issue URL handoff | 4 |
| Technical plan, review, then implementation plan with concrete changes | Original workflow and agent-pipeline/Superpowers/GSD provide planning/checking patterns | Adapt selected planning and plan-checking skills to Crew, with owner approvals | 3–4 |
| Robust reusable skill/agent system | Crew discovery/loading and external engineering libraries are identified | Curated, pinned existing skills/profiles, with verified discovery, selection, and actual application | 1, 3 |
| Know which AI tools can do what | Local tests show Kiro/Codex behavior differs, including native subagent and effort support | Evidence-backed capability catalogue; refresh on relevant version/account changes | 1 |
| Smart delegation and model/effort choice during planning and implementation | Crew spawn supports explicit choices; Workgraph/ADW supply decision policies | Native mechanisms where sufficient; adapt policy only for uncovered worker selection | 3, used in 4–5 |
| Monitor credits/resources and use them in decisions | Crew logs have Kiro credits and partial Codex tokens; native Kiro account-usage code exists | Expose run usage and allowance to coordinator; native views or minimal normalization/report glue | 2, used in 3–6 |
| Smart context | Crew inheritance/lazy loading/checkpoints; Repomix/Aider candidates; local cache/context observations | Role-specific handoffs, measured context, controlled inheritance and recovery; existing repo mapping if needed | 2, used in 3–6 |
| Reliable execution and evidence | Native coding tools, shell/CI, independent review, bounded retry patterns | Adapt implementation/review skills and connect actual final revision to checks, review, and usage | 5–6 |
| Minimal work, portability, one start button | Existing runtime and VS Code launcher already present | Configure/import/adapt before writing code; same startup path across project selection; direct Git commits here | Every step |

## Component integration shortlist

These are candidates from the research, not a request to install all of them. Step 1 selects the smallest compatible set and records exact source/revision, files, license, dependencies, and remaining gaps. Step 3 integrates that set. An unresolved source or version stays a candidate rather than becoming an assumed dependency.

| Area | Candidate/foundation | Concrete reuse target | Known adaptation or verification need |
| --- | --- | --- | --- |
| Runtime | Kiro Crew | Dashboard, project context, spawn/completion, skill discovery, native permissions and records | Decide whether Task Runner or a saved workflow actually helps the required gates; verify real behavior |
| Planning and plan audit | [agent-pipeline](https://github.com/roycehoe/agent-pipeline), [Superpowers](https://github.com/obra/superpowers), GSD | Planning procedures, code grounding, plan checking, handoffs | Agent-pipeline has host-specific tools and interdependent skills; final verification must follow any cleanup changes |
| Task decomposition | [Workgraph](https://github.com/shiro-el/workgraph-skills), Lousy Agents Skills | Acceptance-based issue slicing, dependencies, bounded assignments | Workgraph's current source differs from the attachment's five-skill description and uses Linear/host-specific dependencies; choose exact reusable files/version |
| Agent profiles and specialist skills | Crew profiles; agent-crew, Sentry, Matt Pocock and other focused libraries in the supplied research | Existing research/planning/debugging/testing/review/documentation procedures | Map relevant profiles to Crew-supported formats; inspect included scripts, dependencies, and permissions; prove actual selection/use |
| Routing | Crew Jev plus [ADW](https://github.com/pdoronila/adw) and Workgraph policies | Difficulty/risk → model/effort; usage-pressure and failure response | ADW's inspected router works within a backend; its usage probes do not establish Kiro support. Cross-tool routing needs capability-aware adaptation |
| Context | Crew native controls; Repomix/Aider repo-map candidates | Focused handoffs, lazy relevant context, checkpoint/resume; optional repo mapping | Verify actual inherited content and backend compaction; adopt an external map only if native tools leave a gap |
| Metering | Crew ledger/account views; agentic-coding-harness candidate | Per-run resource data, credit/token distinctions, parser/data-model reuse | Inspect exact candidate source and compatible telemetry; preserve Crew runtime and distinguish partial data from zero usage |
| Skill intake | Reviewed source and licensed revisions; Sentry/Cisco scanner candidates | Existing skill inspection/scanning procedures | A scanner is useful evidence, not proof of compatibility or complete safety; add only the needed intake tooling |

Larger lifecycle suites, external observability platforms, and additional backends remain available options from the research. Installing them all is not required to preserve the user's intended system.

## Findings the integration must respect

1. **Usage exists already.** Earlier logs record Kiro credits and Codex input/output/cache tokens. The local research also identified a Kiro account-usage view. These are foundations for monitoring, not reasons to postpone it. Full issue attribution and fresh allowance access still need integration checks.
2. **Account allowance differs from task consumption.** Other sessions can affect account usage. Missing subscription cost data is unknown. Monitoring must show source, units, freshness, coverage, and phase/run identity, and feed routing decisions.
3. **Requested effort can fail to apply.** The historical KAS `low`/`auto` run did not apply the requested effort. Keep requested and effective values distinct and do not assume one backend's controls work on another.
4. **Crew's router has narrower coverage than the target.** The local investigation found optional routing of unpinned subagent starts as well as normal chat routing. Neither that nor the attachment's broader description proves automatic multi-backend worker/model/effort routing for our workflow.
5. **Role configuration is constrained.** The inspected `role_models`/`role_efforts` support `background` and `subagent`, not arbitrary `planner`/`reviewer` keys. Use supported profiles and explicit spawn fields.
6. **Context features are backend-specific.** KAS compaction does not obey Crew's generic autocompact control in the same way. Large cache-read counts are an investigation signal, not proof of removable waste or an exact subscription charge.
7. **Monitoring is not a proven hard financial cap.** The inspected workflow budget did not establish automatic usage charging or a shared cross-provider monetary limit. Start with truthful metering, thresholds, bounded runs, and informed phase decisions.
8. **Approval and tool permission are distinct.** A reviewed plan is not a grant for every tool call. The historical Codex `tools: []` gap means a prompt/allowlist alone cannot demonstrate read-only planning. Validate the actual execution route with designated harmless files.

## Adoption record to fill during implementation

For each adopted component, record source URL, pinned revision, license/attribution, exact files used, dependencies, changes made, Crew loading/configuration path, capability tested, result/evidence, and unresolved limitations. Reuse this small record instead of repeating broad research or inventing a new package-management system.
