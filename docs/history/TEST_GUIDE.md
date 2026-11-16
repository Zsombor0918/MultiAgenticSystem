# Delegálási tesztek — kézi indítás

Minden modellhívás kreditet vagy előfizetéses keretet használhat; az ár a
kiválasztott modelltől és fióktól függ. A dashboard modellválasztójában válassz
elérhető, olcsó modellt; a Kiro kijelzett kredit-szorzóját és a Codex csomag
korlátait ellenőrizd. A teszt egy szülőt és egyszerre legfeljebb egy workert kér.
A setup és a gateway indítása nem futtatja ezeket a promptokat.

1. Kövesd a SETUP_AND_DELEGATION.md telepítési és indítási lépéseit; a dashboard címe
   <http://localhost:5476>. A doctor mutassa a CLI V3 relay útvonalat és a Codex
   adaptert. Ha a Codex telepítés után nem látszik, indítsd újra a gatewayt.
2. A dashboardon válassz ki vagy nyiss chatet ehhez a workspace-hez; ellenőrizd,
   hogy a projektkönyvtár ennek a mappának az abszolút útvonala. A konkrét chat-
   és harnessválasztó megjelenése a telepített dashboardon ellenőrzendő: a helyi
   felület a telepítés hiányában még nem volt kipróbálva.
3. A Settings → Agent Harness részen ellenőrizd a `kas`, majd a `codex` állapotát.
   Ha a backendválasztás előnézeti kapcsolót kér, Settings → Developer → Feature
   Previews alatt engedélyezd a felületen megnevezett kapcsolót. Botonkénti
   harnesshez a dokumentált kapcsoló **Agent harness per Bot**. Ne válts másik
   providerre. Szükség esetén új chatet/gatewayt indíts.
4. Minden próbánál hagyd jóvá a valóban szükséges fájl- és shellműveleteket;
   ne engedélyezz általános automatikus jóváhagyást. A futásazonosítót, látható
   backend nevét, eszközhívást, befejezési eseményt és artefaktumot rögzítsd a
   RESULTS.md-ben. Titkot ne másolj be.

## A — Kiro önállóan

Válassz `kas` chatet, és a doctorból győződj meg a `kiro-cli` V3 relay-ről.
Másold be:

```text
Olvasd el a demo/calculator.py fájlt a fájleszközöddel. Röviden mondd el,
mit csinál. Ne indíts alagentet és ne módosíts fájlokat.
```

Csak akkor PASS, ha látható a tényleges olvasási művelet és a helyes válasz,
valamint a session és a doctor együtt a KAS CLI V3 útvonalat igazolják.

## B — Kiro → Codex

A KAS chatben (a fenti ellenőrzés után) add ki:

```text
Ez kifejezett delegálási teszt. Hívd meg a Kiro Crew spawn_run MCP eszközt
pontosan egy workerrel, backend="codex" paraméterrel. A worker feladata:
hozzon létre a jelenlegi workspace demo/codex-result.txt fájljában pontosan
egy CODEX_WORKER_DONE sort, majd jelentse a tényleges eredményt. Ne végezd el
te a worker helyett. Várd meg a completion eventet, és számolj be a kapott
workerazonosítóról, backendről és eredményről. Ha nem sikerül, írd le a hibát.
```

A 0.12.2 [spawn_run dokumentációja](https://github.com/kirodotdev/KiroCrew/blob/v0.12.2/src/kiro_crew/docs/subagents.md)
szerint a `backend` támogatott, és hiányzó backendnél a kérés visszautasított.
Ellenőrizd a tényleges telepített verzióban is a hívás argumentumait, a Subagents
panel futását (`codex`), a worker eszközhívását, a parent beszélgetésbe érkező
completion eventet és a fájlt. Ha valamelyik hiányzik, ez nem bizonyított PASS.

## C — Codex → Kiro

Új chatben válassz `codex` harness-t; a V3 relay útvonalat továbbra is ellenőrizd.
A dokumentáció backend-paramétere alapján ez az irány elvben kérhető, de a Codex
session számára a Crew MCP elérhetőségét még nem teszteltük. Ha a tool hiányzik
vagy a backend nem indítható, jelöld BLOCKED/FAIL-ként; ne szimuláld.

```text
Ez kifejezett delegálási teszt. Hívd meg a Kiro Crew spawn_run MCP eszközt
pontosan egy workerrel, backend="kas" paraméterrel. A worker feladata:
hozzon létre a jelenlegi workspace demo/kiro-result.txt fájljában pontosan
egy KIRO_WORKER_DONE sort, majd jelentse a tényleges eredményt. Ne végezd el
te a worker helyett. Várd meg a completion eventet, és számolj be a kapott
workerazonosítóról, backendről és eredményről. Ha nem sikerül, írd le a hibát.
```

Ugyanúgy ellenőrizd a `kas` workert, a V3 route-ot, a műveletet, a fájlt és a
Codex parenthez visszaérkezett befejezési eseményt.

## D — natív képességek

Külön, kézzel kérd mindkét backendtől a `demo/calculator.py` olvasását és a
`python3 -m unittest discover -s demo` terminálparancs futtatását. A látható
eszközhívások alapján rögzítsd külön az olvasás és shell eredményét. Ezután
kérj egyetlen natív alagentet egy rövid, csak olvasó feladatra. Vizsgáld meg,
hogy valóban a natív subagent eszköz indult-e, vagy Crew `spawn_run`: a kettő
külön képesség. Kiro Crew koordinálja a `spawn_run` futtatást és completion
eseményt, míg a worker harness végzi saját fájl- és shellhívásait.

**LIMITATION:** a Crew host-contract a KAS natív `invoke_sub_agent` leképezését
leírja, de a Codex natív alagentjének Crew agent-spec `use_subagent` leképezése
hiányzóként szerepel. Ez nem bizonyítja, hogy minden Codex natív alagent funkció
ACP-n keresztül lehetetlen; tényleges próbáig ismeretlen. A Crew-delegálás nem
bizonyítja a natív alagentet.

## Artefaktumok ellenőrzése

Terminálban: `bash scripts/check-results.sh`. Az ellenőrző a projekt `demo/`
és a `.runtime/kirocrew/workspace/demo/` fájljait egyaránt megvizsgálja; a
második a Crew külön dashboard-workspace-e, tehát önmagában nem bizonyítja, hogy
az első könyvtárban történt munkavégzés. Új teszthez a dashboardon a projekt
gyökerét válaszd ki, és ellenőrizd a pontos abszolút célútvonalat.
A script nem hív modellt és nem
módosít fájlokat. A két fájl és pontos tartalmuk létezését ellenőrzi; önmagában
nem tudja igazolni a származást, backendet vagy completion eventet. A demo
Python-próbája: `python3 -m unittest discover -s demo`.
