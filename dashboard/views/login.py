import streamlit as st
from dashboard.utils.auth import validate_password

def render_login_page():
    if "login_mode" not in st.session_state:
        st.session_state["login_mode"] = "LOGIN"
    if "users_db" not in st.session_state:
        st.session_state["users_db"] = {"admin": "Admin123!"} # Default user

    st.markdown("""
    <style>
    [data-testid="stForm"] {
        background-color: #ffffff;
        padding: 40px;
        border: 4px solid #000 !important;
        border-radius: 15px !important;
        box-shadow: 12px 12px 0px #ffd6e0 !important;
        margin-top: 20px;
        text-align: center;
    }
    [data-testid="stFormSubmitButton"] button, 
    [data-testid="stFormSubmitButton"] button p, 
    [data-testid="stFormSubmitButton"] button div, 
    [data-testid="stFormSubmitButton"] button span {
        color: #ffffff !important;
        font-size: 1.5rem !important;
        font-weight: 500 !important;
        -webkit-text-fill-color: #ffffff !important;
    }
    .auth-title {
        font-size: 2.5rem;
        font-weight: 900;
        text-transform: uppercase;
        margin-bottom: 5px;
        color: #000;
        text-shadow: 3px 3px 0px #bdfcc9;
    }
    .auth-subtitle {
        font-size: 1rem;
        font-weight: bold;
        color: #000;
        margin-bottom: 30px;
        background: #cce0ff;
        display: inline-block;
        padding: 5px 15px;
        border: 2px solid #000;
        border-radius: 8px;
    }
    </style>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        mode = st.session_state["login_mode"]
        if mode == "LOGIN":
            with st.form("login_form"):
                st.markdown('<div class="auth-title">SYSTEM LOGIN</div>', unsafe_allow_html=True)
                st.markdown('<div class="auth-subtitle">ENTER YOUR CREDENTIALS</div>', unsafe_allow_html=True)
                
                username = st.text_input("USERNAME", placeholder="| ENTER USERNAME")
                password = st.text_input("PASSWORD", type="password", placeholder="| ENTER PASSWORD")
                
                st.markdown("<br>", unsafe_allow_html=True)
                submitted = st.form_submit_button("ENTER SYSTEM", use_container_width=True)
                
                if submitted:
                    if not username or not password:
                        st.error("USERNAME AND PASSWORD CANNOT BE EMPTY.")
                    elif username in st.session_state["users_db"] and st.session_state["users_db"][username] == password:
                        st.session_state["logged_in"] = True
                        st.session_state["username"] = username
                        st.rerun()
                    else:
                        st.error("INVALID CREDENTIALS. (Hint: use admin / Admin123!)")
            
            st.markdown("<br>", unsafe_allow_html=True)
            if st.button("NEED AN ACCOUNT? SIGN UP", use_container_width=True):
                st.session_state["login_mode"] = "SIGNUP"
                st.rerun()

        else:
            with st.form("signup_form"):
                st.markdown('<div class="auth-title">NEW REGISTRATION</div>', unsafe_allow_html=True)
                st.markdown('<div class="auth-subtitle">CREATE YOUR POWER-PLAY ACCOUNT</div>', unsafe_allow_html=True)
                
                new_username = st.text_input("NEW USERNAME", placeholder="| CHOOSE USERNAME")
                new_password = st.text_input("NEW PASSWORD", type="password", help="Minimum 8 chars, 1 uppercase, 1 number, 1 special character.", placeholder="| SET PASSWORD")
                confirm_password = st.text_input("CONFIRM PASSWORD", type="password", placeholder="| RE-ENTER PASSWORD")
                
                st.markdown("<br>", unsafe_allow_html=True)
                submitted = st.form_submit_button("CREATE ACCOUNT", use_container_width=True)
                
                if submitted:
                    if not new_username:
                        st.error("USERNAME CANNOT BE EMPTY.")
                    elif new_username in st.session_state["users_db"]:
                        st.error("USERNAME ALREADY EXISTS.")
                    elif new_password != confirm_password:
                        st.error("PASSWORDS DO NOT MATCH.")
                    else:
                        is_valid, msg = validate_password(new_password)
                        if not is_valid:
                            st.error(f"WEAK PASSWORD: {msg}")
                        else:
                            st.session_state["users_db"][new_username] = new_password
                            st.success("ACCOUNT CREATED SUCCESSFULLY! LOGGING IN...")
                            st.session_state["logged_in"] = True
                            st.session_state["username"] = new_username
                            import time
                            time.sleep(1)
                            st.rerun()
                            
            st.markdown("<br>", unsafe_allow_html=True)
            if st.button("ALREADY HAVE AN ACCOUNT? LOGIN", use_container_width=True):
                st.session_state["login_mode"] = "LOGIN"
                st.rerun()
