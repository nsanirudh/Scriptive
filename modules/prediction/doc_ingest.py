import os
from typing import List
from pathlib import Path

import fitz  # PyMuPDF
import docx


def extract_text_from_pdf(file_path: str) -> str:
    """
    Extracts all text from a PDF using PyMuPDF.
    """
    text = []
    with fitz.open(file_path) as doc:
        for page in doc:
            text.append(page.get_text())
    return "\n".join(text)


def extract_text_from_docx(file_path: str) -> str:
    doc = docx.Document(file_path)
    return "\n".join(paragraph.text for paragraph in doc.paragraphs)


def extract_text_from_txt(file_path: str) -> str:
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()


def ingest_documents(paths: List[str]) -> str:
    """
    Given a list of file paths, extract and return concatenated text.
    """
    full_text = []

    for path in paths:
        ext = Path(path).suffix.lower()
        if ext == ".pdf":
            text = extract_text_from_pdf(path)
        elif ext == ".docx":
            text = extract_text_from_docx(path)
        elif ext == ".txt":
            text = extract_text_from_txt(path)
        else:
            raise ValueError(f"Unsupported file type: {ext}")

        full_text.append(text.strip())

    return "\n\n".join(full_text)


if __name__ == "__main__":
    files = [
        "/Users/ranjana/Documents/codes/personal_workspace/Scriptive/data/raw/user_docs/BlackHoleThermoShort.pdf"
    ]
    text = ingest_documents(files)
    print(text[:1000])
