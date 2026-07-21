from app.llm.client import GeminiClient
from app.services.summarizer_service import SummarizerSevice
from app.services.chat_service import ChatService

from app.models.document_chunk import DocumentChunk
from app.models.document_page import DocumentPage
from app.config.settings import settings
from app.loaders.pdf_loader import PdfLoader
from app.chunkers.text_chunker import TextChunker

import pandas as pd

def main():
    
    # Primer Prueba 
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
    

#Prueba tecnica, implementacion del modelo para clasificar respuestas
    # c = GeminiClient()
    # df = pd.read_csv(r"C:\Users\alejandro\Documents\LLM-googleIA-studio\app\data\documents\mat-apoyo.csv")
    # df["Clasificación"] = ""

    # for iteracion, fila in df.iterrows():
    #     resp = fila["respuesta"]
    #     pr = f"""
    #         Eres un analista de datos experto en experiencia del cliente.
    #         Tu tarea es analizar la respuesta a la pregunta "¿Qué tan satisfecho estás con el servicio de atención al cliente?".

    #         Usa solo una de estas tres categorias:
    #         - Positivo 
    #         - Negativo 
    #         - Neutro
    #         Regla estricta: Responde solo con la palabra de la categoría (ej. "Positivo"). No agregues puntos, saludos ni explicaciones.

    #         Respuesta: {resp}
    #         """
    #     rfinal = c.generate(prompt=pr)
    #     df.loc[iteracion, "Clasificación"] = rfinal

    # df.head()
    # df.to_csv("C:/Users/alejandro/Downloads/mat-apoyo-completo.csv", index=False)

    load = PdfLoader()
    lista_documents = load.load(r"C:\Users\alejandro\Documents\LLM-googleIA-studio\app\data\documents\informeFinal.pdf")

    chunker = TextChunker(settings.chunk_size, settings.chunk_overlap)
    lista_chunks = chunker.chunk(lista_documents)  
    print(lista_chunks[12])
    
if __name__ == "__main__":
    main()

