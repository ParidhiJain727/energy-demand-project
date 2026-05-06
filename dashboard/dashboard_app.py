import sys
from pathlib import Path
import streamlit as st

# Add project root to sys.path
BASE_DIR = Path(__file__).resolve().parents[1]
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

# Import CSS
from dashboard.utils.css import CSS_STRING

# Import Views
from dashboard.views.login import render_login_page
from dashboard.views.dashboard import render_dashboard_page
from dashboard.views.explainer import render_explainer_page
from dashboard.views.terminal import render_terminal_page

def main():
    st.set_page_config(
        page_title="Smart Demand Forecasting",
        page_icon="⚡",
        layout="wide",
    )
    
    st.markdown(CSS_STRING, unsafe_allow_html=True)
    
    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False
        st.session_state["username"] = ""
        st.session_state["show_explainer"] = False
        st.session_state["show_terminal"] = False

    # Top Navigation Area
    nav_col1, nav_col2, nav_col3 = st.columns([4.5, 0.5, 4.0])
    with nav_col1:
        st.markdown("""
        <div style="display: flex; align-items: center; gap: 15px; margin-top: 10px;">
            <h1 style="font-size: 2.5rem; font-weight: 950; color: #000; text-shadow: 3px 3px 0px #ffd6e0; margin: 0; line-height: 1;">POWERPLAY</h1>
            <div style="font-size: 0.7rem; font-weight: bold; letter-spacing: 2px; background: #bdfcc9; padding: 4px 10px; border: 2px solid #000; border-radius: 6px; box-shadow: 2px 2px 0px #000; white-space: nowrap;">
                ADVANCED FORECASTER
            </div>
        </div>
        """, unsafe_allow_html=True)
    with nav_col3:
        # A container acting as the black panel
        panel = st.container()
        with panel:
            st.markdown("""
            <style>
            [data-testid="stVerticalBlock"] > [style*="flex-direction: column;"] > [data-testid="stVerticalBlock"] {
                background-color: #000000;
                padding: 10px;
                border-radius: 12px;
                box-shadow: -4px 4px 0px #bdfcc9;
            }
            </style>
            """, unsafe_allow_html=True)
            if st.session_state.get("show_explainer", False) or st.session_state.get("show_terminal", False):
                if st.button("BACK TO SYSTEM", use_container_width=True):
                    st.session_state["show_explainer"] = False
                    st.session_state["show_terminal"] = False
                    st.rerun()
            else:
                nav_btn_col1, nav_btn_col2 = st.columns(2)
                with nav_btn_col1:
                    if st.button("WHAT IS POWER PLAY ?", use_container_width=True):
                        st.session_state["show_explainer"] = True
                        st.rerun()
                with nav_btn_col2:
                    if st.button("CHAT WITH US!", use_container_width=True):
                        st.session_state["show_terminal"] = True
                        st.rerun()

    st.markdown("<hr style='border: 2px solid #000; margin-top: 5px; margin-bottom: 20px;'>", unsafe_allow_html=True)

    if st.session_state.get("show_terminal", False):
        render_terminal_page()
    elif st.session_state.get("show_explainer", False):
        render_explainer_page()
    else:
        if not st.session_state["logged_in"]:
            render_login_page()
        else:
            render_dashboard_page()

if __name__ == "__main__":
    main()
