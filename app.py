import streamlit as st
import time
import random

# ============================================================================
# CONFIG
# ============================================================================

st.set_page_config(
    page_title="Happy Anniversary ❤️",
    page_icon="💐",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================================
# CSS
# ============================================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@300;400;500;700&family=Great+Vibes&display=swap');

html, body, [class*="css"] {
    font-family: 'Cormorant Garamond', serif;
}

.stApp {
    background: linear-gradient(to bottom, #f6e9da, #f9efe4);
    overflow-x: hidden;
}

.title {
    font-family: 'Great Vibes', cursive;
    text-align: center;
    font-size: 90px;
    color: #7a4b47;
    animation: float 4s ease-in-out infinite;
}

.subtitle {
    text-align: center;
    font-size: 28px;
    color: #5c3b37;
    margin-bottom: 40px;
}

.paper {
    background: rgba(255,255,255,0.5);
    padding: 40px;
    border-radius: 30px;
    box-shadow: 0 10px 40px rgba(0,0,0,0.15);
    border: 1px solid #d7bfa7;
    transition: 0.4s;
}

.paper:hover {
    transform: translateY(-8px);
}

.glass {
    background: rgba(255,255,255,0.25);
    backdrop-filter: blur(12px);
    border-radius: 30px;
    padding: 30px;
    border: 1px solid rgba(255,255,255,0.3);
    box-shadow: 0 8px 32px rgba(0,0,0,0.15);
}

.letter {
    font-size: 28px;
    line-height: 2.2;
    color: #4d3633;
    white-space: pre-wrap;
}

.center {
    text-align: center;
}

.flower {
    position: fixed;
    top: -10px;
    animation: fall linear infinite;
    z-index: 999;
    opacity: 0.8;
}

@keyframes fall {
    0% {
        transform: translateY(-10vh) rotate(0deg);
    }

    100% {
        transform: translateY(110vh) rotate(360deg);
    }
}

@keyframes float {
    0%,100% {
        transform: translateY(0px);
    }

    50% {
        transform: translateY(-10px);
    }
}

</style>
""", unsafe_allow_html=True)

# ============================================================================
# FLOWERS
# ============================================================================

flowers_html = ""

for _ in range(40):

    left = random.randint(0, 100)
    duration = random.randint(8, 20)
    delay = random.randint(0, 10)
    size = random.randint(20, 45)

    flowers_html += f"""
    <div class="flower"
        style="
            left:{left}%;
            animation-duration:{duration}s;
            animation-delay:{delay}s;
            font-size:{size}px;
        ">
        🌸
    </div>
    """

st.markdown(flowers_html, unsafe_allow_html=True)

# ============================================================================
# HERO
# ============================================================================

st.markdown("""
<div class='glass center'>
    <div style='font-size:90px;'>💐</div>
    <div class='title'>Happy 1st Anniversary</div>
    <div class='subtitle'>
        Satu tahun penuh cerita, tawa, tangis, dan rasa sayang yang terus tumbuh.
    </div>
</div>
""", unsafe_allow_html=True)

st.write("")
st.write("")

# ============================================================================
# MUSIC
# ============================================================================

st.markdown("""
<div class='glass center'>

<h1 style='font-size:65px; color:#7a4b47; font-family: Great Vibes, cursive;'>
💌 Sebelum Membaca...
</h1>

<p style='font-size:28px; color:#5c3b37;'>
baca ini sambil denger lagu ini ya sayang 🎵
</p>

</div>
""", unsafe_allow_html=True)

st.link_button(
    "🎵 Putar Lover - Taylor Swift",
    "https://open.spotify.com/track/1dGr1c8CrMLDpV6mPbImSI"
)

st.write("")
st.write("")

# ============================================================================
# CARDS
# ============================================================================

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class='paper center'>
        <h1>🌹</h1>
        <h2>Bunga Untuk Kamu</h2>
        <p>Karena kamu suka bunga, seluruh halaman ini dipenuhi bunga yang jatuh khusus buat kamu.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='paper center'>
        <h1>🧸</h1>
        <h2>Peluk Virtual</h2>
        <p>Kalau lagi kangen, buka halaman ini dan anggap aku lagi meluk kamu erat.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class='paper center'>
        <h1>✨</h1>
        <h2>365 Hari</h2>
        <p>365 hari yang penuh cerita dan semoga terus bertambah sampai seterusnya.</p>
    </div>
    """, unsafe_allow_html=True)

# ============================================================================
# LETTER
# ============================================================================

letter = '''Salam sayang,

‎Haiii Nurul inii akuu Gilfan, orang yang mungkin kamu gapernah kepikiran bisa ngabisin waktu satu tahun bareng, ahahahaa kalau dipikir-pikir lucu juga yaa  kita rul bisa sampai selama ini, jujur satu tahun itu emang bukan waktu yang lama, tapi waktu yang sebentar buat ngabisin waktu kita bersama. Jujur sedih dan bahagianya pasti ada aja di hubungan kita bedua ini, semakin lama semakin aku berusaha buat mahamin gimana kamu dan apa yang kamu ingin. Jujur aku belum bisa menuhin semua wishlist kamu. Tapi, percayalah aku bakal berusaha buat menuhin itu satu-persatu. Jodoh gaada yang tau dan gaada yang bisa memprediksi, aku hari ini blom tentu sama dengan aku hari esok. Tapi, yang perlu kamu tau, aku selalu sayang dan cinta sama kamu dan aku bakal terus berusaha jadi yang terbaik buat kamu. Aku tau aku bukan yang pertama ada di hati kamu, aku juga tau aku bukan orang yang sangat kamu nanti-nantikan. Aku cuman mau kamu tau, kalau banyak hal, banyak kejadian, banyak masalah atau bahkan kebahagiaan yang kamu bawa ke aku, dan aku sangat bersyukur bisa jadi pasangan kamu saat ini. Entah apa yang ada dipikiranku saat ini dan tulisan ini, tapi yang ada di otak aku saat nulis ini cuman satu sayang, dan kamu harus tau itu. Apa yang aku pikir cuman "Aku sayang sama kamu". Mungkin pikiranku terlalu sempit buat nampung perasaanku yang sangat luas ini. Entah kata-kata apalagi yang harus aku keluarin, tapi jujur aku sangat suka kalau kamu lagi tersenyum dan jadi diri kamu sendiri. Semoga kita bisa bersama terus dan saling sayang. Kalaupun kita tidak ditakdirkan bersama aku tetap bersyukur aku bisa sayang sama kamu, aku harap itu tidak terjadi dan semoga kedepannya banyak hal baik yang menimpa kita ya sayang. Semoga semua berjalan lancar dan bahagia.

‎Salam hangat,
‎Gilfan'''

st.write("")
st.write("")

st.markdown(
    "<div class='title' style='font-size:70px;'>Surat Untuk Kamu 💌</div>",
    unsafe_allow_html=True
)

if "typed_complete" not in st.session_state:
    st.session_state.typed_complete = False

if "final_text" not in st.session_state:
    st.session_state.final_text = ""

container = st.empty()

if not st.session_state.typed_complete:

    typed_text = ""

    for char in letter:

        typed_text += char

        container.markdown(
            f"""
            <div class='paper'>
                <div class='letter'>{typed_text}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

        time.sleep(0.035)

    st.session_state.final_text = typed_text
    st.session_state.typed_complete = True

else:

    container.markdown(
        f"""
        <div class='paper'>
            <div class='letter'>{st.session_state.final_text}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

# ============================================================================
# LOVE COUNTER
# ============================================================================

st.write("")
st.write("")

st.markdown("""
<div class='glass center'>
    <h1 style='font-size:60px;'>⏳</h1>
    <h2 style='font-size:45px; color:#7a4b47;'>
        365 Hari Bersama
    </h2>

    <p style='font-size:24px;'>
        dan semoga terus bertambah selamanya 💖
    </p>
</div>
""", unsafe_allow_html=True)

# ============================================================================
# FLOWER GAME
# ============================================================================

st.write("")
st.write("")

st.markdown(
    "<div class='title' style='font-size:65px;'>Mainkan Bunganya 🌸</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='subtitle'>Klik bunga-bunga di bawah ini dan lihat kejutan kecil muncul 💖</div>",
    unsafe_allow_html=True
)

flower_cols = st.columns(8)

flowers = ['🌷','🌹','💐','🌸','🪻','🌺','🌼','🌻']

for i, flower in enumerate(flowers):

    with flower_cols[i]:

        if st.button(flower, use_container_width=True, key=f"flower_{i}"):

            messages = [
                'Aku sayang kamu lebih dari apapun 💖',
                'Kamu rumah paling nyaman 🌸',
                'Aku beruntung punya kamu 💐',
                'Jangan pergi ya cantik 🥺',
                'Semoga kita terus bersama ✨',
                'Kamu lucu banget kalau senyum 🌷'
            ]

            st.success(random.choice(messages))

# ============================================================================
# ENDING
# ============================================================================

st.write("")
st.write("")
st.write("")

st.markdown("""
<div class='glass center'>

<div style='font-size:80px;'>
🕯️🌸💖💐
</div>

<h1 style='font-size:70px; color:#7a4b47; font-family: Great Vibes, cursive;'>
To Nurul, With Love
</h1>

<p style='font-size:28px; color:#5c3b37; line-height:2;'>
Semoga website kecil ini bisa jadi salah satu kenangan manis buat kamu.
</p>

</div>
""", unsafe_allow_html=True)
