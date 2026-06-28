from pypdf import PdfReader
from app.models.document_page import DocumentPage

class PdfLoader:
    def load(self, path: str) -> list[DocumentPage]:
        pages : list[DocumentPage] = []

        reader = PdfReader(path)
        for p, page in enumerate(reader.pages, start=1):
            text = page.extract_text() or ""
            page_obj = DocumentPage(page_number=p, text= text) 
            pages.append(page_obj)
        

        return pages