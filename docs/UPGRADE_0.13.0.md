# Kiro Crew 0.13.0 upgrade

2026-11-21. **Local AI-DLC reset completed with the gateway stopped.** The next VS Code task start will verify the live dashboard after the reset.

Crew's native controls first closed 15 tabs and cleared 17 conversations. After a restart, the Crew sessions and slots APIs both returned zero and Studio reported healthy with 373 payload files and Bun available. Two visible Studio cards persisted because AI-DLC workflow state survives conversation deletion. Studio's archive attempt returned HTTP 409 for an uncertain delivery. Reconcile from disk left the delivery uncertain.

The user then authorized direct local deletion. With the gateway stopped, both untracked CrewLab intent directories, their intent registry, active cursor and session bindings were removed. The offline Studio database reset cleared 9 actions, 12 action transitions, 2 intent bindings and 62 activity records. Integrity and foreign key checks passed. The CrewLab registration, harness installation receipt, install transaction and Studio preferences matched their pre-reset values.

Remaining saved Crew transcripts and tab/session pointers were removed, along with obsolete backups, the unused virtual environment and old pilot files. CrewLab's Git HEAD was still `5871c68`. Kiro and Codex sign-in checks passed, and Crew and Bun still report 0.13.0 and 1.4.4. Post-reset Crew doctor exited 0 and confirmed the V3 relay. The offline counts were zero CrewLab intent entries, saved Crew transcripts, Studio actions and Studio intent bindings. No AI session was started.

The [official stable release](https://github.com/kirodotdev/KiroCrew/releases/tag/v0.13.0) is not a prerelease. The [official installer](https://github.com/kirodotdev/KiroCrew/blob/v0.13.0/docs/guides/install.md) was run with `KIROCREW_HOME` and `KIROCREW_VENV` pointing to this repository's existing paths and `--version 0.13.0 --channel stable --system-python --no-kas`. Its signed manifest and wheel SHA-256 verification passed; installer exit 0. No upstream code was patched.

At installation time the checked CrewLab, Studio, session, trust and usage files matched their pre-upgrade snapshots. The config comparison found the installer added `agent.kas_bundle` and updated two version and timestamp metadata fields. The temporary snapshots were subsequently removed during cleanup.

## Non-model checks

- Installed version reports 0.13.0. Doctor reports the KAS route as `kiro-cli acp --agent-engine v3 --auth-method cli`; CLI 2.37.0 is newer than the versions in Crew's verified tool-name table.
- Studio 2.0.1 remains installed and enabled with existing grants. Gateway and Studio health passed before the final offline reset. Bun inside model sessions and the full planning flow remain unverified.
- The native implementation described in [PR #33578](https://github.com/kirodotdev/KiroCrew/pull/33578) exists in the installed version, including its consent routes and KAS spec hook integration. Read-only calls to `hooks_enabled` report off with no recorded Crew choice or Kiro CLI trust for this repo, CrewLab and the prepared fixture. No consent was changed and no hook was executed. The UI notice, consent change, protected execution and gate behavior remain untested live. Crew's explicit on/off takes precedence over Kiro CLI workspace trust; without either, hooks stay off. This applies to folder agent spec hooks, not standalone `.kiro/hooks/*.json` files, and cron excludes project hooks. The PR notes that the Kiro CLI trust file itself is not fenced by Crew.
- The initial doctor run failed on 20 stale built-in skills. Crew's native `SkillsLoader.sync_builtins()` resolved the mismatch without setting aside user skills. Doctor then exited 0 and reported all 43 installed built-in skills current.

## Remaining work

Start the gateway through **Kiro Crew: Start** and verify that Studio shows zero old intents and actions. Verify CrewLab's native hook consent before starting the next planning trial.
