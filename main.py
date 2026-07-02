from app.llm.client import GeminiClient
from app.services.summarizer_service import SummarizerSevice
from app.services.chat_service import ChatService

from app.models.document_chunk import DocumentChunk
from app.models.document_page import DocumentPage
from app.config.settings import settings
from app.loaders.pdf_loader import PdfLoader
from app.chunkers.text_chunker import TextChunker

def main():
    
    #service = SummarizerSevice()

    #text = """ 
    #Los Large Language Models son modelos entrenados
    #sobre enormes cantidades de texto para predecir
    #el siguiente token de una secuencia.
    #"""
    #summary = service.summarize(text)
    #print(summary)
    

    """
    c = ChatService()

    for i in range(3):
        p = input("tu turno de hablar: ")

        response = c.send_message(p)

        print(f"\nAsistente: {response}\n")
    """


    load = PdfLoader()
    lista_documents = load.load(r"C:\Users\alejandro\Documents\LLM-googleIA-studio\app\data\documents\informeFinal.pdf")

    chunker = TextChunker(settings.chunk_size, settings.chunk_overlap)
    chunker.chunk(lista_documents)  


if __name__ == "__main__":
    main()

