from app.vectorstores.chroma_store import ChromaStore
from app.embeddings.embedding_client import EmbeddingClient

class Retriver:
    def __init__(
        self, 
        embedding_client: EmbeddingClient,
        vector_store: ChromaStore
    ):
        self.embedding_client = embedding_client
        self.vector_store = vector_store

    def retrive(self, query: str, n_results: int = 5):
