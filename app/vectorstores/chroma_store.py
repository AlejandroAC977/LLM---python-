import chromadb
from app.models.document_chunk import DocumentChunk

class ChromaStore:
    def __init__(self, collection_name: str = "documents"):
        self.client = chromadb.PersistentClient(path="./chroma_db")
        self.collection = self.client.get_or_create_collection(
            name = collection_name
        )


    def add_chunks(self, chunks: list[DocumentChunk], embeddings: list[list[float]])-> None:
        ids=[]
        documents=[]
        metadatas=[]

        for chunk in chunks:
            ids.append(f"chunk_{chunk.chunk_id}")
            documents.append(chunk.text)
            metadatas.append({
            "start_page": chunk.start_page if chunk.start_page is not None else 0,
            "end_page": chunk.end_page if chunk.end_page is not None else 0
            })

        self.collection.add(
            ids=ids,
            documents=documents,
            embeddings=embeddings,
            metadatas=metadatas)

    def show_all(self) -> None:
        data = self.collection.get()

        print("ids: ")
        print(data["ids"])

        print("\nDocuments:")
        print(data["documents"])

        print("\nMetadatas: ")
        print(data["metadatas"])

    def search(self, embedding: list[float], n_results: int = 5):
        results = self.collection.query(
            query_embeddings= [embedding],
            n_results=n_results
        )

        return results