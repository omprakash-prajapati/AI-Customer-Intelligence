from fastapi import Depends
from typing import Annotated
from functools import lru_cache

from openai import AsyncOpenAI

from app.config.settings import Settings, get_settings
from app.providers.google_provider import GoogleProvider
from app.providers.base_embedding_provider import EmbeddingProvider
from app.providers.openai_embeddings_provider import OpenAIEmbeddingsProvider


settings_deps = Annotated[Settings, Depends(get_settings)]

@lru_cache
def get_google_provider() -> GoogleProvider:
    settings = Settings()
    return GoogleProvider(
        model=settings.chat_model,
        api_key=settings.google_api_key,
        base_url=settings.google_provider_base_url,
        timeout_seconds=settings.llm_timeout_seconds,
        max_retries=settings.llm_max_retries,
    )

def get_embedding_provider() -> EmbeddingProvider:
    settings = Settings()
    return OpenAIEmbeddingsProvider(
        client=AsyncOpenAI(api_key=settings.google_api_key, base_url=settings.google_provider_base_url),
        model_name=settings.embedding_provider_model_name,
        dimensions=settings.embedding_provider_dimension
    )

# Dependencies
OpenAPIProviderDependency = Annotated[GoogleProvider, Depends(get_google_provider)]
EmbeddingProviderDependency = Annotated[EmbeddingProvider, Depends(get_embedding_provider)]
