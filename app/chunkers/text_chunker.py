from app.models.document_chunk import DocumentChunk
from app.models.document_page import DocumentPage
from app.config.settings import settings
from app.loaders.pdf_loader import PdfLoader

class TextChunker:
    def __init__(self, chunk_size: int, chunk_overlap: int):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def chunk(self, pages: list[DocumentPage]) -> list[DocumentChunk]:
        texto_unido = []
        for page in pages:
            texto_unido.append(page.text)

        texto_completo = "\n".join(texto_unido)
        print(texto_completo)
        
        start= 0
        while start > len(texto_completo):
            texto_chunk = ""
            end = min(
                start + self.chunk_size,
                len(texto_completo)
                )
            
            texto_chunk = texto_completo[start:end]