# Kiro Crew köré építhető kész TARS-szerű fejlesztőrendszer – mélykutatás

## Fő következtetés

A mostani, szélesebb kutatás alapján **sokkal kevesebb saját fejlesztés kell, mint elsőre gondoltuk**. Nem találtam egyetlen olyan kész csomagot, amelyet egy az egyben a Kiro Crew 0.12.2-be telepítve megkapjuk a teljes kívánt rendszert, viszont találtam **több olyan kész projektet, amelyekből a lényegi részek már implementálva vannak**: issue-felbontás, agent/skill kiosztás, model+effort routing, approval gate-ek, worktree izoláció, független review, CI-visszacsatolás, költségmérés és kontextuskezelés. citeturn367801search4turn367801search3turn367801search5

A legfontosabb felismerés: **nem egy új orchestrator kell, hanem a Kiro Crew meglévő orchestrációjába néhány jól kiválasztott kész skill/workflow/policy átemelése.** A Crew már natívan tud `SKILL.md` csomagokat betölteni, keresni és akár Jevvel kiválasztani; a projektszintű skillek `.kiro/skills/`, a Crew globális skillek `~/.kiro/crew/skills/` alatt használhatók, és nincs szükség package-rebuildre. citeturn220186search0turn220186search1turn220186search2

Ez jól illeszkedik a saját célworkflow-dhoz: Issue → repo-alapú terv → approval → implementáció → shell/CI → független review → PR/bizonyíték, miközben a GitHub és a CI marad a végső igazságforrás. fileciteturn0file2

## A legerősebb kész elemek, amelyeket ténylegesen érdemes átvenni

Az alábbiak közül **nem mindet futtatnám külön rendszerként**. Sokkal érdekesebb a belsejükből átvenni a már kidolgozott skilleket, policy-kat és algoritmusokat.

| Projekt | Mi van már készen | Mit vennék át Kiro Crew-ba | Integráció |
|---|---|---|---|
| **Workgraph Skills** | Goal → issue graph → külön worktree → automatikus model+effort választás → független PR-review → integrációs audit | `plan-workgraph`, `implement-issue`, `review-issue-pr`, `audit-integrated-work`; **ez áll legközelebb a kívánt működéshez** | SKILL.md szinten nagyon jó donor; MIT. citeturn287308search0 |
| **ADW – AI Developer Workflows** | `feature`: plan → human approve → build → deterministic gates → fresh reviewer → human final gate → PR; model router, budget gate, usage-aware downshift, failure-based upshift | `src/adw/workflows/steps.py` logikája, routing-policy, gate/review-loop | Nem kell külön futtatni; algoritmust/policy-t érdemes Crew workflow-ba átvenni. citeturn546275search0turn591841search4 |
| **agent-pipeline** | `plan → audit → execute → validate`, explicit human gate, retry, külön PR-audit; workerek explicit model tiert kapnak | a feature pipeline skilljei és a plan-audit / implementation-validate szétválasztása | Nagyrészt közvetlen SKILL.md donor; MIT. citeturn887885search6turn623039search3 |
| **agent-crew** | lead/architect/coder/reviewer/scout; agentenként model+effort; költségledger; hire/retire/retro; runaway limitek | agentprofilok, routing táblák, `crew-retro`, cost-ledger mintája | Claude-specifikus hookokat át kell írni, de a szerep- és policyfájlok erős donorok; MIT. citeturn295445search7turn546275search2turn623039search0 |
| **Lousy Agents Skills** | feature → terv/issue, issue finomítás és gyermekissue-k, dependency graph, spec audit, adversarial tests, review triage | főleg `issue-refine-loop`, `plan-to-graph`, `spec-auditor`, review/testing skills | Szabványos Agent Skills; BSD-2-Clause. citeturn546275search4turn627585search3 |
| **GSD Core** | repo-feltérképező, researcher, planner, plan-checker, executor, verifier, debugger, integration-checker; wave-alapú delegálás | planning + plan-check + fresh-context execution mintája | Meta-prompt/agent donor; MIT. citeturn450472search0turn450472search1turn450472search11turn627585search2 |
| **Superpowers** | brainstorming → terv → TDD → subagent implementáció → review; külön olcsó orchestrator-minta | planning/TDD/review kész skillek | Több harnessben használható; MIT. citeturn236034search7turn623039search6 |
| **AI-DLC** | requirements/design/implementation/testing, valódi approval gate, Kiro/Codex/Copilot támogatás | lifecycle-gate és plan-approval logika | Kiro támogatása különösen érdekes; MIT-0. citeturn236034search4turn236034search5turn623039search1 |
| **BMAD Method** | analyst/PM/PO/architect/dev agentek, ticket slicing, review, QA, retrospektív; Agent Skills formátum | egyes planning/ticket/testing workflow-k | Hasznos donor, de **nem ez a központ**; MIT. citeturn236034search0turn236034search1turn627585search0 |
| **Spec Kit** | Specify → Plan → Tasks → Implement → Converge; 40+ agentintegráció; extension/preset/workflow rendszer | specifikációs és quality-gate sablonok | Kiro támogatott; MIT. citeturn236034search3turn623039search5 |
| **Ralph** | GitHub Issue/plan → implementer → reviewer loop; Docker sandbox; history és retry | unattended retry/history/TDD minta | Inkább algoritmus-donor; MIT. citeturn450472search5turn623039search7 |
| **Chipping Orchestrator** | Issue watcher → worktree → Codex/Claude implementer → független reviewer → PR; persistent state | issue lifecycle, reviewer-contract, GitHub state machine | külön orchestratornak nem kell, de a `workflow/`, `agents/`, `observability/` részei jó minták; Apache-2.0. citeturn591841search1turn591841search6turn812125search2 |
| **AgentGrid** | planner → párhuzamos coderek → reviewer rejection → integrator → determinisztikus tester → PR; strukturált handoff ledger | structured handoff + reviewer-reject/reassign mechanizmus | Erős referencia, de Gemini-specifikus. citeturn450472search6turn812125search1 |
| **Microsoft Conductor** | deklaratív multi-agent workflow, provider/model/reasoning effort, context mode, cost tracking, human gates, checkpoint/resume | YAML workflow és human-gate implementation ötletek | Ne legyen második orchestrator; a gate/routing megoldásait érdemes tanulmányozni; MIT. citeturn295445search10turn887885search10turn623039search4 |
| **GitHub Copilot Fleet** | automatikus task-felbontás, párhuzamos custom subagentek, külön context window; beépített Explore/Task/Review/Research agentek | Copilot worker esetén natív delegálás kihasználható | Crew → Copilot worker alatt opcionális; ACP módban a `--fleet` nem használható, tehát ezt külön kell capability-testelni. citeturn295445search4turn295445search5turn295445search11 |

A **Workgraph Skills** különösen fontos találat. Ez már gyakorlatilag megvalósítja azt az elvet, amit kerestél: a coordinator bont, a munkát külön worktree-kbe adja, **feladatonként modellt és reasoning effortot választ**, külön agent review-zza a PR-t, és a végén integrációs audit történik. Ebből szerintem nem csak inspirációt, hanem konkrét skilleket érdemes átvenni és Crew-ra adaptálni. citeturn287308search0

Az **ADW** a másik kiemelkedő donor. A modellroutere már azt csinálja, amiről beszéltünk: szerepenként van kiinduló model tier, közelgő usage-limitnél olcsóbb modellre vált, ismételt validation-failure esetén feljebb lép, és a teljes futásra költségkapu állítható. Ez még backend-en belüli routing, de az algoritmus nagyrészt kész. citeturn546275search0

## Skill- és agentkészletből sem kell nulláról indulni

A Crew skillrendszere alapból alkalmas nagy katalógus kezelésére: indexel, kereshető `skill_search`-csel, lazy-loadingot használ, és Jev a normál trigger-match eredményét felülírva egy skillt automatikusan is kiválaszthat. Ez nemcsak elmélet: a jelenlegi dokumentáció konkrétan leírja a `skills.select` döntési pontot és annak fallbackját. citeturn367801search3turn367801search5

A használható skillforrásokból már most óriási kínálat van:

| Forrás | Hasznos nekünk |
|---|---|
| **VoltAgent awesome-agent-skills** | 1000+ összegyűjtött Agent Skill, több harness támogatásával. Katalógusnak kiváló; nem telepíteném vakon az egészet. citeturn861077search2turn861077search3 |
| **Sentry Skills** | valóban használt engineering skillek: code review, find-bugs, security-review, iterate-pr, CI, skill-scanner, AGENTS.md kezelés; Apache-2.0. citeturn861077search5 |
| **Matt Pocock Skills** | planning, TDD, debugging, ticketing, context/handoff jellegű kis composable skillek. citeturn861077search4turn861077search8 |
| **mthines/agent-skills** | teljes `aw` workflow, friss szemű review, PR-review, review-loop, bugfix, handoff, persistent-memory; MIT. citeturn887885search2turn287308search2 |
| **rsodre/agent-skills** | software design principles, multi-persona design review, spec discipline, agent workflow; agent-agnosztikus SKILL.md. citeturn287308search1 |
| **arjunprabhulal/agent-skills** | 60+ skill testingre, review-ra, securityre, SRE-re, debuggingra, build/deliveryre; MIT. citeturn450472search9turn627585search4 |
| **Anthropic Skills** | hivatalos Agent Skills referenciaminták, template és technikai skillek; sok Apache-2.0 komponens. citeturn861077search0 |
| **agent-pipeline** | kifejezetten gated implementation/audit pipeline kész skillekkel. citeturn887885search6 |
| **Workgraph Skills** | öt igen célzott, fejlesztési lifecycle-skill; szerintem első körben ez a legfontosabb import. citeturn287308search0 |

Ez megváltoztatja az eredeti stratégiát: **nem 90 saját skillt kell létrehozni**. Inkább kell egy **kurált skillkatalógus**, ahol a Crew csak az engedélyezett, auditált skillekből választ. A skillbiztonság nem elméleti probléma: több scanner kifejezetten prompt injectiont, credential exfiltrationt és veszélyes scriptet keres az Agent Skills csomagokban. A Cisco scanner például AST/dataflow, YARA/pattern és opcionális LLM-ellenőrzést is használ; Sentrynek szintén van külön `skill-scanner` skillje. citeturn157421search9turn157421search10

## Kontextus, usage és routing: itt is vannak kész donorok

A repo-kontekstre **nem fejlesztenék első körben saját rendszert**. A Crew már tud lazy skill/context betöltést és kontrollált memory/project inheritance-t, de ezt ki lehet egészíteni kész repo-map megoldásokkal. citeturn367801search5turn295445search2

Az **Aider Repo Map** Tree-sitter + dependency-graph ranking alapján csak a tokenbudgetbe férő, aktuálisan releváns szimbólumokat küldi a modellnek. A **Repomix** tokeneket számol, Tree-sitteres tömörítést kínál, MCP szerverként is használható, sandbox módja read-only workspace-be zárható, és Agent Skillt is tud generálni a repóból. citeturn816661search1turn287308search4turn816661search8

A **Codemaps** még érdekesebb lehet később: lokális code graphot és külön `orient`, `locate`, `impact`, `guardrails`, `risk`, `security` nézeteket ad MCP-n keresztül. Ugyanakkor jelenleg pre-alpha, ezért ezt PoC-alapnak nem választanám. citeturn157421search12

A usage oldalra az egyik legerősebb találat az **agentic-coding-harness**. Kirot, Codexet és Copilotot is képes mérni, cache-aware tokenadatot, költséget, budget limitet és OpenTelemetry eseményeket normalizál; a Copilotnál külön kezeli az AI credit telemetriát, és ha nincs megbízható cost adat, nem hazudja azt, hogy nulla. MIT licencű. citeturn157421search3turn591841search3turn812125search3

Nem javaslom, hogy ez futtassa a workereket a Crew helyett. **A parser/adatmodell/metering logikája viszont nagyon értékes donor** a Crew saját usage JSONL-ének kiegészítéséhez.

A **Langfuse** szintén használható külső observabilityként: jelenleg külön coding-agent integrációkat dokumentál Codexhez, Copilothoz és Kirohoz, OTel-alapú tracinggel. Viszont ez telemetria, nem permission enforcement; maga a dokumentáció is figyelmeztet, hogy a hookokat a lokális user ki tudja kapcsolni. citeturn157421search0turn157421search1

A routingnál három réteg rajzolódik ki. A Crew saját Jevje már tud `simple / medium / complex → model` döntést, de **subagenteket és appokat nem route-ol automatikusan**, tehát ez önmagában nem oldja meg a worker-routingot. citeturn367801search3 Az ADW kész, használati-limitet és failure-t figyelő model laddert ad. citeturn546275search0 Ha később valóban adatvezérelt routing kell, a RouteLLM és hasonló routerek már minőség/költség kompromisszumot optimalizáló infrastruktúrát adnak, de ezt csak elegendő saját futásadat után lenne értelme bekötni. citeturn157421search5

## A konkrét összelegózható stack, amit most választanék

Nem húsz frameworköt telepítenék. A kutatásból szerintem ez a **legjobb minimális Crew-stack**:

| Réteg | Megoldás | Miért |
|---|---|---|
| **Orchestrator/runtime** | **Kiro Crew 0.12.2** | Task Runner, Dynamic Workflows, subagentek, worktree, approval, persistence, memory, usage. citeturn367801search4turn367801search1 |
| **Skill discovery** | Crew `skill_search` + később Jev `skills.select` | Kész, lazy; nem kell saját skillrouter. citeturn367801search3turn367801search5 |
| **Nagy issue bontása** | **Workgraph `plan-workgraph` + Lousy `issue-refine-loop/plan-to-graph`** | Issue-alapú, dependency-aware, session-sized munka. citeturn287308search0turn546275search4 |
| **PLAN + approval** | Crew Task Runner + **agent-pipeline** plan/audit gate | külön terv és ellenőrzés már implementálva. citeturn367801search4turn887885search6 |
| **Implementáció** | Crew `spawn_run`; Workgraph `implement-issue` eljárása | külön worktree, szűk scope. citeturn295445search2turn287308search0 |
| **Model/effort routing** | első körben **Workgraph policy + ADW model ladder** | kész nehézség/risk-alapú model+effort minta + usage/failure adaptáció. citeturn287308search0turn546275search0 |
| **Teszt** | shell/CI | determinisztikus ground truth; ne pazaroljunk külön LLM-et puszta `pytest` futtatására. Az AgentGrid is ezt a mintát használja. citeturn450472search6 |
| **Reviewer** | Workgraph `review-issue-pr` vagy Sentry `code-review` / `find-bugs` | külön context, tényleges diff. citeturn287308search0turn861077search5 |
| **Security** | Sentry/Cisco skill scanner + Crew permission/sandbox | harmadik féltől hozott skilleket install előtt ellenőrizni. citeturn157421search9turn157421search10 |
| **Repo context** | először Crew natív context; szükség esetén Repomix/Aider map | kész, olcsóbb, mint saját indexer. citeturn367801search5turn816661search1turn287308search4 |
| **Usage** | Crew ledger + agentic-coding-harness parser/adatmodell mintája | Kiro-credit / Codex-token / Copilot-credit külön egységben. citeturn157421search3turn591841search3 |

Az első körben **nem futtatnám egyszerre az ADW-t, GSD-t, BMAD-ot vagy más lifecycle rendszert a Crew mellett**, mert akkor két orchestrátor próbálná megmondani, mi a következő lépés. Ezekből a használható skilleket és algoritmusokat kell importálni, nem a teljes runtime-ot.

## Mi kész, mihez kell adapter, és mi hiányzik ténylegesen?

| Igényed | Készből | Adapterezés | Valóban hiányzik |
|---|---:|---:|---:|
| Issue → repo PLAN | ✅ | minimális | |
| PLAN approval | ✅ | workflow bekötés | |
| opcionális második PLAN | ✅ mintákból | workflow policy | |
| nagy issue automatikus bontása | ✅ Workgraph/Lousy/BMAD | GitHub-szabályainkhoz igazítás | |
| specialista agentek | ✅ sok kész profil | Crew agent-formátumra mapping | |
| 50–100+ skill katalógus | ✅ | audit + kuráció | |
| automatikus skillválasztás | ✅ Crew/Jev | config | |
| implementáció külön worktree-ben | ✅ Crew | | |
| független review | ✅ Crew/Workgraph/Sentry | | |
| shell/CI validáció | ✅ | projektparancsok | |
| backend Kiro/Codex/Copilot | részben ✅ | capability-test | |
| automatikus modellválasztás | ✅ részben | Workgraph/ADW policy bekötése | |
| automatikus effortválasztás | Workgraphban kész minta | Crew spawn policy | **kis hiány** |
| provider-váltás minőség/költség szerint | | **adapter/policy** | **nincs kész Crew-wide router** |
| per-worker usage | ✅ részben | normalizálás | |
| credit/token/quota közös jelentés | | **kis adapter** | |
| saját eredményekből tanuló routing | | | **későbbi fejlesztés** |
| hard cross-provider budget | | | **külön megbízható enforcement kell** |

A Crew saját Jev-modelroutingja fontos, de jelenleg a dokumentáció szerint **nem route-olja a subagenteket**, tehát a hiányzó központi darab valóban egy `worker.route` jellegű döntés: task type + risk + context + korábbi eredmény → backend + model + effort + agent profile. citeturn367801search3

Ez azonban már **nem egy új orchestrator**. Inkább egy nagyon vékony policy/adapter a meglévő `spawn_run` előtt.

## Az első PoC, amit ebből építenék

A PoC-hoz **egyetlen valódi, kis GitHub Issue** kellene. Nem benchmark és nem mesterséges marker.

A folyamat:

`Issue → issue-refine / repo-map → PLAN → plan-audit → STOP → emberi approval → worker.route → Crew spawn_run → worktree implementáció → shell/CI → külön review skill → PR/report → usage`

A PoC során három kész külső donorral kezdenék: **Workgraph Skills**, **agent-pipeline**, **ADW routing policy**. Mellé a Crew saját Task Runnerét, `spawn_run`-ját, skill discovery-jét és usage ledgerét használnánk. A külső skilleket előtte Sentry/Cisco scannerrel ellenőrizném. citeturn287308search0turn887885search6turn546275search0turn157421search9turn157421search10

A sikerkritérium nem az lenne, hogy „az agent szerint kész”, hanem hogy ugyanahhoz az Issue-hoz visszaköthetően megvan a jóváhagyott terv, a tényleges diff, a CI/test eredménye, a független review, a választott backend/model/effort indoka és a per-worker fogyasztás. Ez pontosan megfelel a saját workflow-d bizonyíték- és kontrollkövetelményeinek. fileciteturn0file2

**A kutatás alapján most már nem azt javaslom, hogy írjunk saját skillcsomagot.** Először össze kell rakni egy **kurált, auditált Crew skillkatalógust** a Workgraph + agent-pipeline + Sentry + Lousy + Superpowers/GSD legjobb elemeiből, és az ADW kész routinglogikáját kell Crew `spawn_run` elé adaptálni. Ha ez működik, a tényleges saját kód várhatóan a **worker-routing és usage-normalizálás vékony ragasztórétegére** korlátozható.