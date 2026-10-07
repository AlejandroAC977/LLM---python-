from app.vectorstores.chroma_store import ChromaStore
from app.embeddings.embedding_client import EmbeddingClient
from app.models.document_chunk import DocumentChunk

class Retriver:
    def __init__(
        self, 
        embedding_client: EmbeddingClient,
        vector_store: ChromaStore
    ):
        self.embedding_client = embedding_client
        self.vector_store = vector_store

    def retrive(self, query: str, n_results: int = 3):
        embedd = self.embedding_client.create_embedding(query)
        search = self.vector_store.search(embedd, n_results= n_results)

        lista_dc = self.parse_dict(search)

        return lista_dc

    def parse_dict(self, search: dict)-> list[DocumentChunk]:
        chunks = []

        ids = search["ids"][0]
        documents = search["documents"][0]
        metadatas = search["metadatas"][0]

        for chunk_id, text, metadata in zip(
            ids,
            documents,
            metadatas
        ):
            chunk = DocumentChunk(
                text=text,
                chunk_id=int(chunk_id.split("_")[1]),
                start_page=metadata["start_page"],
                end_page=metadata["end_page"],
                metadata={}
            )

            chunks.append(chunk)
    
        return chunks