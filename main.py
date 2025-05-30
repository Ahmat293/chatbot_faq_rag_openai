import os
from pathlib import Path

import requests
import streamlit as st
from document_loader import load_and_vectorize_document
from rag_core import ask_question
from speech_to_text import transcribe_audio
from streamlit_mic_recorder import mic_recorder
from text_to_speech import speak_text

# -----------------------------------------------------------------------------#
# 📄 Configuration de la page                                                 #
# -----------------------------------------------------------------------------#
st.set_page_config(
    page_title="ChatAdam – FAQ interne & Toolbox",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -----------------------------------------------------------------------------#
# 🎨 Style global                                                             #
# -----------------------------------------------------------------------------#
CSS = """
<style>
/* ---------- Reset -------------------------------------------------------- */
#MainMenu, header, footer {visibility: hidden;}
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap');
html, body, [class*="css"] {
  font-family: 'Inter', sans-serif;
  scroll-behavior: smooth;
  font-size: 16px;
}

/* ---------- Variables ---------------------------------------------------- */
:root {
  --primary:   #6C63FF;   /* Lavande douce */
  --primary-d: #584CE0;   /* Lavande foncée */
  --bg-chat:   #F9FAFB;
  --user-msg:  #F3F4F6;
  --bot-msg:   #E0ECFF;
  --gray-900:  #111827;
}

/* ---------- Sidebar ----------------------------------------------------- */
section[data-testid="stSidebar"] {
  background: #f9fafb; /* gris très clair */
  padding: 1rem 1.5rem 2rem;
  color: #111827; /* gris foncé */
}

section[data-testid="stSidebar"] * {
  color: #111827 !important; /* texte sombre partout */
}

/* ---------- Cartes de la sidebar ---------------------------------------- */
.sidebar-card {
  background: #ffffff; /* blanc pur */
  color: var(--gray-900);
  border-radius: 1rem;
  padding: 1.2rem;
  margin-bottom: 1.5rem;
  box-shadow: 0 4px 16px rgba(0,0,0,0.07);
}
.sidebar-card--compact {
  padding: 1rem;
  margin-bottom: 1.2rem;
}
.sidebar-card h3 {
  margin: 0 0 .8rem;
  font-size: 1.1rem;
  color: var(--primary);
}

/* ---------- Upload ------------------------------------------------------ */
.sidebar-card .stFileUploader>div {
  border: 2px dashed var(--primary);
  background: var(--bg-chat) !important;
  border-radius: 0.75rem;
  padding: 0.75rem;
  text-align: center;
  transition: all 0.3s ease;
}
.sidebar-card .stFileUploader>div:hover {
  background: #e8edff !important;
  border-color: var(--primary-d);
}
.sidebar-card .stFileUploader * {
  color: var(--gray-900) !important;
}

/* ---------- Inputs + selects -------------------------------------------- */
.sidebar-card .stTextInput>div,
.sidebar-card .stNumberInput>div,
.sidebar-card .stSelectbox>div {
  background: var(--bg-chat) !important;
  border-radius: .55rem !important;
}
.sidebar-card input {
  color: var(--gray-900) !important;
}

/* ---------- Boutons (généraux) ------------------------------------------ */
.stButton>button,
.stDownloadButton>button,
.stFormSubmitButton>button {
  background: var(--primary);
  color: #fff;
  border: none;
  border-radius: .6rem;
  padding: .6rem 1.25rem;
  transition: all 0.2s ease;
  font-weight: 500;
}
.stButton>button:hover,
.stDownloadButton>button:hover,
.stFormSubmitButton>button:hover {
  background: var(--primary-d);
}

/* ---------- Input du chat ----------------------------------------------- */
input[type="text"] {
  border: 1.5px solid #cbd5e1 !important;
  border-radius: .55rem !important;
  padding: .55rem .8rem !important;
  background: #fff !important;
  color: #000 !important;
}
input[type="text"]:focus {
  border-color: var(--primary) !important;
  box-shadow: 0 0 0 2px rgba(108, 99, 255, 0.3);
}

/* ---------- Micro bouton ------------------------------------------------ */
button[data-testid="baseButton-chat_form-micro_chat"] {
  font-size: 1.2rem;
  background: #f1f5f9;
  color: #000;
  border-radius: 0.5rem;
  border: 1.5px solid #cbd5e1;
  transition: all 0.2s ease;
}
button[data-testid="baseButton-chat_form-micro_chat"]:hover {
  background: #e0ecff;
  border-color: var(--primary);
}

/* ---------- Mode sombre ------------------------------------------------- */
.dark-mode html, .dark-mode body, .dark-mode [class*="css"] {
  background: #0f172a !important;
  color: #e2e8f0 !important;
}
.dark-mode .assistant {
  background: #1e293b !important;
}
.dark-mode .stButton>button,
.dark-mode .stFormSubmitButton>button {
  background: #3b82f6;
}

/* ---------- Lisibilité texte (upload, labels, inputs) ------------------- */
.sidebar-card .stFileUploader * {
  color: #1f2937 !important;
  font-weight: 500;
}
.sidebar-card input::placeholder,
.sidebar-card textarea::placeholder {
  color: #4b5563 !important;
  opacity: 1;
}
.sidebar-card label,
.sidebar-card .stTextInput label,
.sidebar-card .stSelectbox label {
  color: #1e1e1e !important;
  font-weight: 500;
}
.sidebar-card .stTextInput>div,
.sidebar-card .stSelectbox>div {
  border: 1px solid #ddd !important;
}
.sidebar-card input:hover,
.sidebar-card textarea:hover {
  background-color: #f0f4ff !important;
}

</style>
"""



st.markdown(CSS, unsafe_allow_html=True)

# -----------------------------------------------------------------------------#
# 🗄️  Session state                                                          #
# -----------------------------------------------------------------------------#
def init_state():
    defaults = {
        "messages":     [],
        "documents":    [],
        "selected_doc": None,
        "dark_mode":    False,
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v
init_state()

# -----------------------------------------------------------------------------#
# 📚  SIDEBAR                                                                 #
# -----------------------------------------------------------------------------#
with st.sidebar:
    # ---- logo & titre -------------------------------------------------------
    st.markdown("<h1 style='font-size:1.85rem;margin:0 0 .4rem'>💼 ChatAdam</h1>", unsafe_allow_html=True)
    st.write("**Assistant interne & Toolbox**")
    st.markdown("---")

    # ---- CARD : Upload ------------------------------------------------------
    st.markdown('<div class="sidebar-card">', unsafe_allow_html=True)
    st.markdown("### 📑 Ajouter des documents", unsafe_allow_html=True)

    uploaded_file = st.file_uploader("Glisse un PDF ici", type="pdf")
    if uploaded_file is not None:
        data_dir = Path("data"); data_dir.mkdir(exist_ok=True)
        file_path = data_dir / uploaded_file.name
        file_path.write_bytes(uploaded_file.read())

        vectorstore_name = file_path.stem
        with st.spinner("Indexation en cours…"):
            load_and_vectorize_document(file_path, vectorstore_name)

        st.success(f"✅ {uploaded_file.name} indexé")

        if vectorstore_name not in st.session_state.documents:
            st.session_state.documents.append(vectorstore_name)
            st.session_state.selected_doc = vectorstore_name
    st.markdown('</div>', unsafe_allow_html=True)

    # ---- CARD : Sélection + dark mode --------------------------------------
    st.markdown('<div class="sidebar-card sidebar-card--compact">', unsafe_allow_html=True)

    if st.session_state.documents:
        st.session_state.selected_doc = st.selectbox(
            "Document actif",
            st.session_state.documents,
            index=st.session_state.documents.index(st.session_state.selected_doc)
            if st.session_state.selected_doc in st.session_state.documents else 0,
        )
    else:
        st.info("Aucun document pour l'instant.")

    st.session_state.dark_mode = st.checkbox("🌙 Mode sombre (expérimental)")
    if st.session_state.dark_mode:
        st.markdown("<script>document.documentElement.classList.add('dark-mode');</script>", unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    # ---- footer -------------------------------------------------------------
    st.caption("by Ahmat Adam")

# -----------------------------------------------------------------------------#
# 🏠  Mise en page principale                                                 #
# -----------------------------------------------------------------------------#
tab_chat, tab_tools, tab_about = st.tabs(["💬 Discussion", "🛠️ Conversions", "ℹ️ À propos"])

# -----------------------------------------------------------------------------#
# 💬  CHAT                                                                   #
# -----------------------------------------------------------------------------#
def process_query(q: str, speak: bool = False):
    """Stocke la question, interroge le RAG, ajoute la réponse."""
    st.session_state.messages.append({"role": "user", "content": q})

    with st.spinner("Recherche en cours…"):
        try:
            raw = ask_question(q, st.session_state.selected_doc)
            answer = raw.get("result") if isinstance(raw, dict) else raw
        except Exception as exc:
            answer = f"⚠️ Erreur : {exc}"

    st.session_state.messages.append({"role": "assistant", "content": answer})
    st.toast("Réponse prête ✅")

    if speak:
        speak_text(answer)

# ---------- Onglet Discussion ----------------------------------------------
with tab_chat:
    st.markdown(
        "<h2 style='background: -webkit-linear-gradient(90deg, var(--primary), var(--primary-d));"
        " -webkit-background-clip: text; -webkit-text-fill-color: transparent;'>Pose ta question</h2>",
        unsafe_allow_html=True,
    )

    chat_container = st.container()

    with st.form("chat_form", clear_on_submit=True):
        col_txt, col_mic = st.columns([8, 1], gap="small")

        with col_txt:
            user_input = st.text_input(
                "Pose ta question",
                placeholder="Tape ici puis Entrée…",
                label_visibility="collapsed",
            )
        with col_mic:
            audio = mic_recorder(
                start_prompt="🎤", stop_prompt="🔴", just_once=True,
                use_container_width=True, key="micro_chat"
            )

        submitted = st.form_submit_button("Envoyer")

    # Texte
    if submitted and user_input:
        if not st.session_state.selected_doc:
            st.error("⚠️ Aucun document sélectionné.")
        else:
            process_query(user_input, speak=False)

    # Audio
    if audio is not None:
        if not st.session_state.selected_doc:
            st.error("⚠️ Aucun document sélectionné.")
        else:
            st.info("Transcription en cours…")
            try:
                text = transcribe_audio(audio["bytes"])
                process_query(text, speak=True)
            except Exception as exc:
                st.error(f"⚠️ Erreur transcription : {exc}")

    # Fil de conversation
    with chat_container:
        if st.session_state.messages:
            for msg in st.session_state.messages:
                st.chat_message(msg["role"]).markdown(msg["content"])
        else:
            st.info("Commence par poser une question ou active ton micro 🎤")

# -----------------------------------------------------------------------------#
# 🛠️  CONVERSIONS                                                            #
# -----------------------------------------------------------------------------#
with tab_tools:
    st.markdown(
        "<h2 style='background: -webkit-linear-gradient(90deg, var(--primary), var(--primary-d));"
        " -webkit-background-clip: text; -webkit-text-fill-color: transparent;'>Outils de conversion</h2>",
        unsafe_allow_html=True,
    )
    st.write("Sélectionne un type de conversion puis remplis les champs.")

    tool = st.radio("Type", ["Unités", "Devises"], horizontal=True, index=0)

    if tool == "Unités":
        units = {
            "Mètres → Kilomètres": 0.001,
            "Kilomètres → Mètres": 1000,
            "Grammes → Kilogrammes": 0.001,
            "Kilogrammes → Grammes": 1000,
            "Centimètres → Mètres": 0.01,
            "Mètres → Centimètres": 100,
        }
        col_conv, col_val = st.columns(2)
        option = col_conv.selectbox("Conversion", list(units.keys()))
        value = col_val.number_input("Valeur", value=1.0)
        st.metric("Résultat", f"{value * units[option]:.4f}")
    else:
        col_from, col_to, col_amt = st.columns(3)
        from_cur = col_from.text_input("Source", "USD")
        to_cur   = col_to.text_input("Cible", "EUR")
        amount   = col_amt.number_input("Montant", value=1.0)

        if st.button("Convertir", key="convert_fx"):
            try:
                params = {"from": from_cur.upper(), "to": to_cur.upper(), "amount": amount}
                data = requests.get("https://api.exchangerate.host/convert", params=params, timeout=4).json()
                if (res := data.get("result")) is not None:
                    st.metric(f"Taux {from_cur.upper()}/{to_cur.upper()}", f"{res:.2f}")
                else:
                    st.error("Conversion impossible.")
            except requests.RequestException as e:
                st.error(f"Erreur API : {e}")

# -----------------------------------------------------------------------------#
# ℹ️  À PROPOS                                                               #
# -----------------------------------------------------------------------------#
with tab_about:
    st.markdown("### ℹ️ À propos de ChatAdam")
    st.markdown(
        """
        **ChatAdam** est un assistant interne basé sur un modèle **RAG** (*Retrieval-Augmented Generation*).  
        Il permet de poser des questions sur vos documents PDF, d’effectuer des conversions rapides d’unités
        ou de devises, et de lire les réponses à haute voix.  

        **Dernières améliorations** 📈  
        1. 📝 Ordre d’exécution corrigé : les réponses s’affichent immédiatement.  
        2. 🎤 Reconnaissance vocale améliorée, lecture de la réponse.  
        3. ✨ UI modernisée + mode sombre expérimental.  
        """
    )
