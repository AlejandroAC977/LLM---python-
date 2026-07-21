from dataclasses import dataclass

@dataclass
class PageIndex:
    page_number: int
    start_char: int
    end_char: int