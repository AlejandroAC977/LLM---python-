from pypdf import PdfReader
from app.models.document_page import DocumentPage

class PdfLoader:
    """ Lee el pdf y regresa cada pagina como un objeto con el texto y el numero de pagina, con esto tendremos una lista de estos ojetos """
    def load(self, path: str) -> list[DocumentPage]:
        pages : list[DocumentPage] = []  # nuestra lista de pagina

        reader = PdfReader(path)
        for p, page in enumerate(reader.pages, start=1):
            text = page.extract_text() or ""
            page_obj = DocumentPage(page_number=p, text= text) 
            pages.append(page_obj)
        

        return pages