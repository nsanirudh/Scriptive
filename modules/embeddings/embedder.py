from sentence_transformers import SentenceTransformer
from typing import List

class TextEmbedder:
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)

    def embed_texts(self, texts: List[str]) -> List[List[float]]:
        """
        Returns a list of embeddings for given list of texts.
        """
        return self.model.encode(texts, show_progress_bar=False, convert_to_numpy=True).tolist()
