"""
FP Sensor Lab - one-click launcher
====================================
Double-click this file (or run: python START.py)
It will install missing packages then open the app in your browser.
"""
import subprocess, sys, importlib, webbrowser, time, os, socket

REQUIRED = ["streamlit", "numpy", "scipy", "pandas", "scikit_learn", "plotly"]
PORT = 8501
URL  = f"http://localhost:{PORT}"

# ── 1. Install any missing packages ─────────────────────────────────────────
def check_and_install():
    missing = []
    for pkg in REQUIRED:
        try:
            importlib.import_module(pkg.replace("-", "_"))
        except ImportError:
            missing.append(pkg.replace("_", "-"))

    if missing:
        print(f"Installing: {', '.join(missing)} ...")
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", "--quiet"] + missing
        )
        print("Done.\n")

# ── 2. Wait until the server port is open, then open browser ─────────────────
def wait_and_open(url, port, timeout=30):
    print(f"\n{'='*52}")
    print(f"  FP Sensor Lab is starting ...")
    print(f"  Open this link in any browser:")
    print(f"\n      {url}\n")
    print(f"{'='*52}\n")
    deadline = time.time() + timeout
    while time.time() < deadline:
        try:
            with socket.create_connection(("localhost", port), timeout=1):
                break
        except OSError:
            time.sleep(0.5)
    webbrowser.open(url)

# ── 3. Launch Streamlit ──────────────────────────────────────────────────────
def main():
    check_and_install()

    # Locate app.py relative to this script
    here = os.path.dirname(os.path.abspath(__file__))
    app  = os.path.join(here, "app.py")

    # Open the browser once the port is up (runs in background thread)
    import threading
    threading.Thread(target=wait_and_open, args=(URL, PORT), daemon=True).start()

    # Start Streamlit (blocks until the window is closed)
    subprocess.run([
        sys.executable, "-m", "streamlit", "run", app,
        "--server.port",              str(PORT),
        "--browser.gatherUsageStats", "false",
        "--server.headless",          "false",
    ], cwd=here)

if __name__ == "__main__":
    main()
