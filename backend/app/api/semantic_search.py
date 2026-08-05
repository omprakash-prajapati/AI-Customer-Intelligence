from app.dependencies import EmbeddingProviderDependency
from fastapi import APIRouter

# from app.providers.fake_embeddings_provider import FakeEmbeddingsProvider
from app.services.semantic_search_service import SemanticSearchService
from app.schemas.semantic_search import SemanticSearchResult

router = APIRouter()

@router.post("/semantic-search")
async def semantic_search(
    query: str, top_k: int, provider: EmbeddingProviderDependency
) -> list[SemanticSearchResult]:
    # provider = FakeEmbeddingsProvider()
    service = SemanticSearchService(provider)

    feedbacks = [
        "Delivery was late.",
        "Payment failed.",
        "Product quality is excellent.",
        "Support did not respond.",
        "I received the wrong product.",
    ]

    for i, feedback in enumerate(feedbacks, start=1):
        await service.add_feedback(
            feedback_id=i,
            feedback_text=feedback,
        )

    results = await service.search(query, top_k)
    return results

