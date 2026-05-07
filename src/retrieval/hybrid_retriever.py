from rank_bm25 import BM25Okapi


class HybridRetriever:

    def __init__(self, chunks):

        self.chunks = chunks

        tokenized = [
            chunk.page_content.split()
            for chunk in chunks
        ]

        self.bm25 = BM25Okapi(tokenized)

    def keyword_search(self, query, top_k=5):

        scores = self.bm25.get_scores(
            query.split()
        )

        ranked = sorted(
            zip(scores, self.chunks),
            reverse=True,
            key=lambda x: x[0]
        )

        return ranked[:top_k]