from fastapi import Depends
from typing import Annotated
from functools import lru_cache

from app.config.settings import Settings, get_settings
from app.providers.google_provider import GoogleProvider


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

OpenAPIProviderDependency = Annotated[
    GoogleProvider, Depends(get_google_provider)
]