from modules.embeddings.embedder import TextEmbedder
from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct, Distance, VectorParams
from typing import List, Dict
import uuid


class QdrantIndexer:
    def __init__(self, collection_name: str = "youtube_scripts", dim: int = 384):
        self.client = QdrantClient(host="localhost", port=6333)
        self.collection_name = collection_name
        self.dim = dim

        self.client.recreate_collection(
            collection_name=self.collection_name,
            vectors_config=VectorParams(size=dim, distance=Distance.COSINE)
        )

    def index_documents(self, texts: List[str], embeddings: List[List[float]], metadata_list: List[Dict]):
        """
        Index documents into Qdrant with corresponding metadata.
        """
        points = []
        for text, embedding, metadata in zip(texts, embeddings, metadata_list):
            points.append(
                PointStruct(
                    id=str(uuid.uuid4()),
                    vector=embedding,
                    payload={**metadata, "text": text}
                )
            )

        self.client.upsert(
            collection_name=self.collection_name,
            points=points
        )

if __name__ == "__main__":

    texts = [
        "This video explores the concept of entropy in thermodynamics...",
        "In the next section, we look at how entropy applies to black holes..."
    ]

    # Corresponding metadata
    metadata = [
        {"video_id": "abc123", "segment_id": 1, "title": "Entropy Explained"},
        {"video_id": "abc123", "segment_id": 2, "title": "Entropy Explained"},
    ]

    embedder = TextEmbedder()
    vectors = embedder.embed_texts(texts)

    indexer = QdrantIndexer()
    indexer.index_documents(texts, vectors, metadata)
