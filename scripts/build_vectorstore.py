import sys, os
# Ensure project root in PYTHONPATH when run as module
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.data.loader import load_documents
from src.data.splitter import split_documents
from src.vectorstore.build_vectorstore import create_vectorstore
from src.config.settings import settings

def main():
    docs_path = os.getenv('DOCS_PATH', settings.docs_path)
    print('Loading documents from', docs_path)
    docs = load_documents(docs_path)
    print('Loaded', len(docs), 'documents')
    chunks = split_documents(docs)
    print('Created', len(chunks), 'chunks')
    db = create_vectorstore(chunks)
    print('✅ Vectorstore created (persist directory):', settings.persist_directory)

if __name__ == '__main__':
    main()
