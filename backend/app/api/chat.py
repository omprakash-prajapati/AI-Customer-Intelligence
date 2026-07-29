from fastapi import APIRouter, Depends
from typing import Annotated
from functools import lru_cache
import logging
from app.models.chat import ChatRequest, ChatResponse
from app.config.settings import Settings
from app.services.chat_service import ChatService
from app.schemas.feedback import FeedbackRequest, FeedbackResponse

router = APIRouter()
logger = logging.getLogger(__name__)

@lru_cache
def get_settings() -> Settings:
    return Settings()

settings_deps = Annotated[Settings, Depends(get_settings)]


@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest, settings: settings_deps) -> ChatResponse:
    # Initialize the OpenAI provider
    chat_service = ChatService(provider="google", api_key=settings.google_api_key)
    provider = chat_service.chat(model="gemini-3.6-flash")
    answer = provider.generate(message=request.message)
    return ChatResponse(answer = answer)

@router.post("/feedback-analysis", response_model=FeedbackResponse)
def feedback_analysis(request: FeedbackRequest, settings: settings_deps) -> FeedbackResponse:
    chat_service = ChatService(provider="google", api_key=settings.google_api_key)
    logger.info(f"{request.feedback=}")
    provider = chat_service.chat(model="gemini-3.6-flash")
    return provider.generate_feedback_analysis(message=request.feedback)
