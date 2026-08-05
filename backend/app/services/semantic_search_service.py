from app.providers.base_embedding_provider import EmbeddingProvider

from app.domain.cosine_similarity import cosine_similarity
from app.schemas.embeddings import EmbeddedFeedback
from app.schemas.semantic_search import SemanticSearchResult

class SemanticSearchService:
    def __init__(self, embedding_provider: EmbeddingProvider) -> None:
        self.embedding_provider = embedding_provider
        self.records: list[EmbeddedFeedback] = []
    
    async def add_feedback(self, feedback_id: int, feedback_text: str) -> EmbeddedFeedback:
        """Add a feedback to the semantic search service"""
        embedding = await self.embedding_provider.embed_text(feedback_text)

        feedback = EmbeddedFeedback(
            id = feedback_id,
            text = feedback_text,
            embedding = embedding,
        )

        self.records.append(feedback)
        return feedback

    async def search(self, query: str, top_k: int ) -> list[SemanticSearchResult]:
        """Search for similar feedbacks"""
        query_embedding = await self.embedding_provider.embed_text(query)

        results = [
            SemanticSearchResult(
                id = record.id,
                text = record.text,
                similarity = cosine_similarity(query_embedding, record.embedding),
            ) for record in self.records
        ]
        results.sort(
            key = lambda result: result.similarity,
            reverse = True,
        )
        return results[:top_k]
