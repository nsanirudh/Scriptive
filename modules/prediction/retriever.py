from typing import List, Dict
from qdrant_client import QdrantClient
from qdrant_client.models import Filter, SearchRequest
from modules.embeddings.embedder import TextEmbedder

class Retriever:
    def __init__(self, host: str = "localhost", port: int = 6333):
        self.qdrant = QdrantClient(host=host, port=port)
        self.embedder = TextEmbedder()

    def retrieve_relevant_chunks(
        self,
        channel_id: str,
        query: str,
        top_k: int = 5
    ) -> List[Dict]:
        """
        Returns top-k transcript chunks from a channel based on a topic query.
        """
        query_vector = self.embedder.embed_texts([query])[0]

        search_results = self.qdrant.search(
            collection_name=channel_id,
            query_vector=query_vector,
            limit=top_k
        )

        chunks = []
        for point in search_results:
            payload = point.payload
            chunks.append({
                "text": payload["text"],
                "video_id": payload.get("video_id"),
                "chunk_id": payload.get("chunk_id"),
                "score": round(point.score, 4)
            })

        return chunks

if __name__ == "__main__":
    retriever = Retriever()
    results = retriever.retrieve_relevant_chunks(
        channel_id="veritasium",
        query="Entropy and thermodynamics in black holes",
        top_k=3
    )

    for r in results:
        print(f"[{r['score']}] (Chunk {r['chunk_id']}) — {r['text'][:100]}...")
