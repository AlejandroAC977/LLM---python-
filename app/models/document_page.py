from dataclasses import dataclass

@dataclass
class DocumentPage:
    page_number: int
    text: str


"""
page = DocumentPage(
    page_number=1,
    text="Hola mundo"
)

print(page)
"""