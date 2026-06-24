from app.llm.client import GeminiClient
from app.prompt.builder import PromptBuilder

class SummarizerSevice:
    def __init__(self):
        self.llm = GeminiClient()
        self.prompt_builder = PromptBuilder()

    def summarize(self, text: str) -> str:
        prompt = self.prompt_builder.build_summary_prompt(text)
        response = self.llm.generate(prompt)

        return response