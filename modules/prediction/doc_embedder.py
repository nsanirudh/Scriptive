import uuid
from typing import List, Dict

from modules.processing.clean_text import clean_transcript
from modules.processing.chunk_text import chunk_text
from modules.embeddings.embedder import TextEmbedder
from modules.embeddings.indexer import QdrantIndexer

class UserDocEmbedder:
    def __init__(self, session_id: str = None):
        self.session_id = session_id or str(uuid.uuid4())
        self.collection_name = f"user_context_{self.session_id}"
        self.embedder = TextEmbedder()
        self.indexer = None  # Lazy init after vector size is known

    def embed_user_text(self, text: str) -> str:
        """
        Cleans, chunks, embeds and indexes the user-provided text.
        Returns the Qdrant collection name used.
        """
        cleaned = clean_transcript(text)
        chunks = chunk_text(cleaned, max_words=100, overlap=20)

        texts = [chunk["text"] for chunk in chunks]
        vectors = self.embedder.embed_texts(texts)

        if self.indexer is None:
            dim = len(vectors[0])
            self.indexer = QdrantIndexer(collection_name=self.collection_name, dim=dim)

        metadata_list = [
            {
                "chunk_id": chunk["chunk_id"],
                "start_word": chunk["start_word"],
                "end_word": chunk["end_word"],
            }
            for chunk in chunks
        ]

        self.indexer.index_documents(texts, vectors, metadata_list)

        return self.collection_name

if __name__ == "__main__":
    from modules.prediction.doc_ingest import ingest_documents

    files = [
        "/Users/ranjana/Documents/codes/personal_workspace/Scriptive/data/raw/user_docs/BlackHoleThermoShort.pdf"
    ]
    text = ingest_documents(files)

    embedder = UserDocEmbedder()
    collection = embedder.embed_user_text(text)

    print(f"[INFO] Embedded context into: {collection}")

# from qdrant_client import QdrantClient
# client = QdrantClient("localhost", port=6333)
# client.delete_collection(collection_name="user_context_<id>")
