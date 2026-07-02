from dataclasses import dataclass

@dataclass
class DocumentChunk:
    text: str
    chunk_id: int 
    start_page: int 
    end_page: int 
    metadata: dict