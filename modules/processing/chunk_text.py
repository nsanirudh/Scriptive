import re
from typing import List, Dict

def chunk_text(
    text: str,
    max_words: int = 100,
    overlap: int = 20
) -> List[Dict]:
    """
    Splits transcript text into overlapping chunks based on word count.
    Returns a list of dicts with chunk metadata.
    """
    words = text.split()
    chunks = []
    start = 0
    chunk_id = 1

    while start < len(words):
        end = min(start + max_words, len(words))
        chunk_words = words[start:end]
        chunk_text = " ".join(chunk_words)

        chunks.append({
            "chunk_id": chunk_id,
            "text": chunk_text,
            "start_word": start,
            "end_word": end
        })

        start += max_words - overlap
        chunk_id += 1

    return chunks

if __name__ == "__main__":
    long_transcript = """
    Thermodynamics is a branch of physics that deals with heat and temperature and their relation to energy and work.
    The behavior of these quantities is governed by the four laws of thermodynamics...
    (Imagine this is 1000+ words)
    """

    chunks = chunk_text(long_transcript, max_words=50, overlap=10)

    for c in chunks[:2]:  # Show just first 2 chunks
        print(f"Chunk {c['chunk_id']}:")
        print(c['text'])
        print("—" * 40)
