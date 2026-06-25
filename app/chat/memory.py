class ChatMemory:
    def __init__(self):
        self.messanges = []

    def add_user_message(self, message: str):
        self.messanges.append({
            "role": "user",
            "content": message
        })
    def add_assistant_message(self, message: str):
        self.messanges.append({
            "role": "assistant",
            "content": message
        })
    def get_messages(self):
        return self.messanges