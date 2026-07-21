from google import genai
from app.config.settings import settings # dentro de config tengo settings donde creo toda la instancia de mi nombre de modelo y su apikey

class EmbeddingClient:
    def __init__(self):
        self.client = genai.Client(api_key=settings.GEMINI_API_KEY)
        self.model =  settings.GEMINI_EMBEDDING_MODEL
    
    def create_embedding(self, text: str):
        
        result = self.client.models.embed_content(
        model=self.model,
        contents=text,
        )