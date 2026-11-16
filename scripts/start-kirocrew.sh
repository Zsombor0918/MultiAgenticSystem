#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/.."
root="$PWD"
export KIROCREW_HOME="$root/.runtime/kirocrew"
export KIROCREW_PORT="${KIROCREW_PORT:-5476}"
# A nem létező saját modell útvonal a dokumentált fail-closed viselkedéssel
# kihagyja az alap embeddingmodell letöltését; csak kulcsszavas keresés lesz.
export KIROCREW_EMBED_MODEL_PATH="${KIROCREW_EMBED_MODEL_PATH:-$root/.runtime/no-embedding-model.gguf}"
export CODEX_PATH="$(command -v codex || true)"
# Keep the Studio pilot's pinned Bun local and available through the same start task.
export PATH="$root/.runtime/pilots/aidlc-studio-2.0.1/bun/bin:$root/.runtime/node-v24.22.3-linux-x64/bin:$root/.runtime/kirocrew-venv/bin:$root/.runtime/codex-adapter/node_modules/.bin:$PATH"

if ! command -v kirocrew >/dev/null; then
  cat <<'MSG'
A Kiro Crew nincs telepítve. Telepítés csak külön jóváhagyás után.
A docs/history/SETUP_AND_DELEGATION.md tartalmazza a korábbi, 0.12.2-re rögzített telepítést;
nem kell forráskódot vagy dashboardot fordítani.
MSG
  exit 1
fi
for cmd in python3 kiro-cli codex; do
  if ! command -v "$cmd" >/dev/null; then
    printf 'Hiányzik: %s. Lásd docs/history/SETUP_AND_DELEGATION.md.\n' "$cmd" >&2; exit 1
  fi
done
if ! kiro-cli whoami >/dev/null 2>&1; then
  printf 'Kiro belépés szükséges: futtasd: kiro-cli login\n'; exit 1
fi
if ! codex login status >/dev/null 2>&1; then
  printf 'Codex belépés szükséges: futtasd: codex login\n'; exit 1
fi
if ! kiro-cli acp --help | grep -q 'v3'; then
  printf 'A Kiro CLI ACP súgójában nincs V3; ellenőrizd/frissítsd a CLI-t.\n'; exit 1
fi
if ! python3 - "$KIROCREW_PORT" <<'PY'
import socket, sys
try:
    port = int(sys.argv[1])
    if not 1 <= port <= 65535:
        raise ValueError('port outside 1..65535')
    with socket.socket() as sock:
        sock.bind(('127.0.0.1', port))
except (OSError, ValueError) as exc:
    print(f'A port nem használható: {exc}. Adj meg másik KIROCREW_PORT értéket.', file=sys.stderr)
    sys.exit(1)
PY
then exit 1; fi

if [ ! -f "$KIROCREW_HOME/.demo-setup-confirmed" ]; then
  cat <<MSG
Az első setup és gateway indítás módosíthatja a ~/.kiro/agents/kirocrew.json és
~/.kiro/settings/mcp.json fájlt; régi generált skillt is eltávolíthat, és
~/.local/bin/kirocrew parancsot kezelhet. A setup a globális MCP-t tisztíthatja.
Állítsd a setup workspace-kérdését erre: $root
A sandbox kikapcsolásához NE adj hozzájárulást. A beépített KAS-re ne válts.
A setup csak akkor indul, ha külön jóváhagyod az otthoni módosításait.
MSG
  read -r -p 'Jóváhagyod a fenti setup módosításokat és a mentést? [i/N] ' reply
  [[ "$reply" == i || "$reply" == I ]] || exit 1
  mkdir -p "$KIROCREW_HOME/backups"
  backup="$KIROCREW_HOME/backups/$(date +%Y%m%d-%H%M%S)-$$"
  mkdir -m 700 "$backup"
  for path in "$HOME/.kiro/agents/kirocrew.json" "$HOME/.kiro/settings/mcp.json" "$HOME/.local/bin/kirocrew"; do
    if [ -e "$path" ] || [ -L "$path" ]; then
      name="$(basename "$(dirname "$path")")-$(basename "$path")"
      cp -a -- "$path" "$backup/$name"
    fi
  done
  printf 'Mentés: %s\n' "$backup"
  kirocrew setup
  printf 'Csak akkor folytasd, ha a setup teljesen lefutott.\n'
  read -r -p 'Sikeres volt és a workspace a fenti könyvtár? [i/N] ' reply
  [[ "$reply" == i || "$reply" == I ]] || exit 1
  [ -f "$KIROCREW_HOME/config.json" ] || { echo 'Nincs config.json; a setup nem igazolható.'; exit 1; }
  touch "$KIROCREW_HOME/.demo-setup-confirmed"
fi
printf '\nKiro Crew diagnosztika (a KAS route és Codex sorokat ellenőrizd):\n'
kirocrew doctor
printf '\nDashboard: http://localhost:%s\nLeállítás: Ctrl+C ebben a terminálban.\n' "$KIROCREW_PORT"
printf 'Kizárólag akkor kezdj Kiro-próbát, ha a doctor V3 CLI relay útvonalat jelez.\n'
printf 'Ha a dashboard bejelentkezést kér, másik terminálban: KIROCREW_HOME="%s" kirocrew token\n' "$KIROCREW_HOME"
exec kirocrew gateway --no-open --approval interactive > >(trap '' INT; cat)
