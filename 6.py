import streamlit as st
from streamlit_webrtc import webrtc_streamer, WebRtcMode, RTCConfiguration
import time

# Sahifa sozlamalari
st.set_page_config(page_title="1_s_m_a_i_1_o_v", layout="wide", initial_sidebar_state="collapsed")

# --- ADMIN PAROLI ---
ADMIN_PASSWORD = "10001h"

# --- STIL (Ome.TV dizayni) ---
st.markdown("""
    <style>
    .main { background-color: #1a1a1a; color: white; }
    .stButton>button { width: 100%; border-radius: 20px; background-color: #ff4b4b; color: white; height: 50px; font-weight: bold; }
    .video-container { position: relative; width: 100%; background: black; border-radius: 10px; min-height: 300px; display: flex; align-items: center; justify-content: center; }
    .reklama-box { border: 2px solid #555; padding: 15px; border-radius: 10px; text-align: center; background: #262626; margin-bottom: 10px; }
    .chat-box { height: 250px; overflow-y: scroll; border: 1px solid #444; padding: 10px; background: #000; color: #00ff00; font-family: monospace; }
    </style>
    """, unsafe_allow_html=True)

# --- ASOSIY FUNKSIYALAR ---
if 'user_id' not in st.session_state:
    st.session_state.user_id = f"ID-{int(time.time()) % 100000}"
if 'online_count' not in st.session_state:
    st.session_state.online_count = 24 

# --- KIRISH QISMI (Qirg'iz tilida) ---
if 'username' not in st.session_state:
    st.title("🔴 1_s_m_a_i_1_o_v")
    st.subheader("Кош келиңиз!")
    # Ism so'rash qismida "Umar" deb o'zgartirildi
    name = st.text_input("Атыңызды киргизиңиз:", placeholder="Мисалы: Умар")
    if st.button("Кирүү"):
        if name:
            st.session_state.username = name
            st.rerun()
else:
    # --- INTERFEYS ---
    col1, col2 = st.columns([2, 1]) 

    with col1:
        st.markdown(f"### Сиздин ID: <span style='color:#ff4b4b'>{st.session_state.user_id}</span> | Онлайн: {st.session_state.online_count}", unsafe_allow_html=True)
        
        # Tasodifiy odam videosi
        st.markdown("<div class='video-container'><b>Издөөдө... (Searching...)</b></div>", unsafe_allow_html=True)
        
        # O'zingizning kamerangiz (Xatolar tuzatilgan versiya)
        RTC_CONFIG = RTCConfiguration({"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]})
        webrtc_streamer(
            key="main-video",
            mode=WebRtcMode.SENDRECV,
            rtc_configuration=RTC_CONFIG,
            media_stream_constraints={"video": True, "audio": True}
        )
        
        if st.button("➡️ Кийинки"):
            st.toast("Жаңы колдонуучу изделүүдө...")

    with col2:
        # --- REKLAMA ---
        st.markdown("<div class='reklama-box'>", unsafe_allow_html=True)
        st.write("📢 **ЖАРНАМА (РЕКЛАМА)**")
        st.warning(f"Жарнама: 15 секунд")
        st.markdown(f"""
        <hr style='border: 0.5px solid #444'>
        <p style='font-size: 13px; color: #bbb;'>Бу жерде сиздин жарнамаңыз болушу мүмкүн</p>
        <p style='font-size: 16px; font-weight: bold;'>📞 +996 990 220 477</p>
        <p style='font-size: 20px;'>🟢 WhatsApp | 🔵 Telegram</p>
        """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

        # --- CHAT ---
        st.markdown("### Чат")
        st.markdown("<div class='chat-box'>Жазышууну баштаңыз...</div>", unsafe_allow_html=True)
        st.text_input("Билдирүү жазыңыз...", key="chat_input")

# --- ADMIN PANEL (O'zbek tilida) ---
with st.sidebar:
    st.header("⚙️ Boshqaruv (Admin)")
    pw = st.text_input("Parolni kiriting", type="password")
    if pw == ADMIN_PASSWORD:
        st.success("Xush kelibsiz, Ismoilov!")
        st.subheader("Sozlamalar")
        st.number_input("Vaqt (sekund)", value=15)
        st.checkbox("Ovozli reklama", value=False)
