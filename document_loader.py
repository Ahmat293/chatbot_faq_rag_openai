import os
import pdfplumber
from dotenv import load_dotenv
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma  # ✅ nouveau import

load_dotenv()

DATA_FOLDER = "data"
DB_FOLDER = "chroma_db"


def load_pdf(file_path):
    with pdfplumber.open(file_path) as pdf:
        return "\n".join(page.extract_text() or "" for page in pdf.pages)


def split_text(text, chunk_size=1000, chunk_overlap=200):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    return splitter.split_text(text)


def load_and_vectorize_document(pdf_path, vectorstore_name):
    """
    📥 Charge le PDF, le découpe et crée un vectorstore dans chroma_db/{vectorstore_name}
    """
    print(f"📄 Chargement du document : {pdf_path}")
    raw_text = load_pdf(pdf_path)
    chunks = split_text(raw_text)
    print(f"🔹 {len(chunks)} morceaux générés.")
    print(f"🔹 Exemple chunk : {chunks[0][:200]}")

    # 🔧 Nouveau dossier pour chaque document
    doc_db_folder = os.path.join(DB_FOLDER, vectorstore_name)
    if os.path.isdir(doc_db_folder) and os.listdir(doc_db_folder):
        print("✅ Index déjà présent, on ne le reconstruit pas.")
        return
    os.makedirs(doc_db_folder, exist_ok=True)

    embeddings = OpenAIEmbeddings()
    vectorstore = Chroma.from_texts(
        texts=chunks,
        embedding=embeddings,
        persist_directory=doc_db_folder
    )
    return vectorstore
