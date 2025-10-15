from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.llms import Ollama
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from src.config.settings import settings

class RAGPipeline:
    def __init__(self):
        """Initialize RAG pipeline components"""
        self.embedding_model = HuggingFaceEmbeddings(model_name=settings.embedding_model)

        # Load Chroma vector database
        self.vectorstore = Chroma(
            persist_directory=settings.VECTORSTORE_DIR,
            embedding_function=self.embedding_model
        )

        self.retriever = self.vectorstore.as_retriever(search_kwargs={"k": 3})

        # Initialize Ollama LLM (LLaMA3)
        self.llm = Ollama(model=settings.llm_model)

        # Build QA Chain
        template = """
        You are a legal assistant specialized in Vietnamese civil law.
        Use the retrieved context to answer the user's question precisely.
        If unsure, say "I don't know" — do not make up an answer.

        Context: {context}
        Question: {question}

        Answer in Vietnamese:
        """
        prompt = PromptTemplate(template=template, input_variables=["context", "question"])

        self.qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff",
            retriever=self.retriever,
            chain_type_kwargs={"prompt": prompt},
            return_source_documents=False
        )

    def query(self, question: str) -> str:
        """Query the system and return an AI-generated legal answer"""
        response = self.qa_chain.run(question)
        return response
