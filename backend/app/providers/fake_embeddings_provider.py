from app.providers.base_embedding_provider import EmbeddingProvider
from app.providers.base_embedding_provider import Embedding

class FakeEmbeddingsProvider(EmbeddingProvider):
    async def embed_text(self, text: str,) -> Embedding:
        normalized_text = text.lower()

        return [
            1.0 if "delivery" in normalized_text else 0.0,
            1.0 if "payment" in normalized_text else 0.0,
            1.0 if "product" in normalized_text else 0.0,
            1.0 if "support" in normalized_text else 0.0,
        ]
