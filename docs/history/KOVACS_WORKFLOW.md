# KovacsTrader – együttműködési és intelligens AI-fejlesztési workflow

**Állapot:** v0.4 – Kiro Crew-alapú stratégiai munkavázlat és célarchitektúra<br>
**Dátum:** 2026-11-16<br>
**Hatókör:** KovacsTrader / Quant Trading projekt<br>
**Fontos:** ez a dokumentum munkarendet és célarchitektúrát rögzít. A dokumentált, korábban részlegesen kipróbált és végponttól végpontig igazolt képességek nem azonosak.

## 1. Miért van szükség rá?

A KovacsTrader hosszú távú fejlesztési projekt. A cél olyan TARS-szerű, intelligens, többügynökös fejlesztési munkafolyamat, amely a GitHub Issue-kból ellenőrzött, jóváhagyott és visszakövethető fejlesztési eredményeket hoz létre.

A felhasználó a célokról, prioritásokról, kompromisszumokról és jóváhagyásokról dönt. Nem kell kézzel minden részfeladathoz coding agentet, modellt, reasoning effortot, skillt vagy toolt választania.

**A központi orchestrator a Kiro Crew.** A rendszer nem egy új, saját agentframework felépítésére épül, hanem a Kiro Crew meglévő képességeinek helyes használatára és kész külső komponensek integrálására.

Alapelvek:

1. **Rövid stratégiai kommunikáció:** ChatGPT a célok és döntések tisztázásában segít.
2. **Külön stratégiai és technikai tervezés:** ChatGPT a *mit és miért*, Kiro Crew a *hogyan a jelenlegi repositoryban* kérdésért felel.
3. **Emberi jóváhagyási pontok:** a stratégiai Issue, a technikai terv, szükség esetén a részletes terv, a scope-változás és a merge kontrollált.
4. **Intelligens delegálás:** az orchestrator feladatonként választ backendet, agentet, skillt, modellt, reasoning effortot, eszközt és kontextust.
5. **Natív coding képességek:** a Kiro, Codex és más támogatott backendek saját fejlesztőeszközei használhatók, nem szükséges őket mesterségesen egy minimális közös toolkészletre szűkíteni.
6. **Biztonság valódi határokkal:** izoláció, jogosultságok, jóváhagyások, tesztek, független review és CI. A nagyobb eszközszabadság nem korlátlan jogosultság.
7. **Kész komponensek előnyben:** először meglévő Crew-funkció, konfiguráció, importálható skill/agent/workflow; saját kód csak igazolt hiány esetén.
8. **Minőség- és költségtudatosság:** a teljes, elfogadott fejlesztési feladat erőforrásigényét optimalizáljuk, nem pusztán egyetlen agenthívás árát.
9. **GitHub mint nyilvántartás:** a célok, feladatok, PR-ek, tesztek, review-k és státuszok bizonyítékai visszakereshetők.

A TARS-rendszer a strukturált, intelligensen delegáló fejlesztőcsapat inspirációja, nem kötelező technikai függőség.

## 2. Szerepek és felelősségek

| Szereplő | Fő feladat | Határ |
| --- | --- | --- |
| **Felhasználó** | Cél, prioritás, scope, kompromisszumok és jóváhagyások | Nem kell kézzel koordinálnia minden kódszintű lépést |
| **ChatGPT – stratégiai konzulens és kritikus partner** | Ötletelés, alternatívák, kockázatok, Issue-bontás, stratégiai Issue-tervezet | Nem írja elő a teljes konkrét kódmegoldást |
| **Kiro Crew – orchestrator** | Repository-feltárás, technikai terv, dinamikus kiosztás, koordináció, végrehajtás és bizonyítékgyűjtés | Nem ugorhatja át a jóváhagyásokat és a repository-védelmet |
| **Coding workerek** | Tervezési részfeladatok, implementáció, teszt, dokumentáció a választott backend natív képességeivel | Nem léphetnek túl a jóváhagyott scope-on és jogosultságon |
| **Független reviewer** | Diff, követelmények, tesztek, architektúra és kockázatok ellenőrzése | Nem lehet a megvalósító egyetlen önellenőrzése |
| **GitHub és CI** | Issue/PR nyilvántartás, determinisztikus ellenőrzések és merge-védelem | Az agentek nem kerülhetik meg |

### 2.1 Dinamikus specialisták, nem fix saját agenthierarchia

A tervező, implementáló, tesztelő, dokumentációs és reviewer **feladatkörök**. Nem követelmény, hogy mindegyikhez külön, saját fejlesztésű állandó agent tartozzon.

A Kiro Crew a feladat jellege szerint használhat meglévő agentprofilt, specialistát, kész skillt vagy külön workerfuttatást. Egyszerű feladatnál egy worker is elegendő lehet; összetett feladatnál több specialista indokolt.

A **független review kötelező**, a felesleges delegálás nem.

### 2.2 Backendfüggetlenség

A kívánt elsődleges backendek: **Kiro és Codex**. További backend – például GitHub Copilot – csak igazolt támogatás és hasznosság alapján kerülhet be.

Az orchestrator nem feltételezheti, hogy minden backend ugyanazokat a modelleket, toolokat, effortbeállításokat vagy fogyasztási adatokat biztosítja.

A backendválasztás célja az adott feladathoz legalkalmasabb képesség, minőség és erőforrásigény.

## 3. ChatGPT kommunikációs szerződés

### 3.1 Alapmód – rövid stratégiai konzultáció

- Alapesetben **maximum körülbelül 150 szó**, magyarul.
- Elsősorban az aktuális kérdésre, a legfontosabb kockázatra és a következő érdemi döntésre válaszoljon.
- Nincs fölösleges bevezető, ismétlés, automatikus összefoglaló vagy hosszú felsorolás.
- Legyen kritikus és proaktív, de **ne változtassa meg a felhasználó célját**.
- A rövid válasz nem jelenthet felületes elemzést.
- A felhasználó kérhet részletes kutatást, összehasonlítást vagy teljes dokumentumot.

### 3.2 Parancsok

| Parancs | Mire szolgál | Várt eredmény |
| --- | --- | --- |
| **Alapmód** | Gyors stratégiai konzultáció | Rövid, fókuszált válasz |
| `KOVACS:EXPLORE` | Mélyebb ötletelés, kutatás, alternatívák | Részletesebb, kritikus elemzés |
| `KOVACS:ISSUE` | Egyeztetett stratégiai terv formalizálása | GitHub Issue-tervezet, publikálás csak külön jóváhagyással |
| `KOVACS:PLAN` | Issue-alapú, repository-specifikus technikai tervezés indítása a Kiro Crew-ban | **Tervezett belépési konvenció; nem igazolt kész Crew-parancs** |

A ChatGPT-parancsok kommunikációs konvenciók, nem automatikusan regisztrált CLI-parancsok.

### 3.3 Tartós érvényesítés

- A **Quant Trading Project Instructions** a rövid, ideiglenes kommunikációs szabályokat tartalmazza.
- A **`KOVACS_WORKFLOW.md`** a részletes stratégiai referenciadokumentum.
- Új beszélgetésben a dokumentumnak hozzáférhetőnek kell lennie.
- A munkarendet valós tapasztalatok alapján módosíthatjuk.

## 4. Végponttól végpontig munkafolyamat

### 0. Ötlet vagy probléma

A felhasználó ChatGPT-vel tisztázza a célt, értéket, határokat, függőségeket, kockázatokat és elfogadási feltételeket.

ChatGPT szükség esetén ellenőrzi a tényleges GitHub-kontextust, de a stratégiai szakaszban nem talál ki implementációs részleteket.

### 1. Feladatméret és stratégiai terv

Együtt eldöntjük, hogy a munka egy Issue, több önálló Issue vagy epic és kisebb Issue-k legyenek.

A bontás alapja: önállóan értékelhető eredmény, függőség, tesztelhetőség és kezelhető review-méret. Nem mechanikusan fájlonként vagy agentenként bontunk.

### 2. Stratégiai GitHub Issue – `KOVACS:ISSUE`

A jóváhagyott stratégiai tervből a meglévő repository-sablonhoz illeszkedő Issue-tervezet készül.

Tartalma: probléma, cél, scope, nem-célok, kockázatok, függőségek és ellenőrizhető elfogadási feltételek.

**A stratégiai Issue nem írja elő előre az osztályokat, függvényeket vagy kódarchitektúrát.**

A `type:*`, `area:*` és `risk:*` labeleket a meglévő készletből választjuk. Munkastátuszt csak a GitHub Project `Status` mezőjében követünk.

ChatGPT először megmutatja a tervezetet. GitHub-írás csak a felhasználó kifejezett jóváhagyása után történhet.

### 3. Kiro Crew – repository-alapú PLAN

A Kiro Crew az Issue és a tényleges repository alapján technikai tervet készít.

Feladata:

- a releváns kód, tesztek, dokumentáció és repository-kontraktusok feltárása;
- az érintett komponensek és függőségek azonosítása;
- a megoldási lehetőségek és kockázatok értékelése;
- a megvalósítási lépések és tesztelési stratégia megtervezése;
- a szükséges agent-, skill-, backend- és eszközigény felmérése;
- a várható komplexitás, fogyasztás és scope-kockázatok jelzése.

A tervezéshez használhat kész skilleket és delegált kutató- vagy elemzőagenteket.

**Ebben a szakaszban nincs implementáció.** A tervkészítésre vonatkozó írásvédelmet és jóváhagyási határt ténylegesen érvényesíteni kell, nem elég promptban kérni.

### 4. Emberi tervjóváhagyás

A felhasználó ellenőrzi a technikai tervet, és elfogadja, módosíttatja vagy elutasítja.

Elutasított vagy nem jóváhagyott tervből nincs automatikus végrehajtás.

#### Opcionális kétlépcsős tervezés

Komplex vagy magas kockázatú feladatnál:

1. **Architekturális terv:** megoldási irány, fő döntések, függőségek, kockázatok, feladatbontás.
2. **Részletes implementációs terv:** konkrét lépések, fájlok, interfészek, tesztek, delegálás.

A két szint külön jóváhagyható. Egyszerű feladatnál nem erőltetjük a második tervet.

#### Scope-bontás

Ha a repository-feltárás során kiderül, hogy az Issue túl nagy, az orchestrator javasoljon kisebb, önállóan ellenőrizhető Issue-kat.

A bontást és a megváltozott scope-ot a felhasználó hagyja jóvá.

### 5. Intelligens implementáció

A Kiro Crew a jóváhagyott terv szerint koordinálja a végrehajtást.

Feladatonként a megfelelő kombinációt választja:

| Döntés | Kiválasztási szempont |
| --- | --- |
| **Backend** | Kiro, Codex vagy más igazoltan támogatott backend; natív képességek és hozzáférés |
| **Agent/agentprofil** | Feladatkör, specializáció, jogosultság |
| **Modell** | Komplexitás, kockázat, minőség, várható erőforrásigény |
| **Reasoning effort** | A feladat nehézsége és a szükséges gondolkodási mélység |
| **Skill** | Feladathoz illő, meglévő és kompatibilis képesség |
| **Tool** | A végrehajtáshoz szükséges natív eszközök |
| **Kontextus** | Issue, jóváhagyott terv, releváns fájlok, kötelező szabályok |

A cél az **automatikus, ellenőrizhető választás**, nem a felhasználó által kézzel kiosztott állandó modell- és agentlista.

Az első működő konfigurációban az alacsony párhuzamosság és a kontrollálható delegálás az előnyös. Később mérés alapján növelhető.

A munka izolált branchben vagy worktree-ben történjen. A natív coding eszközök használata nem jelenthet korlátlan fájl-, hálózati vagy GitHub-jogosultságot.

### 6. Teszt és független review

Az implementáció után:

1. Releváns automatizált tesztek és determinisztikus ellenőrzések futnak.
2. A tényleges Git diff és a jóváhagyott terv összevetése megtörténik.
3. A megvalósítótól elkülönülő reviewer vizsgálja a kódot és a tesztbizonyítékokat.
4. A reviewer megállapításai alapján szükség esetén korlátozott javítás és újratesztelés történik.
5. A kötelező CI-kapuknak teljesülniük kell.

A reviewer nem tekintheti bizonyítéknak pusztán az implementáló saját állításait.

**Sikertelen vagy nem igazolt review esetén nincs automatikus „kész” állapot.**

A retry és replan korlátozott; ismétlődő hiba vagy lényeges scope-változás emberi döntést igényel.

### 7. PR, riport és zárás

A rendszer rövid, bizonyítékalapú riportot készít:

- mi változott, mely commitban vagy PR-ben;
- milyen tesztek futottak, milyen eredménnyel;
- mit állapított meg a független reviewer;
- teljesültek-e a kötelező CI-kapuk;
- mely backendek, modellek, agentek és skillek dolgoztak;
- milyen fogyasztási adatok érhetők el;
- milyen kockázatok vagy nyitott döntések maradtak.

A PR és a merge a repository-védelem szerint történik. **A merge külön emberi döntés.**

Az Issue-t és a GitHub Project státuszát a felhasználó a tényleges eredmények alapján kezeli.

### 8. Tapasztalatok visszacsatolása

A rendszer feladatonként gyűjtheti a routing, a fogyasztás és a minőség tapasztalatait.

A későbbi cél, hogy ezekből javuljon a backend-, modell-, effort- és skillválasztás.

**Az adatvezérelt, önmagát javító routing célállapot, nem jelenleg bizonyított automatikus funkció.**

### A teljes folyamat

**Ötlet → stratégiai terv → Issue → Kiro Crew PLAN → emberi jóváhagyás → opcionális részletes PLAN és jóváhagyás → intelligens IMPLEMENT → TEST → független REVIEW → PR/CI → emberi merge-döntés → tanulságok**

## 5. Kiro Crew-képességek, routing, költség és kontroll

### 5.1 A meglévő rendszerre építünk

A korábbi Kiro Crew 0.12.2-vizsgálatok alapján releváns építőelemek:

| Építőelem | Tervezett szerep | Igazoltság |
| --- | --- | --- |
| **Task Runner** | Tervezés, végrehajtás, feladatkövetés | Meglévő Crew-képesség; a teljes KovacsTrader-lánc nem igazolt |
| **Dynamic Workflows** | Ismételhető, többfázisú koordináció | Meglévő Crew-képesség; szükségességét PoC dönti el |
| **`spawn_run` / subagentek** | Elkülönített agentfuttatás és delegálás | Korábbi vizsgálatokban Kiro és Codex futott |
| **Agentprofilok** | Szerep- és jogosultságkonfiguráció | Konfigurálhatók; dinamikus end-to-end kiválasztás ellenőrzendő |
| **Skill discovery / search** | Kész skillek felfedezése és betöltése | Meglévő mechanizmus; tényleges automatikus alkalmazás ellenőrzendő |
| **Jev döntési mechanizmusok** | Modell- és skillválasztási döntések támogatása | Egyszerű routing ismert; tanuló optimalizálás nem igazolt |
| **Kontextuskezelés** | Szűk handoff, checkpoint és kompaktálás | Meglévő építőelemek; megfelelő integráció ellenőrzendő |
| **Usage ledger** | Fogyasztási adatok rögzítése | Részleges Kiro-kredit- és Codex-tokenadatok korábban látszottak |
| **Git/worktree és reviewer** | Izolált munka és ellenőrzés | Meglévő mechanizmusok; fail-closed viselkedés külön tesztelendő |

A Task Runner az elsőként vizsgálandó alap egyetlen Issue végigviteléhez. Dynamic Workflow-t csak akkor vezetünk be, ha a jóváhagyási kapuk, a delegálás vagy az ellenőrzés ezt ténylegesen igényli.

### 5.2 Kész skillek, agentek és workflow-k

A fejlesztési sorrend:

**Kiro Crew gyári képesség → konfiguráció → kompatibilis kész külső komponens → minimális adapter → saját kód kizárólag bizonyított hiány esetén.**

Feltérképezendő:

- beépített Crew-skillek, agentprofilok és workflow-k;
- meglévő Agent Skills-kompatibilis katalógusok;
- más rendszerekből átvehető kész fejlesztési módszertanok, agentprofilok és review-workflow-k;
- kész context engineering és repository-feltáró eszközök;
- használható modellrouting- és fogyasztásmérési komponensek;
- GitHub Issue-, PR-, CI- és review-integrációk.

Minden külső komponensnél ellenőrizni kell a konkrét átvehető fájlokat, licencet, verziót, kompatibilitást, jogosultságokat és a tényleges automatikus kiválasztást.

A nagy skillkatalógus önmagában nem eredmény: az a fontos, hogy a Crew megtalálja, kiválassza és a worker ténylegesen használja a megfelelő skillt.

**Nem készítünk előre saját specialist agentcsomagot vagy új orchestration engine-t.**

### 5.3 Natív eszközhasználat és jogosultságok

A korábbi szűk eszközmodell helyett a coding backendek saját, feladathoz szükséges natív eszközeit részesítjük előnyben.

A kontrollt nem az összes eszköz mesterséges letiltása, hanem a megfelelő rétegek biztosítják:

- izolált munkaterület és branch/worktree;
- backend natív sandbox- és permission mechanizmusai;
- feladatonként megengedett scope;
- kötelező emberi approval gate;
- teszt, független review, Git diff és CI;
- auditálható futási naplók és megállási feltételek.

**A promptbeli tiltás nem helyettesíti a technikai jogosultságvédelmet.**

Nincs automatikus merge, éles kereskedési művelet, deployment, jogosultságbővítés vagy CI-védelem kikapcsolása.

### 5.4 Kontextuskezelés

- Minden worker a szükséges Issue-t, jóváhagyott tervet, releváns fájlokat és szabályokat kapja.
- Nem másoljuk minden delegáláshoz a teljes repositoryt és chatelőzményt.
- A kötelező governance és elfogadási feltételek nem veszhetnek el kontextuscsökkentés közben.
- A handoff rövid, strukturált és ellenőrizhető.
- A Crew meglévő memória-, checkpoint- és kompaktálási mechanizmusait használjuk, ahol megfelelnek.

A cél nem a lehető legkisebb kontextus, hanem a **legkisebb elégséges kontextus**.

### 5.5 Modell, effort és routing

Az orchestrator célállapotban automatikusan választ, de a választás ellenőrizhető legyen.

Rögzítendő, ahol technikailag elérhető:

- kért és tényleges backend;
- kért és tényleges modell;
- kért és tényleges reasoning effort;
- kiválasztott agentprofil és skillek;
- routingdöntés indoka;
- eredmény, idő, retry és fogyasztás.

Korábbi vizsgálatban a kért alacsony effort nem minden esetben érvényesült. Ezért **a kért beállítás nem tekinthető automatikusan ténylegesen alkalmazottnak**.

A meglévő modellrouting kezdetben egyszerű, ellenőrizhető szabályokkal használható. A minőség- és költségadatokból tanuló routing csak későbbi fejlesztési cél.

### 5.6 Fogyasztás és költség

A teljes feladatot mérjük: tervezés, delegált kutatás, implementáció, teszt, review, retry és replan.

| Mérőszám | Értelmezés |
| --- | --- |
| **Kiro-kreditek** | Kiro elszámolt fogyasztása |
| **Codex-tokenek** | Input, output és cache-használat, ahol elérhető |
| **Copilot-kvóta** | Csak igazolt backend- és adatforrás-integráció után |
| **Idő** | Teljes futási és várakozási idő |
| **Retry / replan** | Sikertelen és megismételt próbálkozások |
| **Minőség** | Tesztek, review, elfogadási feltételek és regressziók |
| **USD-költség** | Csak ellenőrizhető árazásból számítható becslés vagy tényleges díj |

**Az ismeretlen pénzügyi költség nem nulla költség.** Kiro-kreditet, Codex-tokent és előfizetéses kvótát nem vonunk össze bizonyítatlan árfolyamon.

A cél az **elfogadott, tesztelt és review-zott feladatra jutó teljes erőforrásigény** javítása.

Kezdetben usage-riport és szabályalapú routing elegendő. Egységes providerközi hard budget és adaptív optimalizálás nincs igazolva.

### 5.7 Megállási feltételek

- Nincs implementáció jóváhagyott terv nélkül.
- Nincs önkényes scope-bővítés.
- A delegálási és retry-láncok korlátozottak.
- A review-hiba vagy hiányzó bizonyíték nem válhat automatikus sikerré.
- Sikertelen kötelező CI mellett nincs merge.
- A költségkeret és a jogosultsági korlát tényleges érvényesítését tesztelni kell.
- Bizonytalan, ismételten sikertelen vagy magas kockázatú helyzetben emberi döntés szükséges.

## 6. GitHub Issue-k, állapotok és repository-védelem

A **KovacsTrader GitHub-repository a kötelező nyilvántartás** az Issue-khoz, PR-ekhez, mérföldkövekhez, teszt-/review-bizonyítékokhoz.

A chat a stratégiai egyeztetés helye, nem a megvalósítás állapotának bizonyítéka.

Az alábbi repository-specifikus részletek a **2026-11-14-i állapotfelvételből** származnak; végrehajtás előtt aktuálisan ellenőrizendők.

### 6.1 Meglévő Issue-rendszer és labelek

A repositoryban meglévő Issue Form sablonok:

- `architecture.yml`
- `bug.yml`
- `feature.yml`
- `validation.yml`
- `config.yml` – sablonválasztási konfiguráció

A `KOVACS:ISSUE` során ezekhez és a meglévő taxonomiához igazodunk. Nem hozunk létre párhuzamos Issue-formátumot.

A sablon technikai mezőit a stratégiai szakaszban csak igazolt információval töltjük ki.

A `sync-labels.yml` és `label-taxonomy-report.json` alapján használt **17 label**:

| Kategória | Használt labelek | Használat |
| --- | --- | --- |
| **Típus** | `type:bug`, `type:feature`, `type:architecture`, `type:validation` | A feladat jellege |
| **Terület** | `area:data`, `area:features`, `area:selector`, `area:strategy`, `area:risk`, `area:execution`, `area:nautilus`, `area:operations`, `area:governance` | Érintett komponens |
| **Kockázat** | `risk:low`, `risk:medium`, `risk:high`, `risk:live-trading` | Hatás és ellenőrzési igény |

A státuszt **nem GitHub-labelek**, hanem a [Quant Trader GitHub Project](https://github.com/users/Zsombor0918/projects/1) `Status` mezője jelöli.

| Project `Status` | Projektleírás | Munkafolyamatbeli értelmezés |
| --- | --- | --- |
| **BackLog** | Not started yet. | Még nem indult el |
| **AI planning** | Plan changes with AI agent. | Technikai tervezés |
| **In Progress** | This is actively being worked on. | Jóváhagyott végrehajtás |
| **Testing** | Test before merging. | Tesztelés és független review |
| **Done** | This has been completed, ready to merge! | Merge-re előkészített; nem feltétlenül mergelt |
| **Blocked** | Unable to continue! | Hiba, függőség vagy döntés hiánya |

**A Project-státuszt a felhasználó kezeli.** Automatikus módosítása külön döntés.

A GitHub Issue `open`/`closed` állapota, a Project `Status` és a `docs/PROJECT_STATUS.md` `implemented`, `tested`, `validated`, `experimental`, `planned`, `deferred` kategóriái külön fogalmak.

A korábbi állapotfelvétel szerint a `sync-labels.yml` négy régi státuszlabel-definíciót még tartalmazott. Ezeket a workflow nem használja; tényleges kivezetésük külön repository-változtatás.

A meglévő Milestone- és Issue-függőségek megmaradnak.

### 6.2 Kötelező GitHub merge-védelem: Repo Audit

A 2026-11-14-i ellenőrzés szerint a [Repo Audit ruleset](https://github.com/Zsombor0918/KovacsTrader/rules/19214649) (ID `19214649`) aktív volt a `main` ágon, bypass actor nélkül.

A rögzített feltételek:

- `main`-be csak Pull Requesten keresztül kerülhet változtatás;
- tiltott a force-push és a nem megengedett branchtörlés;
- a review threadeknek lezártnak kell lenniük;
- kötelező, friss, sikeres státuszellenőrzések: `check`, `audit`, `scan`;
- a strict ellenőrzés miatt a PR-nek a célághoz képest naprakésznek kell lennie.

A ruleset a korábbi ellenőrzéskor **0 kötelező jóváhagyó review-t** kért. Ettől függetlenül a **független reviewer és a tulajdonosi jóváhagyás** a KovacsTrader munkafolyamatának saját kötelező szabályai (`AGENTS.md`, `docs/AI_WORKFLOW.md`).

A Kiro Crew nem gyengítheti vagy kerülheti meg a repository-védelmet. Az agent „kész” állítása nem helyettesíti a megfelelő commiton sikeres CI-t.

### 6.3 Folder- és dokumentációs struktúra

A [`docs/REPOSITORY_STRUCTURE.md`](https://github.com/Zsombor0918/KovacsTrader/blob/main/docs/REPOSITORY_STRUCTURE.md) a kötelező folder/package contract.

Kapcsolódó szabályozás:

- `AGENTS.md`
- `docs/AI_WORKFLOW.md`
- `tests/architecture/`
- `tools/audit_change_compliance.py`
- `CHANGELOG.md`
- `docs/CHANGE_AUDIT.md`
- `docs/PROJECT_STATUS.md`

Új top-level Python package vagy új dokumentációs contract csak `docs/REPOSITORY_STRUCTURE.md` **Amendment Log** bejegyzéssel és megfelelő architektúrateszt-módosítással vezethető be.

Strukturális vagy érdemi módosításnál a kapcsolódó dokumentációs, changelog- és auditkötelezettségek megmaradnak. A meglévő auditbejegyzések utólag nem írhatók át.

A tiltott import- és réteghatárokat a repository tesztjei védik. **Kötelező CI nélkül nincs merge.**

A Kiro Crew által generált tartós implementációs tervek helye és életciklusa még nincs eldöntve. Új dokumentumtípus bevezetésekor a struktúraszerződést szabályosan módosítjuk, nem oldjuk fel a gate-eket.

### 6.4 Bizonyítékok és hivatkozási helyek

- **GitHub Issue / Milestone / Project:** cél, prioritás, függőség, feladatstátusz.
- **Kiro Crew terv és futási napló:** technikai terv, delegálás, végrehajtási események.
- **GitHub PR:** diff, commit SHA, CI, review és merge-döntés.
- **Repository-dokumentáció:** architektúra, kontraktusok, validáció, változásaudit, igazoltság.
- **ChatGPT-chat:** stratégiai tanácsadás, nem az egyetlen igazságforrás.

„Elkészült”, „pusholva van”, „tesztelt”, „validált” vagy „működik az agent/tool” csak ellenőrzött bizonyítékkal állítható.

**Források:** [Issue sablonok](https://github.com/Zsombor0918/KovacsTrader/tree/main/.github/ISSUE_TEMPLATE), [label szabályozás](https://github.com/Zsombor0918/KovacsTrader/blob/main/.github/workflows/sync-labels.yml), [architektúra-szerződés](https://github.com/Zsombor0918/KovacsTrader/blob/main/docs/REPOSITORY_STRUCTURE.md), [CI](https://github.com/Zsombor0918/KovacsTrader/blob/main/.github/workflows/ci.yml), [governance](https://github.com/Zsombor0918/KovacsTrader/blob/main/AGENTS.md).

## 7. Bevezetés, PoC és nyitott kérdések

### 7.1 Első prioritás: meglévő képességek tényleges összekapcsolása

A cél **nem** új orchestrator, új agentframework vagy saját, nagyméretű skillcsomag írása.

Elsőként a telepített Kiro Crew képességeit és a kompatibilis kész komponenseket kell megvizsgálni.

Az eredmény minden vizsgált elemnél:

**Készen működik / konfigurálható / kész komponenssel integrálható / minimális adapter kell / nem igazolt / nem támogatott.**

A döntést konkrét konfiguráció, forráskód, futási napló vagy PoC-bizonyíték támassza alá.

### 7.2 Egyetlen valódi GitHub Issue PoC

Egy kicsi, alacsony kockázatú, önálló Issue-n végigpróbáljuk:

**Issue → PLAN → emberi jóváhagyás → Kiro/Codex delegálás → IMPLEMENT → TEST → független REVIEW → CI → riport.**

Külön vizsgálandó:

- [ ] A terv tényleges repository-feltáráson alapul.
- [ ] Jóváhagyás előtt nincs implementáció vagy jogosulatlan írás.
- [ ] Az opcionális második terv és scope-bontás szükség esetén megállíthatja a munkát.
- [ ] A Crew képes kész skillt felfedezni, kiválasztani és ténylegesen alkalmazni.
- [ ] A Kiro → Codex → Kiro delegálás ellenőrizhető.
- [ ] A backend, modell és effort kért és tényleges értéke ellenőrizhető, ahol támogatott.
- [ ] A coding backend natív eszközei használhatók a jóváhagyott határokon belül.
- [ ] A kontextus célzott, és nem vesznek el a kötelező szabályok.
- [ ] A tesztek reprodukálhatóan lefutnak.
- [ ] A független reviewer a tényleges diffet vizsgálja.
- [ ] A review- vagy CI-hiba nem eredményez hamis sikert.
- [ ] A fogyasztási és időadatok visszakereshetők; az ismeretlen költség nem nulla.
- [ ] Nincs automatikus merge vagy engedély nélküli GitHub Project-státuszmódosítás.

Az eredményeket **működött / részben működött / nem működött / nem tesztelt** kategóriákban rögzítjük.

### 7.3 Minimális saját fejlesztés

**Cél: nulla saját orchestrator-kód.**

Első körben csak a szükséges Crew-konfigurációt, meglévő agentprofilok és skillek használatát, jóváhagyási szabályokat és tesztparancsokat állítjuk össze.

Csak bizonyított hiány esetén készülhet:

- vékony routing- vagy backendadapter;
- egyszerű, csak olvasó usage-riport;
- minimális GitHub-összekötő;
- indokolt egyedi Dynamic Workflow.

Egyetlen PoC nem bizonyítja automatikusan a teljes adaptív optimalizálást vagy minden backend kompatibilitását.

### 7.4 Fokozatos fejlesztési sorrend

1. **Kontrollált alapfolyamat:** Issue, terv, approval, implementáció, teszt, review, riport.
2. **Dinamikus többbackend-delegálás:** Kiro/Codex, agentprofil, skill, modell, effort és kontextus kiválasztása.
3. **Fogyasztás és minőség mérése:** teljes feladatra vetített, auditálható eredmények.
4. **Adatvezérelt optimalizálás:** routing és effort fokozatos javítása.
5. **További integrációk:** új backendek és kész skillek csak bizonyított érték esetén.

Minden fázis külön értékelhető. A következő fázis nem indul automatikusan.

### 7.5 Nyitott kérdések

- A telepített Kiro Crew-verzió pontos képességei és korlátai.
- A Task Runner önmagában elég-e, vagy Dynamic Workflow szükséges.
- Az automatikus skill-, agent-, backend-, modell- és effortválasztás tényleges lánca.
- A natív toolok és a sandboxjogosultságok megőrzése delegáláskor.
- A kétirányú Kiro/Codex handoff megbízhatósága.
- A reviewer fail-closed működése.
- A fogyasztásmérés és a providerközi költségkorlátok.
- A kész külső agent- és skillcsomagok kompatibilitása.
- A technikai tervek tartós repository-helye.
- A GitHub Project-státuszok opcionális későbbi automatizálása.

**Mostani prioritás:** a Kiro Crew és a kész komponensek tényleges képességeinek ellenőrzése, majd egyetlen valódi Issue PoC. Nem új saját orchestrator fejlesztése.

## 8. Gyors használat

- Rövid megbeszélés: „Szerintem az M2-nél ezt kellene változtatni…”
- Mélyebb ötletelés: `KOVACS:EXPLORE – vessük össze a megoldásokat.`
- Issue-tervezet: `KOVACS:ISSUE – a megbeszélt tervből készíts issue-tervezetet.`
- Műszaki tervezés, ha a Crew-integráció igazolt: `KOVACS:PLAN [GitHub Issue URL]`.

### Referenciák

- [Kiro Crew GitHub](https://github.com/kirodotdev/KiroCrew)
- [KovacsTrader repository](https://github.com/Zsombor0918/KovacsTrader)
- [Quant Trader GitHub Project](https://github.com/users/Zsombor0918/projects/1)
- [Repository-struktúra](https://github.com/Zsombor0918/KovacsTrader/blob/main/docs/REPOSITORY_STRUCTURE.md)
- [Repository-governance](https://github.com/Zsombor0918/KovacsTrader/blob/main/AGENTS.md)

---

**Változtatási elv:** a workflow szolgálja a fejlesztést, ne fordítva. A kész képességeket használjuk, a működést bizonyítjuk, a fölösleges komplexitást elhagyjuk.
