from google import genai
from app.config import settings

class GeminiClient:
    """ Cliente para interactuar con gemini """
    def __init__(self):
        self.client = genai.Client(api_key=settings.GEMINI_API_KEY)
        self.model =  settings.GEMINI_MODEL

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
    
    