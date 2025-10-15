from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document

def split_documents(documents, chunk_size=1000, chunk_overlap=200):
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    out = []
    for doc in documents:
        parts = splitter.split_text(doc.page_content)
        for p in parts:
            out.append(Document(page_content=p, metadata=doc.metadata))
    return out
