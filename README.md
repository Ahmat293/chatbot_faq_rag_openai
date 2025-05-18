💼 ChatAdam – Chatbot d'entreprise avec RAG & interface vocale
🚀 Description
ChatAdam est un assistant intelligent capable de répondre aux questions des collaborateurs d'une entreprise en s'appuyant sur les documents internes (au format PDF). Il utilise une architecture de type RAG (Retrieval-Augmented Generation), combinant des capacités de recherche documentaire et de génération de texte, avec en plus une interface utilisateur conviviale, un micro pour poser des questions vocales, et un système de lecture vocale des réponses.
Ce projet a été réalisé dans le cadre du module NLP (Natural Language Processing) avec l'objectif de démontrer l'utilisation des techniques modernes d'IA générative dans une application réelle d'entreprise.
________________


🎯 Objectifs
* Offrir un chatbot capable de comprendre une question et d'aller chercher une réponse dans des documents PDF internes.

* Gérer le langage naturel avec OpenAI.

* Fournir une interface Web avec Streamlit, incluant une expérience utilisateur riche :

   * Upload de documents(un ou plusieurs documents, deux pdfs exemple dans le dossier data)

   * Sélection dynamique

   * Chat textuel

   * Transcription audio (via Whisper)

   * Synthèse vocale des réponses

   * Conversion unités / devises (bonus)
Pour faire fonctionner le vocal, appuyer sur l’icône micro parler, réappuyer sur l'icône point rouge et appuyer sur envoyé.

________________


🧱 Architecture technique
      * LangChain : construction de la chaîne RAG

      * ChromaDB : stockage vectoriel local des documents PDF (avec persistance)

      * OpenAI / Mistral : modèles de LLM pour génération de texte

      * Whisper API : pour la transcription vocale des questions posées à l'oral

      * Streamlit : interface Web moderne et interactive

      * Pyttsx3 : pour lire les réponses à haute voix (TTS)

      * streamlit-mic-recorder : module pour enregistrer la voix directement depuis l'interface

________________


🧪 Fonctionnalités principales
Fonctionnalité
	Description
	Upload de documents PDF
	Chargement de documents internes
	Vectorisation automatique
	Embedding des textes avec OpenAI & stockage dans ChromaDB
	Recherche intelligente (RAG)
	Récupération de contexte + génération par LLM
	Interface conversationnelle textuelle
	Poser une question et recevoir une réponse avec mémoire
	Transcription vocale (Whisper)
	Possibilité de poser une question à l'oral
	Lecture de la réponse à haute voix (TTS)
	Synthèse vocale de la réponse pour accessibilité
	Mode sombre / clair
	UI adaptée (optionnelle)
	Conversions bonus
	Onglet de conversion unités et devises (API externe)
	________________


🖥️ Lancer le projet en local
1. Cloner le repo
git clone https://github.com/Ahmat293/chatbot_faq_rag_openai.git
cd chatbot_faq_rag_openai


2. Créer un fichier .env
Créer un fichier .env à la racine avec le contenu suivant :
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxx


3. Installer les dépendances
Assurez-vous d'avoir Python >= 3.9 :
pip install -r requirements.txt


4. Lancer l'application
streamlit run main.py


________________


🌍 Déploiement sur Streamlit Cloud
         1. Aller sur https://streamlit.io/cloud

         2. Connecter son compte GitHub et choisir le repo

         3. Ajouter un fichier .streamlit/secrets.toml :

[openai]
api_key = "sk-xxxxxxxxxxxxxxxxxxxxxxxx"


            4. Cliquer sur Deploy !











________________


📁 Structure du projet
chatbot_faq_rag_openai/
├── .env                      # Clés d’API (non commité)
├── main.py                  # Interface principale Streamlit
├── document_loader.py       # Chargement + vectorisation PDF
├── rag_core.py              # Logique RAG (retrieval + LLM)
├── speech_to_text.py        # Transcription vocale (Whisper)
├── text_to_speech.py        # Lecture vocale des réponses
├── requirements.txt         # Librairies
├── notebooks/               # TP1 à TP5
├── chroma_db/               # DB vectorielle persistante
├── data/                    # Dossiers de documents
└── .streamlit/
    └── secrets.toml         # Clé API pour le déploiement cloud


________________


📚 Travaux pratiques inclus (TP1 à TP5)
            * Tous les TPs du module NLP sont présents dans le dossier notebooks/ :

               * TP1 : Prétraitement de textes

               * TP2 : Embedding & réduction de dimension

               * TP3 : Prompt Engineering

               * TP4 : Amélioration des prompts

               * TP5 : Similarité de textes (cosine / euclidienne)

________________


👨‍💻 Auteur
Ahmat Adam – GitHub @Ahmat293
Alternant Data Analyst / IA chez 123elec
________________


✅ Statut du projet
Projet terminé et fonctionnel.