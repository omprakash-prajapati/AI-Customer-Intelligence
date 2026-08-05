from typing import Protocol

type Embedding = list[float]

class EmbeddingProvider(Protocol):
    async def embed_text(self, text: str) -> Embedding:
        """Embed a text into a vector of floats"""
        pass
