# Teszteredmények

Állapotok: **PASS** = tényleges bizonyíték; **FAIL** = futtatott próba hibázott;
**BLOCKED** = előfeltétel megakadályozta; **NOT TESTED** = még nem futott.
Ne tárolj hitelesítő adatot vagy titkot ebben a fájlban.

| Ellenőrzés | Állapot | Bizonyíték / megjegyzés |
|---|---|---|
| Python, WSL, memória, port | PASS | Python 3.12.3; WSL2 Ubuntu 24.04; 13 GiB elérhető; 5476 szabad volt a méréskor |
| Kiro CLI belépés és V3 súgó | PASS | 2.37.0; Builder ID; ACP súgóban V3 (nem modellhívás) |
| Codex CLI belépés | PASS | 0.166.0; ChatGPT (nem adapteres futás) |
| Kiro Crew telepítés | PASS | 0.12.2, aláírt manifest és SHA-256 ellenőrzött wheel |
| Codex ACP adapter | PASS | 1.11.0 telepítve; Node 24.22.3 mellett a Crew feloldja az adaptert; session nincs igazolva |
| Doctor / KAS tényleges route | PASS | CLI ACP V3 relay, CLI credential store; doctor más okokból hibakóddal tér vissza |
| Interaktív setup és Start újraindítása | PASS | Setup lefutott, a második indítás átugrotta; HTTP 200 |
| Gateway és dashboard | PASS | 127.0.0.1:5476, HTTP 200; teszt után leállítva |
| Codex worker futása Crew alatt | PASS | 752636c27154a574: backend és provider codex, modell gpt-6.1-terra[high], elkészült artefaktum |
| KAS supervisor futása | NOT TESTED | A talált chatrekord nem azonosítja a szülő backendjét; külön ellenőrzendő |
| A: Kiro session | NOT TESTED | Nincs modellhívás |
| B: Codex delegálás és eredmény visszaadása | PASS | spawn_run a felhasználó beszámolója szerint; Codex state, artefaktum és completion event ellenőrizve; ID 752636c27154a574 |
| B: a szülő ténylegesen KAS volt | NOT TESTED | A doctor route önmagában nem bizonyítja a chat backendjét |
| C: Codex → Kiro | PASS | Az útmutató szerinti Codex szülőből indított 119d77c035366804 worker rekordja backend/provider kas; a completion esemény és az eredményfájl ellenőrizve |
| D: Kiro fájl és shell | PASS | A Kiro-chat rekordjában külön Read File és unittest shellhívás; beszámoló szerint 1 teszt, OK, exit 0 |
| D: KAS-worker shell | PASS | cded4303d2d75a01: backend/provider kas, parancshívás a naplóban, a worker szerint unittest OK exit 0 |
| D: Kiro natív alagent | BLOCKED | A Kiro session szerint nem állt rendelkezésre invoke_sub_agent; a naplóban nincs eszközhívás. Ez egy sessionre vonatkozó megfigyelés. |
| D: Codex fájl olvasása és shell | PASS | A chat naplója külön olvasást és unittest parancsot mutat; a Codex szerint az olvasás terminállal történt |
| D: Codex külön natív fájlolvasó | NOT TESTED | A Codex szerint ilyen eszköz nem volt elérhető; az olvasás terminálon történt |
| D: Codex natív alagent | PASS | Codex chat: Start subagent calculator_summary, wait, Read file, Complete subagent; azonos agentThreadId szerepel az indulási és befejezési eseményben |

Futásonként jegyezd fel az időpontot, modellnevet, szülő/worker backendjét és
azonosítóját, a látható hívást, az eredmény-visszaadást és az artefaktumot.

A 752636c27154a574 futás fájlja `.runtime/kirocrew/workspace/demo/codex-result.txt`: ez a dashboard által választott külön workspace, nem a projekt gyökerében lévő `demo/`. A futásrekord Codex backendet és providert, valamint `gpt-6.1-terra[high]` modellt rögzít; a szülő chatben a completion esemény látható. A call paramétereit a felhasználó ellenőrizte.

A 119d77c035366804 worker rekordja `backend=kas`, `provider=kas`, `result_complete=true`; a szülő chatbe completion esemény érkezett. A `demo/kiro-result.txt` pontosan a `KIRO_WORKER_DONE` sort és egy sortörést tartalmaz. A szülő naplója `gpt-6.1-terra[high]` modellt rögzít, a backend explicit nevét nem; a Codex szülő kiválasztása a kézi teszt lépésein alapul. A CLI V3 route-ot a korábbi doctor külön igazolta.

A Codex natív alagentpróba sessionje `dashboard_chat-7-1794780735`: a session eseményei egy `calculator_summary` natív alagent elindítását és befejezését, valamint fájlolvasást mutatnak. Ez a natív alagentpróba különbözik a Crew spawn_run delegálásától.
