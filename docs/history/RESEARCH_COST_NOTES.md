# Kiro Crew 0.12.2 — költség, keretek és modellválasztás

2026-11-16. Folyamatban lévő, helyi forráskódra és meglévő futásadatokra támaszkodó vizsgálat. Új modellhívás vagy Crew-agentfutás nem indult. A kód képességet bizonyít, nem a jelenlegi beállítás hatását.

## Kiinduló megállapítás

A Kiro-kreditek, a Codex-előfizetés kerete és a Copilot-használat nem tekinthetők automatikusan közös pénznemnek. Külön kell kezelni a ténylegesen szolgáltatott usage-adatot, a becsült költséget és a hátralévő előfizetéses keretet.

## 1. Ami már rendelkezésre áll

**KÓDBAN:** az `acp/types.py::TurnUsage` külön tárolja az input/output/cache tokeneket, USD-költséget, Kiro-kreditet, időt és kontextusfoglalást. A `context_sum_tokens` nem számlázott token, hanem a modellhívások után jelentett kontextusfoglalások összege. A `subagent_manager/usage_row.py::persist_usage_row` a workerek promptonkénti adatait is menti. A `dashboard/handlers/usage_spend.py::slot_spend` és `usage_cost.py::cost_breakdown` viszont kifejezetten kreditközpontú összesítést ad: ezt nem szabad minden backend teljes költségmérőjének tekinteni.

**HELYBEN MÉRT:** a `.runtime/kirocrew/usage/tokens/2026-11-15.jsonl` és `2026-11-16.jsonl` meglévő soraiban:

| Worker | Backend a state alapján | Kredit | Input/output/cache-read token | Következtetés |
|---|---|---:|---:|---|
| `fa78c2aa8519413f` | KAS | 0.1528272058 | 0 / 0 / 0 | Kiro-kredit ténylegesen rögzült |
| `cded4303d2d75a01` | KAS | 0.1723346166 | 0 / 0 / 0 | Shellpróba Kiro-kreditje rögzült |
| `8586672e71ba9e1a` | Codex | 0 | 211 / 104 / lásd nyers sor | Vannak tokenadatok; a 0 kredit nem ingyenesség |
| `17fcb93da79bee12` | Codex | 0 | 331 / 319 / 26752 | USD `cost=0`; tényleges pénzügyi díj ebből nem állapítható meg |

A Codex utolsó példájának kontextusa 27402 / 475000, időtartama 29248 ms. A kis markerfeladathoz képest a 26752 cache-read token számottevő keretterhelés lehet, de nem árazható automatikusan a ChatGPT-előfizetésben. A sorokból a beépített prompt, eszközleírások és történet részesedése nem választható szét biztosan. A harness szerinti aggregáláshoz a `slot=subagent:<id>` mezőt a `subagents/<id>/state.json` backendjéhez kell kapcsolni: a usage sor `provider=acp` mezője önmagában nem különbözteti meg a Codexet és a KAS-t.

**KÓDBAN:** `dashboard/handlers/kiro_usage_api.py::fetch_usage_limits` a meglévő Kiro-bejelentkezésből olvassa a fiók felhasznált/tervezett krediteit, ellenőrzi a profil azonosságát; a fallback a CLI `/usage`. Ezt a kutatás nem hívta meg, nem olvasott hitelesítő adatot. Az account-szintű fogyás más Kiro-sessionök használatát is tartalmazhatja; nem azonos egy issue költségével.

**HIÁNY:** Copilot-mérést nem találtam a helyi tesztekben. Az `agent_sdk/backends_turns.py::ACP_BACKENDS_REPORT_USAGE` 0.12.2-ben nem tartalmazza sem a Copilotot, sem a Codexet; ezt a kód szerint nem bizonyított teljes számlázási lefedettségként kell kezelni. A Codex meglévő tokensorai mutatnak részleges adatot, ezért az állítás nem az, hogy semmit sem mér. A provider nem jelentett usage értéke nem egyenlő nulla költséggel.

## 2. Modell- és effortválasztás

**KÓDBAN:** az `agent.role_models` és `agent.role_efforts` valóban létezik, de `config/sections_agent_fields.py::ROLE_MODEL_KEYS` szerint csak **`background` és `subagent`** a támogatott szerep. Nem lehet ide feltételezett `planner`, `implementer`, `reviewer` kulcsokat írni és működést várni. Fázisonkénti választáshoz a dokumentált `spawn_run(model=..., backend=..., reasoning_effort=...)`, megfelelő agentprofil vagy más igazolt workflow-mechanizmus kell.

A helyi KAS `low`/`auto` próba figyelmeztetése szerint az effort nem alkalmazódott. A kért értéket és a tényleges session-beállítást külön kell tárolni. Modellazonosító csak a kiválasztott backend tényleges katalógusából; az „auto” modell önmagában nem képesség- vagy árszerződés.

**KÓDBAN, NEM HELYBEN TESZTELT:** `decisions/points/model_route.py` beépített `model.route` döntési pontot ad. `simple/medium/complex` osztályozás, owner által választott **Auto (Jev)**, engedélyezett döntési réteg, hirdetett modellek és kontextusablak-ellenőrzés szükséges. Manuálisan választott konkrét modellt nem ír felül. A három tier alapból üres: osztályozás történhet anélkül, hogy tényleges modellváltás történne.

`derive_tier_models` a backend saját katalógusának ismert kreditszorzóiból választ: simple = baseline alatti legolcsóbb, medium = örökölt baseline, complex = baseline feletti legdrágább. Hiányzó ár vagy egyértelmű választás hiányában nem derivál. Ez **ár- és feladatkategória-alapú heurisztika, nem mért minőség/költség alapján tanuló, többprovideres optimalizáló**. A „legdrágább” nem minőségbizonyíték. A normál chat-turn döntése nem terjed automatikusan cronra/workerekre; a `model_route_derive` az explicit modell/agent/backend választás nélküli subagent-indításra külön utat ad. A felhasználó mostani explicit `backend=codex/kas` próbáiból nem következik e router működése.

## 3. Kontextus és keretek

**KÓDBAN/DOKUMENTÁLVA:** `session.autocompact_pct` alapértelmezése 70%, de KAS alatt a KAS engine maga dönt a tömörítésről. Van context assembly budget, a workernek átadott memória/projekt/lessons kapcsolható, a role/subagent modell pinelhető, a tool-call szám, idő és konkurencia korlátozható. Ezek költségbefolyásoló fékek, nem egzakt pénzügyi sapkák.

Az átnézett általános konfigurációban **nem igazoltam univerzális issue-szintű Kiro+Codex+Copilot költséglimitet**, amely tényleges kiadás alapján minden új hívást megállít. Az `apps/builtins/auto_improvement/spine/cost.py` külön alkalmazás számára tartalmaz USD-s `CostMeter`-t, de a nulla alapértékű, be nem kötött mérő sosem éri el a limitet. Ezt nem szabad általános Crew-budget garanciának feltüntetni.

**Külön workflow-budget vizsgálat:** `workflows/context.py::Budget` tokenegységű számláló (`budget_total`), nem kredit- vagy USD-sapka. A `charge()` a számláló határán `BudgetExceeded` hibát dob, a `workflows/runner.py` pedig az `agent()`, `open_session()` és `send_to_session()` előtt `would_exceed()`-et ellenőriz. Ugyanakkor a teljes `workflows/*.py` forrásban a `charge()` hívásának automatikus usage-bekötését nem találtam: csak maga a `Budget.charge` definíció szerepel. A híváselőtti ellenőrzés önmagában nem méri a fogyasztást. **A tényleges backend-usage → budget terhelés nincs igazolva; ezt sem nevezném kész hard limitnek.** Ezt helyi modellteszt nélkül a kód olvasása állapította meg, nem teljes futásbizonyítás.

## 4. Minimális javaslat

1. Egyetlen orchestrator, szakaszonként legfeljebb egy worker, kicsi fáziskontextus és tartós terv/eredmény. Nagy terv végrehajtása előtt emberi felbontási kapu.
2. Kezdetben kis, engedélyezett profilkészlet: „tervezés”, „megvalósítás”, „review”; mindegyik ténylegesen kipróbált backend/modell/effort kombináció. A szerepnevek helyi policy-szavak, nem kitalált Crew-configkulcsok.
3. Az orchestrator ezek közül válasszon indoklással; a tesztfuttatás legyen lehetőleg determinisztikus shell/CI, ne új LLM-feladat. Teszttervezés és hibadiagnózis külön AI-feladat lehet.
4. Egy kicsi **csak olvasó usage-riport**, nem új orchestrator: issue/fázis/run-ID, backend, kért és tényleges modell/effort, Kiro-kredit, token/cache adatok, idő, eredmény, mérési hiány. Külön oszlop az API-árból becsült USD-nek; az előfizetéses keretet ne tekintse igazolt díjnak.
5. Több hasonló, elfogadási teszten mérhető feladat után hasonlítsunk: összköltség = tervező + implementáló + reviewer + javítás + újrapróbálás. A legolcsóbb első hívás helyett az elfogadott feladatra jutó költséget kell csökkenteni.
6. A költségadat nélküli backend ne kapjon „0 költség” előnyt. A policy kezdetben soft budget + fázisvégi emberi kapu; hard cap csak külön végponttól végpontig ellenőrzött admission/stop mechanizmussal nevezhető igazoltnak.

## Források

Minden vizsgált kód a telepített `kiro_crew` 0.12.2 csomagból való. Hivatalos, verzióhoz kötött online megfelelők:

- [TurnUsage és ACP statisztika](https://github.com/kirodotdev/KiroCrew/blob/v0.12.2/src/kiro_crew/acp/types.py)
- [Usage-képességmátrix a kódban](https://github.com/kirodotdev/KiroCrew/blob/v0.12.2/src/kiro_crew/agent_sdk/backends_turns.py)
- [Beépített modellrouter](https://github.com/kirodotdev/KiroCrew/blob/v0.12.2/src/kiro_crew/decisions/points/model_route.py)
- [Támogatott role model/effort kulcsok](https://github.com/kirodotdev/KiroCrew/blob/v0.12.2/src/kiro_crew/config/sections_agent_fields.py)
- [Kiro account-usage lekérdezés](https://github.com/kirodotdev/KiroCrew/blob/v0.12.2/src/kiro_crew/dashboard/handlers/kiro_usage_api.py)
- [Kreditközpontú költségnézet](https://github.com/kirodotdev/KiroCrew/blob/v0.12.2/src/kiro_crew/dashboard/handlers/usage_cost.py)
- [Konfiguráció és context-compaction korlát](https://github.com/kirodotdev/KiroCrew/blob/v0.12.2/src/kiro_crew/docs/configuration.md)
