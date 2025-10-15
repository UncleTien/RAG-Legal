from src.config.settings import settings
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

def get_retriever(persist_directory=None, k=3):
    if persist_directory is None:
        persist_directory = settings.persist_directory
    embedder = HuggingFaceEmbeddings(model_name=settings.embedding_model)
    db = Chroma(persist_directory=persist_directory, embedding_function=embedder)
    return db.as_retriever(search_kwargs={'k': k})
