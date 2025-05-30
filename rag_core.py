from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv
import os

load_dotenv()

DB_FOLDER = "faiss_db"

def ask_question(question, vectorstore_name):
    """
    🔎 Pose une question au document sélectionné
    """
    doc_db_folder = os.path.join(DB_FOLDER, vectorstore_name)
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.load_local(
        doc_db_folder,
        embeddings,
        allow_dangerous_deserialization=True
    )

    retriever = vectorstore.as_retriever()
    llm = ChatOpenAI(temperature=0, model="gpt-4o")

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff"
    )

    print(f"📥 Question : {question} sur ➡️ {vectorstore_name}")
    result = qa_chain.invoke(question)
    print(f"📤 Réponse : {result}")
    return result
