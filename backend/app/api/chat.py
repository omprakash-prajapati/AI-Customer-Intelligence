from fastapi import APIRouter, Depends
from typing import Annotated
from functools import lru_cache

from app.models.chat import ChatRequest, ChatResponse
from app.providers.openai_provider import OpenAIProvider
from app.config.settings import Settings

router = APIRouter()

@lru_cache
def get_settings() -> Settings:
    return Settings()

@router.post("/chat", response_model=ChatResponse)
async def chat(
    request: ChatRequest, settings: Annotated[Settings, Depends(get_settings)]
) -> ChatResponse:
    # Initialize the OpenAI provider
    provider = OpenAIProvider(model="gpt-4o-mini", api_key=settings.openai_api_key)
    answer = await provider.generate(request.message)
    return ChatResponse(answer = answer)
