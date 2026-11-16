# Capabilities relevant to the extension pilot

Updated: 2026-11-16. Reuse Crew's native catalogue; this is a small evidence overlay, not a replacement capability database.

| Area | Existing surface | Current evidence / limit |
| --- | --- | --- |
| Runtime / extension loading | Crew 0.12.2 native app loader | Real loader imports and lifecycle tests passed in isolated test homes; Studio is installed/recorded enabled. Live backend health is NOT RUN |
| Backend capabilities | Crew [capability cards](https://github.com/kirodotdev/KiroCrew/blob/v0.12.2/src/kiro_crew/agent_sdk/backend_cards.py) and Agent Harness settings | Use their available/unavailable/unmeasured distinctions. Do not infer native tool/permission equivalence between Kiro and Codex |
| Models and effort | Native `/api/models`, `/api/effort-levels`, spawn controls | No current authenticated model-list query or effective effort test in this slice. Earlier Kiro/Codex observations remain historical |
| Model policy | Native Decisions and optional `model_route_derive` | Existing capability, not enabled by this slice. Remaining backend/role/effort/allowance policy still needs integration |
| Usage and allowance | Native usage/session/account views | No paid Crew turns started here; no fresh task consumption/allowance evidence collected. The user's 33% statement is not a verified cross-provider balance |
| Context | Native inheritance, lazy skill loading and checkpoints | No live planner/reviewer handoff measured. Review identity and scoped context remain required |
| Studio approval handling | Supplied session bridge and patched AI-DLC hooks | Selected unit/fixture tests for duplicate-delivery and actual Bun hook handling passed. Browser-origin approval and denied premature transitions on the live route are NOT RUN |
| Dependency | Bun 1.4.4, Node 24.22.3 for UI syntax check | Local Bun reports its pinned version; archive checksum verified. Launcher exposes Bun; actual extension-session PATH is NOT RUN |
| Startup | Existing VS Code task and launcher | Three local stub tests pass: failed doctor prevents gateway; successful path retains gateway flags/Bun; task still names the same launcher. Actual UI task/restart remains NOT RUN |

Observed facts, fixture-test evidence and live observations are different. A tested host loader does not establish effective worker permissions, independent model review or the complete two-plan workflow. Keep requested/applied settings, credits/tokens/currency, task consumption and remaining allowance separate when live evidence is added.
