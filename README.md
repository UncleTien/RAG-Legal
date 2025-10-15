# ⚖️ RAG-Legal: AI System for Vietnamese Legal Document Retrieval and Analysis

## 🧩 Project Overview

**RAG-Legal** is an AI Agent system designed to **automate the retrieval, summarization, and analysis of Vietnamese legal documents**.  
The project leverages the **RAG (Retrieval-Augmented Generation)** architecture combined with **LLaMA3 (via Ollama)** to deliver **context-aware, semantically grounded responses** to legal queries.

It aims to support **law students, legal practitioners, researchers, and citizens** in accessing and understanding Vietnamese laws more efficiently and accurately.

---

## 🧠 System Architecture

The RAG-Legal system consists of three main components:

1. **Data Loader (`src/data/loader.py`)**  
   - Reads and processes legal documents from formats such as DOCX, PDF, and TXT.  
   - Cleans, segments, and transforms the data into plain text for model consumption.

2. **Vector Store Builder (`scripts/build_vectorstore.py`)**  
   - Converts text segments into **vector embeddings** using the model `sentence-transformers/all-MiniLM-L6-v2`.  
   - Stores embeddings in **ChromaDB** for efficient semantic retrieval.

3. **RAG Pipeline (`src/pipeline/rag_pipeline.py`)**  
   - Accepts user questions and retrieves relevant text chunks from the vector store.  
   - Generates contextually accurate responses using **LLaMA3 through Ollama**.

---

## 🚀 How to Run the Project

### 📥 1. Clone the Repository

```bash
git clone https://github.com/UncleTien/RAG-Legal.git
cd RAG-Legal
```

---

### 🔧 2. Setup Environment

#### 🪟 On Windows:
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

#### 🍎 On macOS / Linux:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

### ⚙️ 3. Build the Vector Database

Generate semantic embeddings from the legal documents in `datasets/`:
```bash
python -m scripts.build_vectorstore --verbose
```

---

### 🤖 4. Run the RAG System

Execute the AI pipeline to query and analyze data:
```bash
python -m scripts.run_rag
```

Or launch the Streamlit user interface:
#### 💻 User Interface

RAG-Legal provides an intuitive **Streamlit web interface**, allowing users to input queries, choose legal documents, and view AI-generated answers directly in their browser.
```bash
streamlit run app.py
```

---

## 🧩 Project Structure

```
RAG-Legal/
│
├── app.py                     # Streamlit web interface
├── datasets/                  # Legal document dataset (e.g., luat_dan_su.docx)
├── data/vectorstore/          # Generated vector database
│
├── scripts/
│   ├── build_vectorstore.py   # Build vector embeddings
│   └── run_rag.py             # Run RAG pipeline
│
├── src/
│   ├── config/settings.py     # Project configuration
│   ├── data/loader.py         # Data loading & preprocessing
│   └── pipeline/rag_pipeline.py # Main RAG pipeline
│
├── requirements.txt
└── README.md
```

---

## 🧠 Core Technologies

- **LangChain + ChromaDB** – for the Retrieval-Augmented Generation (RAG) framework.  
- **Sentence Transformers (HuggingFace)** – for text vectorization and semantic search.  
- **Ollama + LLaMA3** – for natural language generation with contextual awareness.  
- **Streamlit** – for building an interactive, user-friendly frontend.  
- **Python 3.10+** – the primary programming language of the project.

---

## 💡 Practical Impact

RAG-Legal empowers users to:
- Quickly retrieve legal provisions and articles from Vietnamese laws.  
- Automatically summarize and interpret complex legal texts.  
- Build intelligent, context-aware legal Q&A systems.  
- Contribute to digital transformation and AI adoption in Vietnam’s legal domain.
