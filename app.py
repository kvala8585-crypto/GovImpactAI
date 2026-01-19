import streamlit as st
import pandas as pd
import pickle
import os
import hashlib
import sqlite3
import random
import smtplib
import time
from email.mime.text import MIMEText

# ================= BASIC APP CONFIG =================
# App nu title, icon ane layout set karva mate
st.set_page_config(
    page_title="GovImpact-AI",
    page_icon="🏛️",
    layout="wide"
)

# OTP ketla second sudhi valid rehse
OTP_EXPIRY_SECONDS = 300

# Admin contact email (future use mate)
ADMIN_EMAIL = "admin@govimpact.ai"

# ================= TEMP DEMO LOGIN =================
# Interview / demo mate fixed login rakhyo che
FIXED_EMAIL = "rkavi6785@gmail.com"
FIXED_PASSWORD = "12345678"

# ================= EMAIL CONFIG =================
# Production ma secrets use thase, local ma fallback
try:
    SMTP_EMAIL = st.secrets["SMTP_EMAIL"]
    SMTP_PASS = st.secrets["SMTP_PASS"]
except:
    SMTP_EMAIL = "yourgmail@gmail.com"
    SMTP_PASS = "GMAIL_APP_PASSWORD"

# ================= DATABASE SETUP =================
DB_PATH = "users.db"

# User table create karva mate function
def init_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            email TEXT UNIQUE,
            password_hash TEXT
        )
    """)
    conn.commit()
    conn.close()

# App start thay tyare DB ready hoy
init_db()

# ================= HELPER FUNCTIONS =================
# Password ne secure hash ma convert karva mate
def hash_password(pw):
    return hashlib.sha256(pw.encode()).hexdigest()

# OTP email send karva mate function
def send_otp_email(to_email, otp):
    msg = MIMEText(f"Your GovImpact-AI OTP is: {otp}\nValid for 5 minutes.")
    msg["Subject"] = "GovImpact-AI OTP Verification"
    msg["From"] = SMTP_EMAIL
    msg["To"] = to_email
    try:
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login(SMTP_EMAIL, SMTP_PASS)
        server.send_message(msg)
        server.quit()
        return True
    except:
        st.error("❌ Email sending failed")
        return False

# ================= LOGIN PAGE =================
def login_page():
    st.subheader("🔐 Login")

    username = st.text_input("👤 Username")
    email = st.text_input("📧 Email")
    password = st.text_input("🔑 Password", type="password")

    if st.button("Login"):

        # Demo / fixed login check (testing purpose)
        if email == FIXED_EMAIL and password == FIXED_PASSWORD:
            st.session_state.logged_in = True
            st.session_state.user = username if username else "Gov User"
            st.session_state.email = email
            st.success("✅ Login successful")
            st.rerun()

        # Normal database based login
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()
        cur.execute(
            "SELECT password_hash FROM users WHERE username=? AND email=?",
            (username, email)
        )
        row = cur.fetchone()
        conn.close()

        if row and row[0] == hash_password(password):
            st.session_state.logged_in = True
            st.session_state.user = username
            st.session_state.email = email
            st.rerun()
        else:
            st.error("❌ Invalid credentials")

# ================= SIGNUP PAGE =================
def signup_page():
    st.subheader("📝 Create Account")

    username = st.text_input("👤 Username")
    email = st.text_input("📧 Email")
    password = st.text_input("🔑 Password", type="password")
    confirm = st.text_input("🔑 Confirm Password", type="password")

    if st.button("Send Verification OTP"):
        if not username or not email or password != confirm:
            st.warning("⚠️ Please enter valid details")
            return

        # Random 6 digit OTP generate
        otp = random.randint(100000, 999999)
        st.session_state.signup_otp = otp
        st.session_state.signup_time = time.time()
        st.session_state.signup_data = (username, email, password)

        if send_otp_email(email, otp):
            st.session_state.page = "signup_verify"
            st.rerun()

# ================= OTP VERIFY PAGE =================
def signup_verify_page():
    st.subheader("📧 Verify Email")

    otp_input = st.text_input("Enter OTP")

    if st.button("Verify & Create"):
        # OTP expiry check
        if time.time() - st.session_state.signup_time > OTP_EXPIRY_SECONDS:
            st.error("⏰ OTP expired")
            st.session_state.page = "signup"
            st.rerun()
            return

        # OTP match thay to account create
        if otp_input == str(st.session_state.signup_otp):
            username, email, password = st.session_state.signup_data
            conn = sqlite3.connect(DB_PATH)
            cur = conn.cursor()
            try:
                cur.execute(
                    "INSERT INTO users (username,email,password_hash) VALUES (?,?,?)",
                    (username, email, hash_password(password))
                )
                conn.commit()
                st.success("✅ Account created successfully")
                st.session_state.page = "login"
                st.rerun()
            except sqlite3.IntegrityError:
                st.error("User already exists")
            conn.close()
        else:
            st.error("❌ Invalid OTP")

# ================= SESSION CONTROL =================
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "page" not in st.session_state:
    st.session_state.page = "login"

# Login flow control
if not st.session_state.logged_in:
    if st.session_state.page == "login":
        login_page()
        if st.button("Create Account"):
            st.session_state.page = "signup"
            st.rerun()
        st.stop()

    elif st.session_state.page == "signup":
        signup_page()
        st.stop()

    elif st.session_state.page == "signup_verify":
        signup_verify_page()
        st.stop()

# ================= DASHBOARD =================
st.sidebar.success(f"Logged in as {st.session_state.user}")
if st.sidebar.button("Logout"):
    st.session_state.clear()
    st.rerun()

# Dashboard header UI
st.markdown("""
<div style="background:#203a43;padding:25px;border-radius:15px;color:white;text-align:center">
<h1>🏛️ GovImpact-AI</h1>
<p>AI-Powered Government Policy Impact Simulator</p>
</div>
""", unsafe_allow_html=True)

# ================= MODEL & DATA LOAD =================
BASE_PATH = r"C:\Users\kavi vala\Desktop\GovImpact-AI"

reg_model = pickle.load(open(os.path.join(BASE_PATH, "model/impact_score_model.pkl"), "rb"))
cls_model = pickle.load(open(os.path.join(BASE_PATH, "model/policy_success_model.pkl"), "rb"))
df = pd.read_csv(os.path.join(BASE_PATH, "data/gov_policy_impact_data.csv"))

# ================= USER INPUT SECTION =================
inputs = {}
cols = st.columns(3)
feature_cols = reg_model.feature_names_in_

for i, col in enumerate(feature_cols):
    with cols[i % 3]:
        inputs[col] = st.number_input(
            col.replace("_", " ").title(),
            value=0.0
        )

# ================= PREDICTION LOGIC ===============
if st.button("🚀 Simulate Policy Impact"):

    # Feature alignment model sathe match karva mate
    reg_features = reg_model.feature_names_in_
    cls_features = cls_model.feature_names_in_

    reg_input = pd.DataFrame(
        [{col: inputs.get(col, 0) for col in reg_features}]
    )

    cls_input = pd.DataFrame(
        [{col: inputs.get(col, 0) for col in cls_features}]
    )

    # Model prediction
    impact_score = reg_model.predict(reg_input)[0]
    success_level = cls_model.predict(cls_input)[0]

    st.success(f"📊 Impact Score: {round(impact_score, 2)}")
    st.info(f"🏆 Success Level: {success_level}")
