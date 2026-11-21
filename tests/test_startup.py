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
    def run_launcher(self, doctor_exit, model_path=None, check_browser=False):
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
                    'case "$1" in doctor) '
                    '[ "${KIROCREW_EMBED_MODEL_PATH-}" = "$PILOT_MODEL_PATH" ] || exit 24; '
                    'exit "$PILOT_DOCTOR_EXIT";; '
                    'gateway) printf "%s\\n" "$*" > "$PILOT_EVENTS"; '
                    'command -v bun >> "$PILOT_EVENTS"; '
                    'if [ -n "$PILOT_FAKE_GATEWAY" ]; then exec python3 "$PILOT_FAKE_GATEWAY"; fi;; '
                    '*) exit 99;; esac'
                ),
                "powershell.exe": (
                    '[ -f "$PILOT_READY" ] || { echo "opened early" >> "$PILOT_EVENTS"; exit 1; }; '
                    'printf "%s\n" "$*" >> "$PILOT_EVENTS"'
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
                       PILOT_MODEL_PATH=model_path or "", KIROCREW_PORT=str(port),
                       PILOT_FAKE_GATEWAY="", WSL_DISTRO_NAME="startup-test")
            env.pop("KIROCREW_EMBED_MODEL_PATH", None)
            if model_path is not None:
                env["KIROCREW_EMBED_MODEL_PATH"] = model_path
            if check_browser:
                env["PILOT_READY"] = str(root / "ready")
                fake_gateway = root / "fake_gateway.py"
                env["PILOT_FAKE_GATEWAY"] = str(fake_gateway)
                fake_gateway.write_text("""
import os
import time
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path


class ReadyProbe(BaseHTTPRequestHandler):
    probes = 0

    def do_GET(self):
        assert self.path == '/api/ready'
        ReadyProbe.probes += 1
        if self.probes == 3:
            Path(os.environ['PILOT_READY']).touch()
        self.send_response(503 if self.probes == 2 else 200)
        self.end_headers()
        self.wfile.write(b'{"ready": false}' if self.probes == 1 else b'{"ready": true}')


with HTTPServer(('127.0.0.1', int(os.environ['KIROCREW_PORT'])), ReadyProbe) as server:
    server.timeout = 4
    for _ in range(3):
        server.handle_request()
    events = Path(os.environ['PILOT_EVENTS'])
    deadline = time.monotonic() + 2
    while len(events.read_text().splitlines()) == 2 and time.monotonic() < deadline:
        time.sleep(0.02)
""")
            result = subprocess.run(["bash", str(root / "scripts/start-kirocrew.sh")],
                                    env=env, capture_output=True, text=True, timeout=10)
            return result, events.read_text() if events.exists() else "", str(bun)

    def test_failed_doctor_never_launches_gateway(self):
        result, events, _ = self.run_launcher(23)
        self.assertEqual(result.returncode, 23, result.stderr)
        self.assertEqual(events, "")

    def test_success_uses_default_model_local_bun_and_existing_gateway_options(self):
        result, events, bun = self.run_launcher(0)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(events.splitlines(), ["gateway --no-open --approval interactive", bun])

    def test_explicit_custom_model_path_reaches_doctor(self):
        result, events, _ = self.run_launcher(0, model_path="/tmp/pilot-custom-model.gguf")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue(events)

    def test_browser_opens_once_after_http_success_and_ready_true(self):
        result, events, _ = self.run_launcher(0, check_browser=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertNotIn("opened early", events)
        self.assertEqual(events.count("Start-Process 'http://localhost:"), 1)
        self.assertIn("Dashboard kész: http://localhost:", result.stdout)

    def test_vscode_task_keeps_the_single_launcher(self):
        tasks = json.loads((ROOT / ".vscode/tasks.json").read_text())["tasks"]
        start = [task for task in tasks if task["label"] == "Kiro Crew: Start"]
        self.assertEqual(len(start), 1)
        self.assertEqual(start[0]["command"], "bash")
        self.assertEqual(start[0]["args"], ["${workspaceFolder}/scripts/start-kirocrew.sh"])


if __name__ == "__main__":
    unittest.main()
