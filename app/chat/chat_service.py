from app.chat.memory import ChatMemory
from app.prompt.chat_prompt_builder import ChatPromptBuilder
from app.llm.client import GeminiClient

class ChatService:
    def __init__(self):
        self.memory = ChatMemory()
        self.promp_builder = ChatPromptBuilder()
        self.llm = GeminiClient()

    def send_message(self, user_message: str)->str:
        messages = self.memory.get_messages()
        prompt = self.promp_builder.build_chat_prompt(messages, user_message)

        # temporal print del prompt 
        print(f"prompt entero enviado: \n {prompt} \n ------------------------------------")

        print(self.memory.get_messages())
        response = self.llm.generate(prompt)

        # Agregamos el mensaje del usario y del asistente al historial 
        self.memory.add_user_message(user_message)
        self.memory.add_assistant_message(response)
        
        return response
    
    