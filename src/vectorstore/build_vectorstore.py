from src.config.settings import settings
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
import os

def create_vectorstore(documents, persist_directory=None):
    if persist_directory is None:
        persist_directory = settings.persist_directory
    os.makedirs(persist_directory, exist_ok=True)
    embedder = HuggingFaceEmbeddings(model_name=settings.embedding_model)
    db = Chroma.from_documents(documents, embedding=embedder, persist_directory=persist_directory)
    # Chroma auto-persists in newer versions
    return db
