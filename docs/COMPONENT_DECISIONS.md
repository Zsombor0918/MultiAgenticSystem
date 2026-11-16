# Component decisions

Updated: 2026-11-16. Crew remains the selected runtime. Local preparation and focused offline checks are complete; the live extension trial is pending.

| Component | Decision and exact source | Evidence / remaining work |
| --- | --- | --- |
| Kiro Crew 0.12.2 | Retain installed runtime and native app loader, capability cards, dispatch, context and usage | Studio manifest/loader tests pass against this installation; no repeat of the earlier delegation benchmark |
| AI-DLC Studio 2.0.1 | Install the [pinned release](https://github.com/warren830/kirocrew-app-aidlc/tree/8b3881d4737399c3394d8d187f102a5c95d6e528) through Crew's native local-app CLI | Installed and recorded enabled with per-app local trust. Backend startup, actual planning/review and live gate remain NOT RUN |
| Bundled AI-DLC | Keep Studio's 2.11.3 payload, upstream base `a8721be3631e6a254cf524ea57e5932aa56b4149`, with its four documented patches | All 373 payload files matched recorded sizes/hashes. Do not substitute upstream 2.11.4 or remove compatibility patches |
| Bun 1.4.4 | Use the [official release](https://github.com/oven-sh/bun/releases/tag/bun-v1.4.4), only under the ignored pilot directory | Archive matched published SHA-256; binary reports 1.4.4. Launcher provides its path; real gateway/session reachability still needs the VS Code trial |
| Studio UI | Reuse the release's committed `ui/dist/index.mjs` | Source and installed copy match; Node syntax check passes. No npm install or UI rebuild needed |
| Test dependencies | Isolated pilot overlay: pytest 8.4.2 and pytest-asyncio 1.2.0 | No changes to the installed Crew environment. Only selected upstream tests ran |
| Other libraries/apps | Defer Spec Builder/BMAD/Superpowers/metaswarm and additional dashboards | Do not install competing lifecycles. Reconsider only from actual Studio integration evidence |

Studio is Apache-2.0; its bundled AI-DLC is MIT-0. The checkout/installed app retain `LICENSE`, `THIRD_PARTY_NOTICES.md`, `payload/AIDLC-LICENSE` and payload provenance. Bun is a separate local dependency with its release provenance recorded here. No third-party code is vendored into this repository's tracked source. Original local work stays AGPL-3.0-only.

Local layout:

- `.runtime/pilots/aidlc-studio-2.0.1/source/`: pinned ordinary clone, not a worktree.
- `.runtime/pilots/aidlc-studio-2.0.1/bun/bin/bun`: verified local dependency.
- `.runtime/pilots/aidlc-studio-2.0.1/test-deps/`, `test-tmp/`: isolated test overlay and generated fixtures.
- `.runtime/pilots/aidlc-studio-2.0.1/fixture/`: separate harmless planning repository; no harness installed into it yet.
- `.runtime/pilots/aidlc-studio-2.0.1/backups/`: private configuration backups before trust changes.
- `.runtime/kirocrew/apps/aidlc-studio/`: native installed app copy.

Installation used `kirocrew app install <pinned local source>`, merged only `aidlc-studio` into `agent.apps_trusted` and `agent.apps_trusted_local` via native config commands, then used `kirocrew app enable aidlc-studio`. All commands used this repository's `KIROCREW_HOME`. Blanket third-party trust stays off. No gateway was reached; enablement registered one Advisor agent without running it. Gateway lifecycle hooks are pending the normal task start.

Native enablement also generated the namespaced `~/.kiro/agents/aidlc-studio--aidlc-studio-advisor.json`; existing global agents were not replaced. No Crew/adapter package, shell profile or other project was changed. The only launcher changes add the local Bun path and let a nonzero doctor result stop startup. See [results](STEP_1_RESULTS.md) and [remaining execution plan](NEXT_STEP.md).
