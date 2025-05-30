# 💼 ChatAdam – Chatbot d'entreprise avec RAG & interface vocale

[![Deploy on Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://chatbotfaqragopenai-wxy7on9id29afemtynd2v3.streamlit.app)

---

## 🚀 Description

ChatAdam est un assistant intelligent capable de répondre aux questions des collaborateurs d'une entreprise à partir de documents internes (PDF).  
Il utilise une architecture **RAG (Retrieval-Augmented Generation)** combinant recherche sémantique et génération de réponses via GPT-4.

💡 L'application est également capable :
- de transcrire la voix via **Whisper**
- de lire les réponses à voix haute (TTS)
- de convertir des unités & devises

🎓 Ce projet a été réalisé dans le cadre du module **NLP** de Ynov Campus.

---

## 🎯 Objectifs

- Interroger un ou plusieurs documents PDF internes
- Générer des réponses précises grâce à OpenAI GPT-4
- Utiliser une interface Streamlit claire, moderne et vocale
- Bonus : conversions d’unités et devises

---

## 🧱 Architecture technique

| Module                   | Usage                                                   |
|--------------------------|---------------------------------------------------------|
| **LangChain**            | Chaîne RAG (retrieval + génération)                     |
| **FAISS**                | Stockage vectoriel des chunks (⚠️ mémoire, sans persistence cross-session) |
| **OpenAI GPT-4**         | Génération des réponses                                 |
| **Whisper API**          | Transcription vocale                                    |
| **pyttsx3**              | Synthèse vocale (TTS)                                   |
| **Streamlit**            | Interface Web interactive                               |
| **streamlit-mic-recorder** | Enregistrement de la voix dans l'UI                   |

---

## 🧪 Fonctionnalités principales

- 📤 **Upload de documents PDF**
- 🧠 **Recherche intelligente** (RAG + embeddings)
- 💬 **Interface conversationnelle**
- 🎤 **Entrée vocale** avec Whisper
- 🔊 **Lecture vocale** des réponses
- 🌗 **Mode sombre**
- 🔧 **Outils de conversion**

---

## 🖥️ Lancer en local

1. Cloner le repo :

```bash
git clone https://github.com/Ahmat293/chatbot_faq_rag_openai.git
cd chatbot_faq_rag_openai


2. Créer un fichier `.env` :

```
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxx
```

3. Installer les dépendances :

```bash
pip install -r requirements.txt
```

4. Lancer :

```bash
streamlit run main.py
```

---

## 🎤 Fonctionnement du vocal (Whisper)

Pour poser une question à l'oral :
1. Clique sur le bouton **🎤 micro** dans l'onglet **Discussion**
2. Parle dans ton micro
3. Clique sur le bouton **🔴 rouge** pour arrêter l'enregistrement
4. Clique sur **Envoyer** pour déclencher la transcription
5. Le chatbot affiche la réponse ET peut la lire à voix haute (TTS)

> ⚠️ Assure-toi d'autoriser l'accès au micro sur ton navigateur.

---

## 🌍 Déploiement Streamlit Cloud

⚠️ ChromaDB nécessite `sqlite3 ≥ 3.35`.  
Streamlit Cloud ne supporte pas encore cette version → à remplacer par FAISS ou fallback léger.

🔗 Démo en ligne :  
https://chatbotfaqragopenai-wxy7on9id29afemtynd2v3.streamlit.app

---

## 📁 Structure du projet

```
chatbot_faq_rag_openai/
├── .env                      # Clé OpenAI
├── main.py                  # Interface principale Streamlit
├── document_loader.py       # Chargement + vectorisation PDF
├── rag_core.py              # Logique RAG
├── speech_to_text.py        # Transcription vocale
├── text_to_speech.py        # Lecture vocale des réponses
├── requirements.txt         # Dépendances
├── notebooks/               # TP1 à TP5
├── chroma_db/               # DB vectorielle (⚠️ local only)
└── .streamlit/
    └── secrets.toml         # Clé API pour déploiement
```

---

## 🧪 TP1 à TP5 inclus

✔️ Tous les TPs du module NLP sont inclus dans `notebooks/` :
- TP1 : Prétraitement
- TP2 : Embedding & réduction
- TP3 : Prompt Engineering
- TP4 : Amélioration des prompts
- TP5 : Similarité cosinus & euclidienne

---

## 👤 Auteur

**Ahmat Adam Goukouni**  
Alternant Data Analyst & IA chez 123elec  
GitHub : [@Ahmat293](https://github.com/Ahmat293)

---

## ✅ Statut du projet

Projet terminé, fonctionnel, déployé et prêt pour présentation.  
Accès partagé au professeur : `kevin.duranty@quera.fr`