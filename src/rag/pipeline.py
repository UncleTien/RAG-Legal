from src.vectorstore.retriever import get_retriever
from src.llm.llm_wrapper import generate_answer

def query_rag(question: str, k: int = 3):
    retriever = get_retriever(k=k)
    docs = retriever.get_relevant_documents(question)
    context = "\n\n".join([d.page_content for d in docs])
    return generate_answer(question, context)
