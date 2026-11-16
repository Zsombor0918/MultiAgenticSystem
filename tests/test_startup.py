"""Exercise the real launcher without authentication, a gateway, or model calls."""

import json
import os
from pathlib import Path
import shutil
import socket
import subprocess
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]


class StartupTest(unittest.TestCase):
    def run_launcher(self, doctor_exit):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "scripts").mkdir()
            shutil.copy2(ROOT / "scripts/start-kirocrew.sh", root / "scripts")
            home = root / ".runtime/kirocrew"
            home.mkdir(parents=True)
            (home / ".demo-setup-confirmed").touch()
            binaries = root / ".runtime/kirocrew-venv/bin"
            binaries.mkdir(parents=True)
            bun = root / ".runtime/pilots/aidlc-studio-2.0.1/bun/bin/bun"
            bun.parent.mkdir(parents=True)
            events = root / "gateway-events"
            scripts = {
                "kiro-cli": 'case "$1" in whoami) exit 0;; acp) echo v3;; esac',
                "codex": "exit 0",
                "kirocrew": (
                    'case "$1" in doctor) exit "$PILOT_DOCTOR_EXIT";; '
                    'gateway) printf "%s\\n" "$*" > "$PILOT_EVENTS"; '
                    'command -v bun >> "$PILOT_EVENTS";; *) exit 99;; esac'
                ),
            }
            for name, body in scripts.items():
                path = binaries / name
                path.write_text("#!/usr/bin/env bash\n" + body + "\n")
                path.chmod(0o755)
            bun.write_text("#!/usr/bin/env bash\nexit 0\n")
            bun.chmod(0o755)
            with socket.socket() as sock:
                sock.bind(("127.0.0.1", 0))
                port = sock.getsockname()[1]
            env = dict(os.environ, PATH=f"{binaries}:{os.environ['PATH']}",
                       PILOT_DOCTOR_EXIT=str(doctor_exit), PILOT_EVENTS=str(events),
                       KIROCREW_PORT=str(port))
            result = subprocess.run(["bash", str(root / "scripts/start-kirocrew.sh")],
                                    env=env, capture_output=True, text=True, timeout=10)
            return result, events.read_text() if events.exists() else "", str(bun)

    def test_failed_doctor_never_launches_gateway(self):
        result, events, _ = self.run_launcher(23)
        self.assertEqual(result.returncode, 23, result.stderr)
        self.assertEqual(events, "")

    def test_success_uses_local_bun_and_existing_gateway_options(self):
        result, events, bun = self.run_launcher(0)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(events.splitlines(), ["gateway --no-open --approval interactive", bun])

    def test_vscode_task_keeps_the_single_launcher(self):
        tasks = json.loads((ROOT / ".vscode/tasks.json").read_text())["tasks"]
        start = [task for task in tasks if task["label"] == "Kiro Crew: Start"]
        self.assertEqual(len(start), 1)
        self.assertEqual(start[0]["command"], "bash")
        self.assertEqual(start[0]["args"], ["${workspaceFolder}/scripts/start-kirocrew.sh"])


if __name__ == "__main__":
    unittest.main()
