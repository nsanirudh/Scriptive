from modules.embeddings.embedder import TextEmbedder
from modules.embeddings.indexer import QdrantIndexer

# Example transcript chunks
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
