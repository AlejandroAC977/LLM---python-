from app.llm.client import GeminiClient
from app.services.summarizer_service import SummarizerSevice


def main():
    service = SummarizerSevice()

    text = """ 
    Los Large Language Models son modelos entrenados
    sobre enormes cantidades de texto para predecir
    el siguiente token de una secuencia.
    """
    summary = service.summarize(text)
    print(summary)


if __name__ == "__main__":
    main()

