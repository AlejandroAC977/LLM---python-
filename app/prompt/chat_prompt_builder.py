from app.chat.memory import ChatMemory

class ChatPromptBuilder:
    def build_chat_prompt(
            self,
            messages: list[dict],
            user_message: str
    ) -> str:
        history_text = ""
        for message in messages:
            role = message["role"]
            content = message["content"]

            if role == "user":
                history_text += f"usuario: \n {content}\n\n"
            elif role == "assistant":
                history_text += f"Asistente: \n {content}\n\n"
        return F"""
        Eres un asistente útil y profesional.

        Tu objetivo es responder usando el contexto de la conversación.

        Historial de conversación:

        {history_text}

        Pregunta actual:

        {user_message}

        Responde de forma clara y precisa.   
            """