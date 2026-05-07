import chromadb


class ChromaStore:

    def __init__(self):

        self.client = chromadb.PersistentClient(
            path="output/chroma_db"
        )

        self.collection = self.client.get_or_create_collection(
            name="manuscript_collection"
        )

    def add_documents(self, chunks, embeddings):

        ids = [
            f"chunk_{i}"
            for i in range(len(chunks))
        ]

        documents = [
            chunk.page_content
            for chunk in chunks
        ]

        metadatas = [
            chunk.metadata
            for chunk in chunks
        ]

        self.collection.add(
            ids=ids,
            documents=documents,
            embeddings=embeddings.tolist(),
            metadatas=metadatas
        )

    def search(self, query_embedding, top_k=5):

        results = self.collection.query(
            query_embeddings=[query_embedding.tolist()],
            n_results=top_k
        )

        return results