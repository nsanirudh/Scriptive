import os
import argparse
from pathlib import Path

from modules.processing.clean_text import clean_transcript
from modules.processing.chunk_text import chunk_text
from modules.embeddings.embedder import TextEmbedder
from modules.embeddings.indexer import QdrantIndexer

def read_transcript(file_path: str) -> str:
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def embed_channel_transcripts(channel_id: str, transcript_dir: str = "data/processed/transcripts"):
    transcript_files = list(Path(transcript_dir).glob("*.txt"))
    if not transcript_files:
        print("[ERROR] No transcripts found.")
        return

    print(f"[INFO] Found {len(transcript_files)} transcripts.")

    embedder = TextEmbedder()
    indexer = QdrantIndexer(collection_name=channel_id)

    for file_path in transcript_files:
        video_id = file_path.stem
        text = read_transcript(str(file_path))
        cleaned = clean_transcript(text)

        chunks = chunk_text(cleaned, max_words=100, overlap=20)
        texts = [chunk["text"] for chunk in chunks]
        vectors = embedder.embed_texts(texts)

        metadata_list = [
            {
                "video_id": video_id,
                "chunk_id": chunk["chunk_id"],
                "start_word": chunk["start_word"],
                "end_word": chunk["end_word"],
            }
            for chunk in chunks
        ]

        indexer.index_documents(texts, vectors, metadata_list)
        print(f"[INFO] Embedded {len(texts)} chunks for video: {video_id}")

    print(f"[SUCCESS] All transcripts for channel '{channel_id}' embedded into Qdrant.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Embed transcripts into Qdrant")
    parser.add_argument("--channel_id", type=str, required=True, help="Channel ID for Qdrant collection")
    args = parser.parse_args()

    embed_channel_transcripts(channel_id=args.channel_id)
