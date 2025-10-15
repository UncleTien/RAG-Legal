import streamlit as st
from src.pipeline.rag_pipeline import RAGPipeline
import subprocess

def check_ollama_model(model_name="llama3"):
    """Check if Ollama model is available locally"""
    try:
        output = subprocess.check_output(["ollama", "list"]).decode("utf-8")
        return model_name in output
    except Exception:
        return False

def main():
    st.set_page_config(page_title="RAG-Legal Assistant", page_icon="⚖️", layout="wide")

    st.title("⚖️ RAG-Legal — AI Legal Assistant")
    st.markdown("""
    **RAG-Legal** is an AI-powered assistant that helps you query and understand the **2015 Civil Code of Vietnam**  
    using Retrieval-Augmented Generation (RAG) with **Ollama + LLaMA3**.
    """)

    if not check_ollama_model():
        st.warning("⚠️ Ollama model not found. Please run `ollama pull llama3` before using.")
        st.stop()

    # Initialize RAG pipeline
    rag = RAGPipeline()

    # Input field
    query = st.text_area("📝 Enter your legal question (Vietnamese or English):", height=100)

    if st.button("🔍 Analyze"):
        if not query.strip():
            st.error("Please enter a question.")
        else:
            with st.spinner("Analyzing your question..."):
                answer = rag.query(query)
            st.success("✅ Answer generated!")
            st.markdown("### 🧠 AI Assistant Response:")
            st.write(answer)

if __name__ == "__main__":
    main()
