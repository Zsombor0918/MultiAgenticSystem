# Complete systems for a TARS-like Kiro Crew workflow

Research date: 2026-11-16. Status: **source-backed recommendation; no candidate installed or exercised through Crew yet**.

**Crew is the chosen foundation.** The current assembly recommendation is [Crew extension research](CREW_EXTENSIONS_2026-11-16.md), covering actual Crew apps, native capability cards/spec hooks and routing. This broader survey supplies reusable libraries and adapters; it does not reopen runtime choice.

## Decision in brief

We found substantial existing systems worth reusing inside Crew. **BMAD Method v6.12.4** is a strong portable methodology/library; **AI-DLC v2.11.4** provides engineered lifecycle machinery; **metaswarm v0.16.0** is close to the TARS-style specialist-team architecture. The focused follow-up found an actual **AI-DLC Studio Crew app**, so that extension now precedes a BMAD port in the trial order. Crew retains its existing runtime, dispatch, context and accounting services.

BMAD is a strong portable library; the existing AI-DLC Studio Crew extension takes priority for a bounded fit check in [the current trial plan](../NEXT_STEP.md). No external suite has been declared working locally.

The crucial distinction is between a complete development **methodology/agent library**, a complete standalone **runtime**, and a system already integrated with **Crew's actual ACP execution path**. We found the first two. We did not establish the third for any complete external system during this research.

The public [evosoft TARS description](https://www.evosoft.hu/blog/ai-in-education-v4-universities-and-evosoft-meet-in-budapest) supplies the specialist-team inspiration. This search did not establish a public TARS installation we can adopt. The practical objective is its useful behavior, using inspectable, licensed components.

## Scope and evidence

Screened **33 version/candidate entries across 32 distinct repositories**, including unavailable references. Read primary READMEs, release metadata, selected directory trees, and relevant source/configuration files for the main contenders; inspected the installed Crew 0.12.2 implementation. Depth varies by candidate and is recorded in the [source inventory](COMPLETE_SYSTEMS_SOURCES_2026-11-16.json). This is a broad practical search, not an exhaustive census of every system.

No installers, dependency builds, agent benchmarks, gateway sessions, paid model calls, or upstream test suites ran. No source inspected here was adopted into the runtime. Passing a repository's own tests or its production claims would not by itself demonstrate this user's workflow; none of those claims is treated as a local PASS.

The user's required flow is preserved:

`ChatGPT ideas → approved GitHub issue → Crew actionable plan/review → user approval → smart implementation → tests/CI → independent review → PR/report → human merge`

**Later scope clarification (2026-11-16):** For complex tasks, an additional technical-plan approval followed by a detailed implementation plan and approval is an option, not a universal requirement. The original comparison of two-plan-capable candidate systems is retained as research background.

Capabilities required during planning and execution: reusable specialist agents and skills; actual tool-capability knowledge; backend/model/effort selection; focused context and recovery; credit/usage monitoring that informs choices. Normal startup stays **VS Code → Kiro Crew: Start**. Development here uses ordinary Git commits, without a worktree requirement. A donor's worktree default is an adaptation point, not a reason to impose it on this repository.

## 1. Shortlist against the actual requirements

**Present** means inspected source/procedures support the capability on their documented host. It does not mean verified under Crew. **Adapt** means a specific mapping or missing behavior is needed. **Unproven** means the evidence inspected does not establish the requirement.

| System / line inspected | Lifecycle and specialists | Kiro/Codex fit | Model/effort intelligence | Context/recovery | Kiro credit-aware decisions | Practical role here |
| --- | --- | --- | --- | --- | --- | --- |
| BMAD **6.12.4 stable** | Present: architecture/spec/build/review agents and procedures | Installer explicitly targets Kiro skills and Codex skills; Crew dispatch still needs adaptation | Adapt: host/profile policy, not a demonstrated cross-tool optimizer | Present: JIT step files, rendered snapshots and compact specs | Adapt: use Crew data | **Portable library for actual gaps / alternative to Studio** |
| AWS AI-DLC **2.11.4** | Present: shared stage engine, specialist fleet, approval guard | Native Kiro V3 and Codex projections; ACP hook contract needs proof under Crew | Partial: tier policy exists, but Kiro defaults inherit the session model | Present: state, resume, persistent artifacts, per-stage behavior | Missing in its Kiro producer; use Crew | **Best engineered lifecycle alternative**, conditional on hook bridge |
| metaswarm **0.16.0** | Present: issue/research/planning gates/execution/review/PR lifecycle | Codex integration exists; no inspected native Kiro adapter | Role model maps and failure escalation; external Codex/Gemini adapters | Present: knowledge and BEADS-backed recovery | Not demonstrated; USD estimate is not Kiro metering | **Closest TARS-like team**, larger port/default-tuning cost |
| AgentSys **5.14.0 legacy** | Documented full `next-task` pipeline with specialist profiles | Has Kiro-converted profiles; native gates differ by host | Documented role model allocation; Kiro mappings need checking | Flow/task records and repo-intel | Not established | Historically close, but required plugin source unavailable to this connection |
| AgentSys **6.1.1 / current** | Marketplace plus Foreman queue; useful skills | Kiro/Codex install surfaces exist | Not evidence of complete Crew-wide routing | State is workflow-specific | Not established | Selected tools/library, not the preferred lifecycle base |
| GSD Core **next** | Full discuss/plan/execute/verify/ship process | Codex supported; first-party Kiro integration explicitly out of scope | Model profiles and bounded failure-tier escalation | Strong focus on fresh-context work and recovery | Not established | Context/routing reference or Codex-only alternative |
| Superpowers | Complete design/approval/implementation/review methodology | Codex supported; direct Crew mapping untested | Model/effort and resource policy need Crew | Focused task contexts and separate review | Needs Crew | Lean fallback if BMAD adaptation is excessive |
| Kiro Team **2.1.1 line** | Lead/builder/validator/documenter implementation team | Native Kiro; cross-Codex path not established | Fixed source model default, not adaptive selection | Plan/TODO ownership | Not established | Small native role/delegation reference |

The comparison does not justify installing all eight. Pick one primary lifecycle/library, retain Crew's working services, and add a supplementary component only for a concrete gap.

## 2. BMAD: a strong portable library, and the exact missing pieces

The stable [6.12.4 package](https://github.com/bmad-code-org/BMAD-METHOD/blob/v6.12.4/package.json) and [release](https://github.com/bmad-code-org/BMAD-METHOD/releases/tag/v6.12.4) are distinct from the V7 preview described on main. Use the stable pin for the first attempt. Its [platform configuration](https://github.com/bmad-code-org/BMAD-METHOD/blob/v6.12.4/tools/installer/ide/platform-codes.yaml) explicitly includes Kiro `.kiro/skills` and Codex `.agents/skills`. This is concrete installation support, not just a generic claim of portability.

Reuse a complete, necessary module and its renderer/configuration dependencies. The [build entry point](https://github.com/bmad-code-org/BMAD-METHOD/blob/v6.12.4/src/bmm-skills/ship/bmad-build/SKILL.md) requires `_bmad/scripts/render_skill.py` via `uv` and halts on rendering failure. Copying one `SKILL.md` into Crew would lose that contract. The [renderer](https://github.com/bmad-code-org/BMAD-METHOD/blob/v6.12.4/src/scripts/render_skill.py) creates the snapshot the workflow follows. Preserve the upstream tree and MIT notice; keep local changes explicit.

BMAD gives us a substantial existing specialist and workflow library. For the user's sequence, trial its architecture/specification work followed by the build planning step. The [architecture skill](https://github.com/bmad-code-org/BMAD-METHOD/blob/v6.12.4/src/bmm-skills/plan/bmad-architecture/SKILL.md) already has a reviewer gate. Its build planning writes a code map, tasks, questions, and acceptance-related content. These are the foundations for the two distinct user-reviewed artifacts.

There are four important adaptations, supported by inspected code:

1. **Force both user gates.** [Build planning](https://github.com/bmad-code-org/BMAD-METHOD/blob/v6.12.4/src/bmm-skills/ship/bmad-build/step-02-plan.md) can route small work directly into a oneshot implementation. That default conflicts with this user's two-stage approval workflow. Select/customize a plan-only path, or make a small versioned patch if customization cannot express it. A behavioral instruction alone does not prove write denial.
2. **Map dispatch and waiting to Crew.** [Implementation](https://github.com/bmad-code-org/BMAD-METHOD/blob/v6.12.4/src/bmm-skills/ship/bmad-build/step-03-implement.md) uses subagents when available and otherwise works inline. [Review](https://github.com/bmad-code-org/BMAD-METHOD/blob/v6.12.4/src/bmm-skills/ship/bmad-build/step-04-review.md) expects synchronous subagent collection. Crew uses spawn/completion semantics; map them deliberately. Do not allow unavailable delegation to turn an independent reviewer into implementer self-review.
3. **Add the actual worker policy.** BMAD persona skills are not automatically registered Crew agents. A Crew worker can be assigned an exact persona/skill with scoped instructions, or a proven native profile can carry it. Do not invent `agent="bmad-architect"` and assume Crew discovers it. Backend/model/effort choices belong to verified Crew spawn parameters, with a quality floor for review.
4. **Use Crew monitoring and context controls.** BMAD's compact artifacts are useful, but they do not supply our Kiro credit producer or prove which context Crew inherited. Keep per-phase/run metering and measured handoffs in the integrated path.

These are specific integration tasks, not a reason to rewrite BMAD. Their effort remains unmeasured. If a native mapping fails, stop the trial and decide whether AI-DLC or Superpowers offers a cheaper next experiment.

## 3. AI-DLC: the strongest engineered alternative, with a real host boundary

AWS's [AI-DLC](https://github.com/awslabs/aidlc-workflows) is a substantial harness-neutral lifecycle implementation, not merely a set of prompting ideas. It has authored specialist agents, an engine/state machine, stage protocols, persisted artifacts, hook adapters, and a [code-plan approval guard](https://github.com/awslabs/aidlc-workflows/blob/main/core/hooks/aidlc-plan-approval-guard.ts). Its [Kiro guide](https://github.com/awslabs/aidlc-workflows/blob/main/docs/guide/harnesses/kiro.md) and [Codex guide](https://github.com/awslabs/aidlc-workflows/blob/main/docs/guide/harnesses/codex-cli.md) describe real native distributions. The checked stable release is [v2.11.4](https://github.com/awslabs/aidlc-workflows/releases/tag/v2.11.4); main has subsequent changes, so do not conflate them.

It is a strong option if we want its deterministic lifecycle to own stage state while Crew owns sessions and cross-backend dispatch. A lifecycle engine inside Crew is not inherently a bad architecture: the boundary must specify one owner for stage advancement, approvals, dispatch, and recovery. Avoid two competing autonomous dispatch loops.

Three findings prevent calling it a drop-in solution:

- **Metering is not cross-harness.** The released [usage extractor](https://github.com/awslabs/aidlc-workflows/blob/v2.11.4/core/tools/aidlc-usage.ts) says only the Claude harness wires a producer. Kiro/Codex/opencode consumers have no ledger data from this module. Crew's own Kiro credits and Codex metrics are still needed.
- **Tier names do not mean automatic Kiro model routing.** The released [tier implementation](https://github.com/awslabs/aidlc-workflows/blob/v2.11.4/core/tools/aidlc-tiers.ts) omits default Kiro model pins. Kiro agents inherit session settings; Codex also inherits its model with a medium cap for certain reviewers. Explicit per-install model policy exists, but does not establish the user's desired capability/usage-aware Crew decisions.
- **Use the existing hook integration first.** AI-DLC's Kiro guide requires a native ACP hook advertisement that Crew deliberately omits to avoid duplicate execution; see [handshake source](https://github.com/kirodotdev/KiroCrew/blob/v0.12.2/src/kiro_crew/acp/types.py). Follow-up inspection found Crew's existing [spec-hook runner](https://github.com/kirodotdev/KiroCrew/blob/v0.12.2/src/kiro_crew/agent_sdk/spec_hooks.py), and AI-DLC Studio supplies Crew-specific host-turn patches. Thus the missing advertisement alone is not a reason to reject this route or build a hook bridge. Check the actual extension's hook ownership, payloads, human approval and denied writes; do not flip flags or patch Crew speculatively.

AI-DLC may ultimately require less custom enforcement than a procedural library, but only a small live gate test can settle that. Its MIT-0 license was checked in the [source](https://github.com/awslabs/aidlc-workflows/blob/main/LICENSE).

## 4. Metaswarm: closest to the envisioned AI team

[Metaswarm](https://github.com/dsifry/metaswarm) already combines specialist roles, research/planning gates, work decomposition, implement/validate/adversarial-review loops, knowledge capture, and PR lifecycle procedures. Its [Codex documentation](https://github.com/dsifry/metaswarm/blob/main/docs/README.codex.md) and [external-tools skill](https://github.com/dsifry/metaswarm/blob/main/skills/external-tools/SKILL.md) show cross-model work rather than a purely single-agent method. The checked release is 0.16.0, with MIT reported by repository metadata.

The [models configuration](https://github.com/dsifry/metaswarm/blob/main/templates/models.yaml) assigns models per role and includes coder escalation after failures. The [external-tools configuration](https://github.com/dsifry/metaswarm/blob/main/skills/setup/templates/external-tools.yaml) selects adapters and budget settings. This is closer to the desired smart team than a generic planning template.

The adaptation cost is higher: its [main procedure](https://github.com/dsifry/metaswarm/blob/main/skills/start/SKILL.md) assumes BEADS state, native team/context behavior, substantial parallel review, and a PR-shepherd lifecycle. Its external adapters cover Codex/Gemini in the inspected files; Kiro through Crew remains an adapter task. Its [cost estimator](https://github.com/dsifry/metaswarm/blob/main/bin/estimate-cost.sh) calculates selected model USD estimates, not Kiro credits or verified subscription charges. Tune fan-out, retries, and merge behavior to the user's rules. Do not import all the default review rounds merely to obtain the specialist roster.

Recommendation: keep metaswarm as the strongest full-team alternative and a source of coherent role/review structures. It is not my first one-week Crew trial because more host and state assumptions must be reconciled.

## 5. AgentSys: the earlier finding was real, but version matters

The user's recollection is correct. AgentSys **5.14.0** [documents a full `next-task` workflow](https://github.com/agent-sh/agentsys/blob/v5.14.0/docs/workflows/NEXT-TASK.md): discovery, exploration, implementation planning, owner approval, implementation, quality gates, review, and delivery. Its policy can stop at “PR Created” rather than merge. It also includes generated [Kiro planning profiles](https://github.com/agent-sh/agentsys/blob/v5.14.0/.kiro/agents/planning-agent.json). Describing all AgentSys versions as merely a small skill catalogue was inaccurate.

However, its [5.14.0 marketplace manifest](https://github.com/agent-sh/agentsys/blob/v5.14.0/.claude-plugin/marketplace.json) points to a separate `agent-sh/next-task` repository, pinned to `8feba0141a895d651a850cbe724a0e333c24a3a0`. That repository returned 404 to this connection during this research. This does not prove deletion, but means a fresh public install of that dependency is not established. The retained generated profiles/docs are not the entire external plugin runtime. Do not assume a historical tag fixes missing dependency access.

The checked latest [6.1.1 release](https://github.com/agent-sh/agentsys/releases/tag/v6.1.1) instead advertises a current [Foreman queue workflow](https://github.com/agent-sh/foreman). Its [skill](https://github.com/agent-sh/foreman/blob/main/skills/foreman/SKILL.md) relies on worktree agents and Revuto review, permits the session to self-review if Revuto is unavailable, and lands changes. Those behaviors require changes for this user's separate-reviewer/human-merge contract. Kiro/Codex installation support in the [platform guide](https://github.com/agent-sh/agentsys/blob/main/docs/CROSS_PLATFORM.md) is not evidence that Claude-native workflow enforcement carries unchanged.

Recommendation: preserve legacy AgentSys as a real close match, but do not make inaccessible old plugin code a critical dependency. Use current AgentSys selectively unless a reproducible complete legacy source is obtained with permission.

## 6. Other systems and why they are not the first choice

| Candidate | What the inspected evidence supports | Decision for this project |
| --- | --- | --- |
| [GSD Core](https://github.com/open-gsd/gsd-core) | Full phase loop, model profiles, bounded dynamic escalation, fresh-context approach | Valuable alternative; its [Kiro integration decision](https://github.com/open-gsd/gsd-core/blob/next/.out-of-scope/kiro-runtime-in-core.md) declines new first-party Kiro runtime support while permitting external integrations. A Codex-hosted installation is different from a Crew-wide solution |
| [Superpowers](https://github.com/obra/superpowers) | Complete design → approval → implementation plan → subagent work → review methodology | Lean lifecycle fallback; add Crew role/capability/usage integration and adapt host dispatch |
| [Workgraph](https://github.com/shiro-el/workgraph-skills) | Coherent complete multi-PR process; current README uses Linear and pinned upstream submodules | Useful but not the least-adaptation GitHub/Crew baseline; do not import the older five-skill description as current fact |
| [ADW](https://github.com/pdoronila/adw) | Deterministic workflows, human gates, separate review, within-backend usage/failure routing | Good small routing/gate donor; no inspected Kiro backend. Importing its whole executor adds another worker owner |
| [agent-pipeline](https://github.com/roycehoe/agent-pipeline) | Interconnected planning/audit/execution procedures | Useful narrower alternative; host-specific tools and verification order need adaptation |
| [Kiro Team](https://github.com/requix/kiro-team) | Actual Kiro JSON roles and plan/build/validate/document flow | Native role reference; source [lead prompt](https://github.com/requix/kiro-team/blob/main/.kiro/agents/team-lead-prompt.md) mandates worktrees, and [profile](https://github.com/requix/kiro-team/blob/main/.kiro/agents/team-lead.json) pins a model. No observed cross-tool or credit-aware router |
| [Kiro Harness](https://github.com/TeiNam/kiro-with-harness) | Rich native Kiro V3 roles, model-family policy, context and cost skills | Technically close enough to revisit. No root LICENSE was found in the inspected tree/package, so permission for packaging its whole assets is unresolved. Its [cost skill](https://github.com/TeiNam/kiro-with-harness/blob/main/skills/cost-tracking/SKILL.md) assumes an existing usage database; it does not create the meter |
| [kiro-workspace](https://github.com/wilbur-labs/kiro-workspace) | AI-DLC-based workspace/context/learned-memory template | Reference for workspace layout; not verified as a complete cross-backend team. Redistribution permission not established in this screening |
| [HJang orchestrator](https://github.com/HJang/multi-agent-orchestrator) | Detailed portable development protocol | README explicitly says per-CLI adapters are specified but not implemented; cannot count it as ready execution code |
| [oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) / [oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | Substantial host-specific teams, workflows, routing/context features | Worth a dedicated Codex/Claude-worker experiment; not proof of cross-backend Crew control. Grandchild cost/permission attribution must be checked |
| [oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | Multi-model host ecosystem, now describing OpenCode/Pi paths | Adds a host/runtime migration; not first choice for the installed Kiro/Codex setup |
| [Ruflo](https://github.com/ruvnet/ruflo) | Large meta-harness with agents/hooks/memory/MCP | Potential standalone alternative; broad runtime changes are greater than our first Crew-based trial |
| [Microsoft Conductor](https://github.com/microsoft/conductor) | YAML engine, human gates, effort mapping, scripts/MCP and cost views | Strong separate runtime; inspected provider list does not establish a Kiro/Crew backend. A custom provider bridge is extra work |
| [Orchestrator.inc](https://github.com/OrchestratorInc/agent-orchestrator) / [Gas Town](https://github.com/gastownhall/gastown) | Full multi-agent workspaces and lifecycle control | Real systems, but adopting their control planes changes the architecture and operational footprint; not a small library installation into Crew |
| [Overstory](https://github.com/jayminwest/overstory) | Multi-runtime orchestration implementation | Archived; README points to Warren. Avoid making an archived new runtime our minimal integration baseline |
| [Antfarm](https://github.com/snarktank/antfarm) | Repeatable specialist workflows on OpenClaw | OpenClaw-specific dependency/runtime boundary; no inspected Crew adapter |
| [Spec Kit](https://github.com/github/spec-kit), [OpenSpec](https://github.com/Fission-AI/OpenSpec), [cc-sdd](https://github.com/gotalab/cc-sdd) | Strong reusable specification-to-implementation processes | Useful planning alternatives. cc-sdd's `kiro-*` naming means Kiro-inspired specs, not demonstrated Kiro CLI support; its README lists other host integrations |
| [ECC](https://github.com/affaan-m/ECC) | Large engineering skills/harness ecosystem | Additional library candidate; deeper compatibility testing is needed before selecting its Kiro or Crew path |
| [agent-crew](https://github.com/exaltedo2/agent-crew) | Compact full Claude role team, explicit model/effort defaults, transcript ledger | Role/routing donor. Claude/PowerShell-specific install and guessed fallback pricing do not supply our Kiro/Codex accounting |
| Moifek/kiro-ensemble; iYoungblood/agentforge | Public references described relevant teams/pipelines | Repository/file lookup returned 404 to this connection; do not build an adoption recommendation on uninspectable source |

These are screening judgments, not performance rankings. No stars, marketing accuracy claims, or agent-count totals were used as proof of workflow reliability.

## 7. The monitoring and context answer

A more complete lifecycle system does not remove the need to meter the actual execution route. Crew already provides the relevant starting point: prior records show Kiro credits and Codex token/cache metrics. Its account-usage implementation and run-state linkage are in the [local cost findings](../history/RESEARCH_COST_NOTES.md). Reuse them first, keep source/unit/freshness/coverage explicit, and expose a concise read-only summary to the coordinator before phase/worker decisions.

[agentic-coding-harness](https://github.com/sblattj/agentic-coding-harness) is a strong supplementary source, but its [Kiro guide](https://github.com/sblattj/agentic-coding-harness/blob/main/docs/KIRO.md) contains a significant caveat: in its reported V3 calibration, the proxy meter saw far fewer credits than the session store on Kiro 2.36.0. Its documented tests include fixtures/fake servers; that is not independent confirmation for our Kiro 2.37.0 route. Do not replace Crew's working meter with a proxy or wrap all workers merely to obtain a dashboard. Reuse a parser/data model only where it addresses a demonstrated gap.

For context, combine Crew's explicit inheritance switches with the chosen system's compact spec, code-map, JIT loading, and resume artifacts. A short copied prompt does not guarantee a short effective session; inspect actual inherited content and reported tokens. Preserve project instructions and approvals. Keep implementer fixes in their useful existing context and reviewer contexts separate. Aider/Repomix remain optional repo-map tools if native reading proves insufficient; neither is required merely because a rich skill library exists.

The minimal smart policy is an auditable choice of supported backend, role, skill, model, effort, context, and stop limits using task risk and recent resource data. It can be a small Crew policy/configuration layer; it need not be a learned router. ADW's [model router](https://github.com/pdoronila/adw/blob/main/src/adw/model_router.py) provides a concrete within-backend algorithm, with missing-probe behavior that we must not mislabel as a budget guarantee.

## 8. Recommended assembly and first real trial

Use the [current extension assembly](CREW_EXTENSIONS_2026-11-16.md): native Crew features, then AI-DLC Studio, then portable libraries for actual gaps. The BMAD assembly below is a concrete alternative if the existing extension proves unsuitable.

**Alternative assembly:** Crew 0.12.2 + pinned BMAD 6.12.4 library/runtime assets + supported Crew spawn/profile policy + native Crew context/usage evidence. Do not install several primary lifecycles simultaneously.

The first trial should answer a real integration question: can Crew run BMAD's code-grounded planning and a separate plan-checking role, with its generated artifacts and dependencies intact, while stopping before implementation? It should use this repository or a designated harmless local fixture, never a worktree requirement or changes to another real project. Register shared assets through supported loading, but verify BMAD's per-project `_bmad` references too; `skills.extra_paths` alone does not install those dependencies.

Required evidence: version-pinned install/source and notices; successful native rendering; correct target paths; actual selected skill/persona; a produced technical artifact; a genuinely separate reviewer/worker completion; requested/applied model/effort or explicit unknowns; parent/worker usage rows or a disclosed telemetry blocker; no project implementation before approval. Preserve the VS Code startup path and stop on the first required failure. Then revise the experiment using the evidence rather than auto-switching or silently weakening a requirement.

If AI-DLC is tried next, its first gate is hook/approval compatibility, not a full feature run. If metaswarm is tried, the first gate is host/state/dispatch integration with reduced fan-out and human merge control. If old AgentSys is retried, the first gate is reproducible access to all pinned plugin dependencies. This makes each alternative falsifiable and keeps experimentation bounded.

## 9. Schedule implications

The earlier **5–7 focused working days** remains an aspirational pilot target, conditional on the first foundation passing. Research has identified a plausible route, not measured the adaptation effort. A first planning-slice trial is a working-session-sized investigation, not proof that a complete robust system takes a week.

Use the existing day-2 checkpoint to decide from actual evidence whether the same week's goal remains realistic. The usable core must still include actionable planning with pre-code owner approval, independent review, actual worker selection, context controls, and credit/usage-informed decisions; a second planning stage is optional. An unresolved host gate or telemetry source may require more time or an agreed architecture adjustment. Broad project hardening and online learned routing are separate from the initial pilot.

## 10. What changed from the earlier plan

- The supplied [research](EXTERNAL_RESEARCH.md) recommended Workgraph/agent-pipeline/ADW donors and treated BMAD as peripheral. That recommendation is reconsidered, rather than treated as an instruction: stable BMAD's explicit Kiro/Codex installation support and coherent library make a full-base trial worth testing. This is an integration-effort hypothesis, not an established win over the donor approach.
- Full systems are evaluated as possible foundations, rather than being reduced automatically to isolated skills.
- BMAD stable, AI-DLC, metaswarm, and both AgentSys generations are compared explicitly.
- AgentSys's historical full workflow is acknowledged; its missing plugin dependency is the concrete current blocker.
- AI-DLC's Kiro/Codex metering gap and Crew-hook mismatch are recorded from implementation, despite its strong native-platform support.
- A rich agent catalogue does not establish adaptive model/effort or credit-aware dispatch; those mappings are named rather than assumed.
- The next experiment exercises an existing candidate's real planning/review path. The generic homemade diagnostic skill is no longer the primary deliverable.
- No candidate has been installed or declared working. The user can inspect and run the revised next-step prompt before implementation proceeds.
