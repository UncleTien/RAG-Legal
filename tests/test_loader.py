from src.data.loader import load_documents
def test_loader_runs():
    docs = load_documents('data/rag')
    assert isinstance(docs, list)
