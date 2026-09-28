from app.models.document_chunk import DocumentChunk
from app.models.document_page import DocumentPage
from app.config.settings import settings
from app.loaders.pdf_loader import PdfLoader
from app.models.pageindex import PageIndex

class TextChunker:
    def __init__(self, chunk_size: int, chunk_overlap: int):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def chunk(self, pages: list[DocumentPage]) -> list[DocumentChunk]:
        # Creacion del texto completo en una lista por pagina
        texto_unido = []
        for page in pages:
            texto_unido.append(page.text)

        texto_completo = "\n".join(texto_unido)
        #print(texto_completo)

        # PageIndex 
        # Variables de Apoyo
        lst_index = []
        inicio = 0
        for i, page in enumerate(pages):
            largo = len(page.text)
            pageIdx = PageIndex(page_number= i+1, start_char=inicio, end_char=inicio + largo)
            lst_index.append(pageIdx)
            inicio += largo + 1


        # chunk final
        # Variables De Ayuda
        start= 0
        chunks = []
        contador_id = 1
        
        while start < len(texto_completo):
            s = None
            e = None
            texto_chunk = ""
            end = min(
                start + self.chunk_size,
                len(texto_completo)
                )
            
            texto_chunk = texto_completo[start:end] 
            for idx in lst_index:
                if start >= idx.start_char and start < idx.end_char:
                    s = idx.page_number
                if (end - 1) >= idx.start_char and (end - 1) < idx.end_char:
                    e = idx.page_number
                if s is not None and e is not None:
                    break

            chunk_obj = DocumentChunk(text = texto_chunk, chunk_id=contador_id,
                                        start_page=s, end_page=e, metadata={})
            chunks.append(chunk_obj) 
            
            contador_id +=1
            start += self.chunk_size - self.chunk_overlap
            #start += end
        #return de la lista de objetos chunks
        return chunks