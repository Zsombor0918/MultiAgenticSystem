# Kiro Crew 0.13.0 upgrade

2026-11-21. **Installed; startup blocked by doctor pending skill synchronization.** The user requested stable 0.13.0 and preservation of configuration, credentials, Studio, CrewLab and workflow state. The prior trial remains paused.

The [official stable release](https://github.com/kirodotdev/KiroCrew/releases/tag/v0.13.0) is not a prerelease. The [official installer](https://github.com/kirodotdev/KiroCrew/blob/v0.13.0/docs/guides/install.md) was run with `KIROCREW_HOME` and `KIROCREW_VENV` pointing to this repository's existing paths and `--version 0.13.0 --channel stable --system-python --no-kas`. Its signed manifest and wheel SHA-256 verification passed; installer exit 0. No upstream code was patched.

Before installation, private ignored backups were created under `.runtime/upgrades/0.13.0/backup/` for the Crew data home, CrewLab, previous venv, generated Kiro agents and CLI symlink. Keep these private: they contain credentials and session data. CrewLab matched its backup, and checksums for Studio's 1,791 installed files, session files, trust, usage and the checked workflow directories matched their backups after installation. Config comparison found only `agent.kas_bundle` added and `meta.lastTouchedAt`/`meta.lastTouchedVersion` changed; `config.local.json` and `folders.json` were unchanged. These are bounded checks, not proof of every external credential or project file.

## Non-model checks

- Installed version reports 0.13.0. Doctor reports the KAS route as `kiro-cli acp --agent-engine v3 --auth-method cli`; CLI 2.37.0 is newer than the versions in Crew's verified tool-name table.
- Studio 2.0.1 remains installed and enabled with existing grants. Its live backend, Bun inside extension sessions, and the full planning flow are not verified under 0.13.0.
- The native implementation described in [PR #33578](https://github.com/kirodotdev/KiroCrew/pull/33578) exists in the installed version, including its consent routes and KAS spec hook integration. Read-only calls to `hooks_enabled` report off with no recorded Crew choice or Kiro CLI trust for this repo, CrewLab and the prepared fixture. No consent was changed and no hook was executed. The UI notice, consent change, protected execution and gate behavior remain untested live. Crew's explicit on/off takes precedence over Kiro CLI workspace trust; without either, hooks stay off. This applies to folder agent spec hooks, not standalone `.kiro/hooks/*.json` files, and cron excludes project hooks. The PR notes that the Kiro CLI trust file itself is not fenced by Crew.
- Doctor exited **1**: 20 installed builtin skills differ from the selected 0.13.0 source; 23 match. The real launcher stops on this failure. Doctor recommends restarting to run native skill sync, and moving a persistently stale installed skill out of the skills directory only if necessary after restart. The repository's doctor-before-gateway startup creates a circular dependency: native sync normally runs at gateway startup. No skill was moved, overwritten or suppressed, no substitute gateway was started, and the live trial has not resumed.

## Next decision

Investigate the supported native skill synchronization mechanism and its effect on user edits, then agree a safe recovery path before retrying the trial. Do not bypass doctor or security checks. Confirm Studio backend health, project hook consent and the normal VS Code task after the blocker is resolved. Original backups and local test evidence remain in ignored runtime paths.
