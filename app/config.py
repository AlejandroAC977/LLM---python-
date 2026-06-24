import os 
from dotenv import load_dotenv  

load_dotenv()

class Settings:
    """ centraliza la configuaracion de la app """
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    GEMINI_MODEL = "gemini-2.5-flash"

settings = Settings()

