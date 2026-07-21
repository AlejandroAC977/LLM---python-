from google import genai
from app.config.settings import settings # dentro de config tengo settings donde creo toda la instancia de mi nombre de modelo y su apikey

class GeminiClient:
    """ Cliente para interactuar con gemini """
    def __init__(self):
        self.client = genai.Client(api_key=settings.GEMINI_API_KEY)
        self.model =  settings.GEMINI_MODEL  # uso settings para llamar el modelo y la apikey y tomarlos como parametros de la clase

    def generate(self, prompt: str):
        """ generacion de respuestas a partir de un prompt """
        try:
            response = self.client.models.generate_content(
                model=self.model,
                contents=prompt,
            )
            return response.text
        except Exception as e:
            print(f"Error al llamar el LLM: {e}")
    
    