import os 
from dotenv import load_dotenv  

load_dotenv()

class Settings:
    def __init__(self):
        """ centraliza la configuaracion de la app """
        self.GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
        self.GEMINI_MODEL = "gemini-2.5-flash"

settings = Settings()

