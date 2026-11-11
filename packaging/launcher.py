"""FP Sensor Lab - standalone launcher (used by PyInstaller).

Double-click FPSensorLab.exe: starts the app and opens the browser automatically.
Close the window to stop.
"""
import multiprocessing
import os
import sys

# Force PyInstaller to bundle these packages (they are imported by the app at runtime)
import numpy, pandas, scipy, scipy.stats, scipy.optimize, scipy.interpolate  # noqa: F401,E401
import plotly.graph_objects, plotly.subplots                                   # noqa: F401,E401
import streamlit.web.cli as stcli


def base_dir() -> str:
    return getattr(sys, "_MEIPASS", os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def _open_browser_when_ready(port: str) -> None:
    import threading, time, urllib.request, webbrowser

    def _wait_and_open():
        for _ in range(120):
            try:
                urllib.request.urlopen(f"http://localhost:{port}/_stcore/health", timeout=1)
                break
            except Exception:
                time.sleep(0.5)
        webbrowser.open(f"http://localhost:{port}")

    threading.Thread(target=_wait_and_open, daemon=True).start()


if __name__ == "__main__":
    multiprocessing.freeze_support()
    base = base_dir()
    os.chdir(base)
    if base not in sys.path:
        sys.path.insert(0, base)
    port = os.environ.get("FP_SENSOR_PORT", "8501")
    sys.argv = [
        "streamlit", "run", os.path.join(base, "app.py"),
        "--global.developmentMode=false",
        "--server.headless=true",
        "--browser.gatherUsageStats=false",
        f"--server.port={port}",
        "--server.fileWatcherType=none",
    ]
    print(f"\nFP Sensor Lab is starting.")
    print(f"If your browser does not open automatically, go to:  http://localhost:{port}")
    print("Close this window to stop.\n")
    _open_browser_when_ready(port)
    sys.exit(stcli.main())
