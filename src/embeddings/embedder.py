from sentence_transformers import SentenceTransformer


class EmbeddingModel:

    def __init__(self):

        self.model = SentenceTransformer(
            "BAAI/bge-m3"
        )

    def encode(self, texts):

        return self.model.encode(
            texts,
            normalize_embeddings=True
        )