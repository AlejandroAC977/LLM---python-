from app.services.chat_service import ChatService
from app.config.settings import settings
from app.loaders.pdf_loader import PdfLoader
from app.chunkers.text_chunker import TextChunker

import pandas as pd


def main():

    # --------------------------------------------------------------------------------------------------------------------
    # chunker completo y funcional:
    # # load = PdfLoader()
    # # lista_documents = load.load(r"C:\Users\alejandro\Documents\LLM-googleIA-studio\app\data\documents\informeFinal.pdf")

    # # chunker = TextChunker(settings.chunk_size, settings.chunk_overlap)
    # # lista_chunks = chunker.chunk(lista_documents)  
    # print(lista_chunks[12])
    # --------------------------------------------------------------------------------------------------------------------   

    c = ChatService()
    
    while True:
        p = input("Di Algo: ")
        if p.lower() == "exit":
                    break

        response = c.send_message(p)
        print(f"\nAsistente: {response}\n")
    

    
if __name__ == "__main__":
    main()

