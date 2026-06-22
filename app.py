import streamlit as st
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from config.theme import COLORS
from modules.auth import login, register, logout
from modules.life_score import compute_life_score
from utils.database import init_db
from utils.styles import inject_styles, metric_card, page_title

st.set_page_config(page_title="LifeOS AI", page_icon="🌟", layout="wide", initial_sidebar_state="expanded")
inject_styles()
init_db()

with st.sidebar:
    st.markdown(f"""
    <div style="text-align:center;padding:20px 0 10px 0;">
        <div style="font-size:2.5rem;filter:drop-shadow(0 0 12px rgba(0,212,255,0.6));">🌟</div>
        <div style="font-size:1.4rem;font-weight:800;background:linear-gradient(90deg,#00d4ff,#a855f7);
            -webkit-background-clip:text;-webkit-text-fill-color:transparent;">LifeOS AI</div>
        <div style="font-size:0.8rem;color:rgba(255,255,255,0.4);">Your Life Operating System</div>
    </div>""", unsafe_allow_html=True)
    st.markdown('<hr class="glow-divider">', unsafe_allow_html=True)
    if "user" in st.session_state and st.session_state.user:
        u = st.session_state.user
        total, scores = compute_life_score(u["username"])
        st.markdown(f"""
        <div style="background:rgba(15,17,42,0.8);border:1px solid rgba(99,102,241,0.35);
            border-radius:14px;padding:16px;margin-bottom:16px;backdrop-filter:blur(8px);">
            <div style="color:rgba(255,255,255,0.4);font-size:0.8rem;">Logged in as</div>
            <div style="color:#fff;font-weight:700;font-size:1.05rem;">👤 {u['username']}</div>
            <div style="margin-top:12px;">
                <div style="color:rgba(255,255,255,0.4);font-size:0.8rem;margin-bottom:4px;">Life Score</div>
                <div style="font-size:1.8rem;font-weight:800;color:{COLORS['primary']};
                    text-shadow:0 0 16px rgba(99,102,241,0.6);">{total}
                    <span style="font-size:1rem;color:rgba(255,255,255,0.4);">/100</span></div>
            </div>
        </div>""", unsafe_allow_html=True)
        if st.button("🚪 Logout"):
            logout()
    else:
        st.info("👋 Please log in to access all features")

if "user" not in st.session_state or not st.session_state.user:
    st.markdown("""
    <div style="text-align:center;padding:60px 0 40px 0;">
        <div style="font-size:4rem;margin-bottom:16px;filter:drop-shadow(0 0 20px rgba(0,212,255,0.7));">🌟</div>
        <h1 style="font-size:3rem;font-weight:900;
            background:linear-gradient(90deg,#00d4ff,#a855f7,#ec4899,#f59e0b,#00d4ff);
            background-size:300% auto;-webkit-background-clip:text;-webkit-text-fill-color:transparent;
            animation:shimmer 4s linear infinite;margin:0;">LifeOS AI</h1>
        <p style="color:rgba(255,255,255,0.5);font-size:1.2rem;margin-top:12px;">Your Intelligent Life Operating System</p>
    </div>""", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        tab1, tab2 = st.tabs(["🔐 Login", "✨ Register"])
        with tab1:
            uname = st.text_input("Username", key="li_user")
            pw    = st.text_input("Password", type="password", key="li_pw")
            if st.button("Login →", key="login_btn"):
                ok, user = login(uname, pw)
                if ok:
                    st.session_state.user = user
                    st.success(f"Welcome back, {user['username']}! 🎉")
                    st.rerun()
                else:
                    st.error("Invalid credentials")
        with tab2:
            r_user  = st.text_input("Username", key="reg_u")
            r_email = st.text_input("Email", key="reg_e")
            r_pw    = st.text_input("Password", type="password", key="reg_p")
            r_role  = st.selectbox("I am a...", ["personal","student","college","business"], key="reg_r")
            if st.button("Create Account →", key="reg_btn"):
                if r_user and r_pw:
                    ok, msg = register(r_user, r_pw, r_email, r_role)
                    if ok:
                        st.success(msg + " Please login.")
                    else:
                        st.error(msg)
                else:
                    st.warning("Fill in username and password")
else:
    u = st.session_state.user
    page_title("🌟", "LifeOS AI Dashboard", f"Welcome back, {u['username']}! Here's your life at a glance.")
    total, scores = compute_life_score(u["username"])
    cols = st.columns(6)
    icons = {"Mood":"😊","Health":"❤️","Goals":"🎯","Finance":"💰","Tasks":"✅"}
    clrs  = [COLORS["primary"],COLORS["accent"],COLORS["secondary"],COLORS["success"],COLORS["warning"],COLORS["danger"]]
    with cols[0]: metric_card("Life Score", f"{total}/100", icon="⭐", color=COLORS["primary"])
    for i,(k,v) in enumerate(scores.items()):
        with cols[i+1]: metric_card(k, f"{v}/20", icon=icons[k], color=clrs[i+1])
    st.markdown('<hr class="glow-divider">', unsafe_allow_html=True)
    st.markdown('<h3 style="color:#fff;font-weight:700;margin-bottom:16px;">🚀 Quick Access</h3>', unsafe_allow_html=True)
    pages=[("📔","Smart Diary",COLORS["primary"]),("😊","Mood Tracker",COLORS["secondary"]),
           ("🎯","Goals",COLORS["success"]),("💰","Finance",COLORS["warning"]),
           ("❤️","Health",COLORS["danger"]),("🤖","AI Assistant",COLORS["accent"])]
    cols2=st.columns(6)
    for i,(icon,name,color) in enumerate(pages):
        with cols2[i]:
            st.markdown(f"""<div style="background:rgba(15,17,42,0.7);border:1px solid {color}55;border-radius:18px;
                padding:22px 10px;text-align:center;backdrop-filter:blur(8px);
                box-shadow:0 0 16px {color}33;cursor:pointer;">
                <div style="font-size:2rem;filter:drop-shadow(0 0 8px {color});">{icon}</div>
                <div style="color:{color};font-weight:700;font-size:0.85rem;margin-top:8px;">{name}</div>
            </div>""", unsafe_allow_html=True)
    st.markdown('<br><p style="color:rgba(255,255,255,0.3);text-align:center;font-size:0.85rem;">Navigate using the sidebar to access all 16 modules • LifeOS AI v2.0</p>', unsafe_allow_html=True)