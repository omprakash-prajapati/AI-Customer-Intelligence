from openai import AsyncOpenAI
from app.providers.base_embedding_provider import Embedding, EmbeddingProvider


class OpenAIEmbeddingsProvider(EmbeddingProvider):
    def __init__(
        self,
        client: AsyncOpenAI,
        model_name: str,
        dimensions: int,
    ) -> None:
        self.client = client
        self.model_name = model_name
        self.dimensions = dimensions

    async def embed_text(self, text: str) -> Embedding:
        prepared_text = self._prepare_text(text)
        response = await self.client.embeddings.create(
            model = self.model_name,
            input = prepared_text,
        )
        return response.data[0].embedding

    @staticmethod
    def _prepare_text(text: str) -> str:
        result = " ".join(text.lower().split())
        if not result:
            raise ValueError("Could not create embedding for empty text")

        return result

