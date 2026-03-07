import streamlit as st
from streamlit_webrtc import webrtc_streamer
import random

# Sahifa sozlamalari
st.set_page_config(page_title="1_s_m_a_i_1_o_v", page_icon="🎥")

# --- ADMIN BOSHQARUVI (SIDEBAR) ---
st.sidebar.title("⚙️ Boshqaruv (Admin)")
admin_pass = st.sidebar.text_input("Parol kiring", type="password")

# Reklama matni (Admin o'zgartirishi mumkin)
reklama_text = "REKLAMAGA BUYURTMA BERING / ЗАКАЗАТЬ РЕКЛАМУ"
if admin_pass == "12345": # Sizning parolingiz
    st.sidebar.success("Xush kelibsiz, Ismoilov!")
    reklama_text = st.sidebar.text_area("Reklama matnini o'zgartirish", reklama_text)
    if st.sidebar.button("Hamma foydalanuvchilarni bloklash"):
        st.sidebar.warning("Tizim vaqtincha to'xtatildi.")

# --- ASOSIY EKRAN ---
st.markdown(f"<h1 style='text-align: center; color: red;'>🔴 1_s_m_a_i_1_o_v</h1>", unsafe_allow_html=True)

st.write("### Onlayn video-muloqot")
st.info("Kameraga ruxsat bering va suhbatni boshlang!")

# Video oyna (WebRTC - Kamera uchun)
webrtc_streamer(key="ruletka", rtc_configuration={
    "iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]
})

# Tugmalar
col1, col2 = st.columns(2)
with col1:
    if st.button("➡️ Keyingi foydalanuvchi"):
        st.write("Qidirilmoqda... 🔎")
with col2:
    if st.button("❌ To'xtatish"):
        st.write("Aloqa uzildi.")

# --- REKLAMA BO'LIMI (PASTDA) ---
st.markdown("---")
st.warning(f"**📢 {reklama_text}**")

# Siz so'ragan tillardagi reklamalar
st.markdown("""
**REKLAMA UCHUN / РЕКЛАМА ҮЧҮН / ДЛЯ РЕКЛАМЫ:**
* 🇺🇿 **O'zbekcha:** Reklamaga buyurtma berish
* 🇰🇬 **Кыргызча:** Рекламага буйрутма бериңиз
* 🇷🇺 **Русский:** Заказать рекламу
""")

# SIZNING NOMERINGIZ
st.error("📞 **+996 990 220 477**")
