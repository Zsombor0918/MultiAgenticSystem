> Historical local setup from November 2026. Run commands from the repository root and verify versions and account state before use. The artifact check depends on ignored local run files and will not pass on a fresh clone without rerunning the documented tests.

# Kiro Crew delegálási teszt

Ez a workspace önálló próba; nem használja a KovacsTrader projektet. Az AI-próbák
csak a dashboardon, kézi indításra futnak. A teljes tesztet lásd:
[TEST_GUIDE.md](TEST_GUIDE.md); az aktuális állapotot: [RESULTS.md](RESULTS.md).

## Ellenőrzött környezet

WSL2 Ubuntu 24.04, Python 3.12.3, Kiro CLI 2.37.0 (Builder ID belépés,
ACP V3 szerepel a súgóban), Codex CLI 0.166.0 (ChatGPT belépés), Node 24.22.3 a projektben (a rendszer Node 18.19.1), npm 9.2.0. A vizsgálatkor kb. 13 GiB szabadon rendelkezésre álló memória volt,
a 5476-os porton nem volt hallgató. A Kiro Crew 0.12.2 és a Codex ACP 1.11.0 települt a `.runtime` könyvtárba.
A belépések később lejárhatnak. A Node 24.22.3 lokális telepítését követően a Crew megtalálja a Codex ACP adaptert; a hitelesített Codex session még nincs igazolva. A kész Crew wheel nem igényel Node-ot frontend-fordításhoz; az
adapterhez viszont Node kell.

## Telepítés — csak jóváhagyás után

A 2026-11-12-én kiadott **0.12.2** stabil verzióhoz készült. A hivatalos,
aláírt manifestet ellenőrző telepítő kész wheelből dolgozik, nem klónoz és nem
épít frontendet. A javasolt futtatás a VS Code terminálban:

```bash
export KIROCREW_HOME="$PWD/.runtime/kirocrew"
export KIROCREW_VENV="$PWD/.runtime/kirocrew-venv"
curl -fsSL https://download.crew.kiro.dev/cli.sh | sh -s -- --version 0.12.2 --system-python --no-kas
```

A telepítő a workspace-en belüli venv és adatkönyvtár mellett a
`~/.local/bin/kirocrew` hivatkozást is létrehozza vagy felülírhatja; egy meglévőt
előzetesen jóváhagyással menteni kell. `--no-kas` kihagyja a külön beépített KAS
csomagot, mivel itt a Kiro CLI V3 relay a cél. A telepítő csomagfüggőségeket és
cache-t is létrehozhat a szokásos felhasználói helyeken. Nem telepítünk szolgáltatást.

A Codex ACP adapter külön hivatalos csomag. A Crew kódja által megadott telepítés:

```bash
npm install --prefix "$PWD/.runtime/codex-adapter" @agentclientprotocol/codex-acp@1.11.0
```

Ezután indítás előtt a `CODEX_ACP_BIN` változóval meg kell adni a csomag tényleges
belépési pontját, ha a doctor nem találja meg; a pontos feloldást a telepített
verzióval kell igazolni. A script a lokális `.runtime/codex-adapter/node_modules/.bin`
könyvtárat is a PATH-ra teszi. A `CODEX_PATH` a meglévő `codex` parancsra mutat,
így az adapter azt használja a csomag saját Codex binárisa helyett. A Crew
sandboxának és a tényleges adapteres bejelentkezésnek a működése a doctor után is
külön próbát igényel. API-kulcsot nem kell megadni.

## Indítás

VS Code-ban WSL-ből nyisd meg ezt a mappát, majd `Ctrl+Shift+P` → **Tasks: Run
Task** → **Kiro Crew: Start**. Alternatíva: `bash scripts/start-kirocrew.sh`.
A script hiányzó szoftvert és bejelentkezést jelez. Első indításkor a setup már lefutott; új környezetben az interaktív setup előtt külön engedélyt kér és menti a felsorolt meglévő fájlokat. A setup
workspace-kérdésénél add meg a script által kiírt teljes útvonalat. Ne válaszd a
sandbox letiltását, felhőt, vagy a külön KAS-bejelentkezést. Sikertelen vagy
félbeszakadt setup után ne erősítsd meg a sikeres futást.

A setup a `~/.kiro/agents/kirocrew.json` agentfájlt létrehozhatja/összevonhatja,
a `~/.kiro/settings/mcp.json` bizonyos régi Crew MCP bejegyzéseit törölheti,
a `~/.local/bin/kirocrew` parancsot kezelheti, továbbá korábban generált, elavult
conductor skillt eltávolíthat. Az első gateway-indítás is végezhet ilyen MCP-tisztítást.
A KIROCREW_HOME nem szigeteli ezeket. Ha ilyen meglévő skill van, indítás előtt
külön mentést és döntést igényel. A Crew a saját adatait a `.runtime/kirocrew`
könyvtárba teszi, ezzel a régi `~/.kirocrew` migrációja kimarad.

A doctorban a **KAS backend / route** kifejezetten `kiro-cli acp --agent-engine v3`
útvonalat és CLI belépést mutasson; fallback vagy saját KAS-engine esetén állj meg.
A Codex sor mutassa a megtalált adaptert és a hibákat. A gateway előtérben marad:
`Ctrl+C` állítja le. Cím: <http://localhost:5476>. Foglalt port esetén válassz
másikat: `KIROCREW_PORT=5477 bash scripts/start-kirocrew.sh`; más folyamatot nem
állítunk le. A port előzetes ellenőrzése és a tényleges bind között felléphet ütközés.

A script a dokumentált `KIROCREW_EMBED_MODEL_PATH` változót egy nem létező
helyi fájlra állítja. A Crew ilyenkor nem tölti le az alapértelmezett kb. 610 MB-os
modellt; figyelmeztetést jelez, és a memória kulcsszavas keresésre áll át. Valódi
helyi GGUF megadható ugyanezzel a változóval. A delegáláshoz embedding nem szükséges.

**2026-11-16 correction:** this historical download-avoidance configuration makes
Crew 0.12.2's doctor fail with exit 1. The current launcher stops on that failure,
so this paragraph is not a working startup recommendation. See the
[actual failure and subsequently approved/applied correction](../STEP_1_RESULTS.md).

A telepítés után a doctor sikeresen igazolta a KAS `kiro-cli` V3 relay és a CLI
saját bejelentkezésének útvonalát; a 2.37-es CLI újabb a Crew által ellenőrzött
verzióknál. A gateway indítása és a dashboard HTTP 200 válasza külön ellenőrizve.
A dashboard belépési linkjéhez a gateway termináljának utasítását kövesd; a token
titkos. A doctor önjavítása egy korábban nem létező
`~/.kiro/agents/kirocrew.json` fájlt hozott létre. A script első setup előtt ezt
is menti és hozzájárulást kér.

Források: [0.12.2 telepítés](https://github.com/kirodotdev/KiroCrew/blob/v0.12.2/docs/guides/install.md),
[konfiguráció](https://github.com/kirodotdev/KiroCrew/blob/v0.12.2/src/kiro_crew/docs/configuration.md),
[subagents](https://github.com/kirodotdev/KiroCrew/blob/v0.12.2/src/kiro_crew/docs/subagents.md),
[agent host contract](https://github.com/kirodotdev/KiroCrew/blob/v0.12.2/docs/system-specs/modules/agent-host-contract.md).
