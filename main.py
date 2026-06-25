#from app.llm.client import GeminiClient
from app.services.summarizer_service import SummarizerSevice
from app.chat.chat_service import Chat_Service


def main():
    
    #service = SummarizerSevice()

    #text = """ 
    #Los Large Language Models son modelos entrenados
    #sobre enormes cantidades de texto para predecir
    #el siguiente token de una secuencia.
    #"""
    #summary = service.summarize(text)
    #print(summary)
    
    c = Chat_Service()

    for i in range(3):
        p = input("tu turno de hablar: ")

        response = c.Send_Message(p)

        print(f"\nAsistente: {response}\n")
        


if __name__ == "__main__":
    main()

