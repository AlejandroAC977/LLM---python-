from app.llm.client import GeminiClient
from app.prompt.builder import PromptBuilder

""" Esta clase funciona como un orquestador de las demas funciones provinientes de client.py y builder.py (las ejecuta en conjunto) """
class SummarizerSevice:
    def __init__(self):
        self.llm = GeminiClient()
        self.prompt_builder = PromptBuilder()

    def summarize(self, text: str) -> str:
        prompt = self.prompt_builder.build_summary_prompt(text)
        response = self.llm.generate(prompt)

        return response