from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    embedding_model: str = "sentence-transformers/all-MiniLM-L6-v2"
    llm_model: str = "llama3"
    VECTORSTORE_DIR: str = "data/vectorstore"

    class Config:
        env_file = ".env"

settings = Settings()
