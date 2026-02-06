
# Install Streamlit if not already installed

import streamlit as st
import time
import random

# Page Config
st.set_page_config(
    page_title="Happy Birthday Beboo Jan ❤️",
    page_icon="🎂",
    layout="centered"
)

# Custom CSS for a more premium look
st.markdown('''
<style>
    .main {
        background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 100%);
    }
    .big-title {
        text-align: center;
        font-size: 55px;
        font-weight: 800;
        color: #d63384;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        padding-bottom: 20px;
    }
    .card {
        background: rgba(255, 255, 255, 0.8);
        padding: 30px;
        border-radius: 25px;
        border: 2px solid #ffb6c1;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        text-align: center;
        color: #4a4a4a;
        font-size: 18px;
    }
    .stButton>button {
        width: 100%;
        border-radius: 50px;
        background-color: #ff4b2b;
        color: white;
        font-weight: bold;
        border: none;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #ff416c;
        transform: scale(1.05);
    }
</style>
''', unsafe_allow_html=True)

# --- HEADER ---
st.markdown("<div class='big-title'>🎂 Happy Birthday, Beboo Jan! ❤️</div>", unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.write("### 🎈 Celebration Controls")
    play_music = st.checkbox("Play Birthday Vibes", value=True)
    if play_music:
        st.write("🎵 *Ready to celebrate!*")

# --- MAIN HEARTFELT MESSAGE ---
st.markdown('''
<div class='card'>
    <h3>✨ To My Favorite Person ✨</h3>
    <p>You aren't just my partner; you're my best friend, my peace, and my home. 
    Today, the world got a little brighter because you were born. 🌸</p>
    <p><b>May this year bring you as much joy as you bring to my life every single day.</b></p>
</div>
''', unsafe_allow_html=True)

st.write("---")

# --- INTERACTIVE SECTION ---
st.subheader("💌 A few reasons why you're amazing...")
reasons = [
    "Your beautiful smile that lights up my darkest days. 😊",
    "The way you care for the people around you. ❤️",
    "Your laugh—it's my favorite sound in the world. 🎶",
    "How you support me in everything I do.🤝",
    "Just being YOU. You are perfect. ✨"
]

if st.button("Click for a reason I love you"):
    reason = random.choice(reasons)
    st.info(reason)

# --- PHOTO GALLERY ---
st.subheader("📸 Our Beautiful Memories")
col1, col2 = st.columns(2)
with col1:
    st.image("https://via.placeholder.com/300x400.png?text=Photo+1", caption="A special moment ✨")
with col2:
    st.image("https://via.placeholder.com/300x400.png?text=Photo+2", caption="I love this one! ❤️")

st.write("---")

# --- SURPRISE BUTTON ---
if st.button("🎁 OPEN YOUR GIFT"):
    st.balloons()
    st.snow() 
    time.sleep(1)
    st.success("🎉 SURPRISE! You get unlimited hugs and kisses today! 💋")
    st.markdown("### 💍 I love you more than words can say.")

# --- FOOTER ---
st.write("")
st.markdown("<div style='text-align: center; color: grey;'>Made with ❤️ for Beboo Jan</div>", unsafe_allow_html=True)
