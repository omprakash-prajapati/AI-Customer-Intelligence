from fastapi import APIRouter

from app.models.chat import ChatRequest, ChatResponse
from app.services.chat_service import ChatService
from app.schemas.feedback import FeedbackRequest, FeedbackResponse
from app.dependencies import OpenAPIProviderDependency, settings_deps

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest, provider: OpenAPIProviderDependency) -> ChatResponse:
    answer = await provider.generate(message=request.message)
    return ChatResponse(answer=answer)


@router.post("/feedback-analysis", response_model=FeedbackResponse)
def feedback_analysis(request: FeedbackRequest, settings: settings_deps) -> FeedbackResponse:
    # Initialize chat service
    chat_service = ChatService(
        provider=settings.feedback_provider, api_key=settings.google_api_key
    )
    # Initialize provider
    provider = chat_service.chat(model=settings.feedback_model)
    # Generate feedback analysis
    return provider.generate_feedback_analysis(message=request.feedback)
