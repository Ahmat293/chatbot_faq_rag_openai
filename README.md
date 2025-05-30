
# 💼 ChatAdam – Chatbot d'entreprise avec RAG & interface vocale

---

## 🚀 Description

ChatAdam est un assistant intelligent conçu pour répondre aux questions des collaborateurs à partir de documents internes (PDF).  
Il repose sur une architecture **RAG (Retrieval-Augmented Generation)** combinée à la puissance de **GPT-4**.

💡 Fonctions incluses :
- Recherche intelligente dans les PDF avec embeddings
- Transcription vocale via **Whisper**
- Lecture des réponses à voix haute (TTS)
- Conversion rapide d’unités et de devises

🎓 Projet réalisé dans le cadre du module **NLP** de Ynov Campus.

---

## 🎯 Objectifs

- Permettre l’interrogation de documents internes PDF
- Générer des réponses précises et contextualisées
- Offrir une interface web conviviale et moderne avec **Streamlit**
- Intégrer des options vocales pour accessibilité et fluidité
- Fournir des outils bonus comme les conversions intégrées

---

## 🧱 Architecture technique

| Module                        | Usage                                                   |
|-------------------------------|---------------------------------------------------------|
| **LangChain**                 | Chaîne RAG (retrieval + génération)                     |
| **FAISS**                     | Stockage vectoriel des chunks (⚠️ compatible cloud)     |
| **OpenAI GPT-4**              | Génération des réponses                                 |
| **OpenAI Whisper API**        | Transcription vocale                                    |
| **pyttsx3**                   | Synthèse vocale (TTS)                                   |
| **Streamlit**                 | Interface Web interactive                               |
| **streamlit-mic-recorder**    | Enregistrement vocal dans l’interface                  |

---

## 🧪 Fonctionnalités principales

- 📤 Upload de documents PDF
- 🧠 Recherche sémantique (RAG + embeddings)
- 💬 Interface conversationnelle moderne
- 🎤 Entrée vocale (Whisper)
- 🔊 Lecture vocale des réponses
- 🌗 Mode sombre (expérimental)
- 🔧 Outils de conversion (unités & devises)

---

## 🖥️ Lancer en local

1️⃣ **Cloner le projet :**
```bash
git clone https://github.com/Ahmat293/chatbot_faq_rag_openai.git
cd chatbot_faq_rag_openai
```

2️⃣ **Créer le fichier `.env` :**
```
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxx
```

3️⃣ **Installer les dépendances :**
```bash
pip install -r requirements.txt
```

4️⃣ **Lancer l’application :**
```bash
streamlit run main.py
```

---

## 🌍 Déploiement Streamlit Cloud

✅ Version FAISS compatible Cloud (sqlite limitations contournées).

🔗 Lien démo en ligne :  
https://chatbotfaqragopenai-wxy7on9id29afemtynd2v3.streamlit.app

> Si besoin, cliquer sur **Reboot** dans Streamlit Cloud pour tirer les dernières modifications après un push Git.

---

## 📁 Structure du projet

```
chatbot_faq_rag_openai/
├── .env                      # Clé API OpenAI
├── main.py                   # Interface principale Streamlit
├── document_loader.py        # Chargement + vectorisation PDF
├── rag_core.py               # Logique RAG
├── speech_to_text.py         # Transcription vocale
├── text_to_speech.py         # Lecture vocale (TTS)
├── requirements.txt          # Dépendances
├── notebooks/                # Travaux pratiques
├── chroma_db/ (local)        # Ancienne DB (remplacée par FAISS)
└── .streamlit/
    └── secrets.toml          # Clé API pour déploiement cloud
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

---

## 🎤 Fonctionnement vocal

1. Clique sur le micro **🎤** pour enregistrer une question.  
2. Clique sur le bouton rouge **🔴** pour arrêter l’enregistrement.  
3. Clique sur **Envoyer** pour lancer la transcription et recevoir une réponse (écrite + vocale).

> Assure-toi d’avoir donné les autorisations micro au navigateur.

---

## 👤 Auteur

**Ahmat Adam Goukouni**  
Alternant Data Analyst & IA chez 123elec  
GitHub : [@Ahmat293](https://github.com/Ahmat293)

---

## ✅ Statut du projet

✅ Projet fonctionnel, déployé, prêt à la démonstration.  
Dernières optimisations : compatibilité cloud FAISS, améliorations CSS, nettoyage du repo.

