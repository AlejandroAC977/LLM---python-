from app.models.document_chunk import DocumentChunk
import re


def contextBuilder(doc: list[DocumentChunk]) -> str:
    parts = []
    for i, d in enumerate(doc):
        text = f"""[Fragmento {i+1} | Páginas {d.start_page}-{d.end_page}]\n
                    {d.text}
                """

        parts.append(text)

    text_f = "\n\n".join(parts)
    text_f = re.sub(r"[ \t]*\n[ \t]*", "\n", text_f)
    text_f = re.sub(r"\n{2,}", "\n", text_f)

    return text_f.strip()
            
