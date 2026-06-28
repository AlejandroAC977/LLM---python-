class PromptBuilder:

    def build_summary_prompt(self, text: str):
        return f"""
                Eres un asistente especializado en resumir textos.

                Tu objetivo es producir un resumen claro, preciso y fiel al contenido.

                Reglas:
                - No inventes información.
                - Conserva únicamente las ideas principales.
                - Si el texto es muy largo, limita el resumen a un máximo de tres párrafos.
                - Usa un lenguaje claro y amable.
                - Escribe el resultado en párrafos.

                Texto a resumir:
                
                -----------------------
                {text}
                -----------------------
                """