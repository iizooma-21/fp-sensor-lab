"""Fabry-Perot Interferometer Sensor Lab - entry point.

Customised version: Sensor Lab (Fabry-Perot only) + Theory (Optical section) tabs.

Run with:   streamlit run app.py
"""
import streamlit as st

from core import branding, help_ui, viz

st.set_page_config(page_title="FP Sensor Lab", page_icon=str(branding.ASSETS / "logo_placeholder.png"),
                   layout="wide", initial_sidebar_state="expanded")

try:
    st.logo(str(branding.find_logo()), size="large")
except Exception:
    st.logo(str(branding.ASSETS / "logo_placeholder.png"), size="large")

try:
    NATIVE = st.context.theme.type or "light"
except Exception:
    NATIVE = "light"

_choice = st.sidebar.segmented_control("Appearance", ["Auto", "Light", "Dark"], default="Auto", key="appearance",
                                       help="Auto follows your computer's light/dark setting. Choose Light or Dark to override it.")
WANT = NATIVE if _choice in (None, "Auto") else _choice.lower()
viz.set_theme(NATIVE)
st.markdown(branding.css(NATIVE) + (branding.INVERT_CSS if WANT != NATIVE else ""),
            unsafe_allow_html=True)

pages = [
    st.Page("views/sensor_lab.py", title="Sensor Lab", icon=":material/sensors:", default=True),
    st.Page("views/theory.py",     title="Theory",     icon=":material/menu_book:"),
]
APP_VERSION = "2026-09-21 appearance-button"
nav = st.navigation(pages)
help_ui.sidebar_toggle()
st.sidebar.caption(f"Version {APP_VERSION} · showing {WANT}")
nav.run()
