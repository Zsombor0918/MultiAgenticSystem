#!/usr/bin/env bash
set -u
cd "$(dirname "${BASH_SOURCE[0]}")/.."
status=0
for entry in 'codex-result.txt:CODEX_WORKER_DONE' 'kiro-result.txt:KIRO_WORKER_DONE'; do
  name=${entry%%:*}; expected=${entry#*:}; found=0
  for dir in demo .runtime/kirocrew/workspace/demo; do
    file="$dir/$name"
    if [ -f "$file" ] && cmp -s "$file" <(printf '%s\n' "$expected"); then
      printf 'ARTIFACT PASS: %s pontos tartalma megfelelő\n' "$file"
      found=1
    elif [ -e "$file" ]; then
      printf 'ARTIFACT INVALID: %s tartalma eltér\n' "$file"
      status=1
    fi
  done
  if [ "$found" -eq 0 ]; then
    printf 'ARTIFACT MISSING: %s (egyik demo könyvtárban sincs megfelelő fájl)\n' "$name"
    status=1
  fi
done
printf 'A fájlok önmagukban nem bizonyítják a backendet, delegálást vagy eredmény visszaadását.\n'
exit "$status"
