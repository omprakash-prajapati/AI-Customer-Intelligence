from app.schemas.feedback import FeedbackResponse


class FakeLLMProvider:
    async def generate(self, message: str) -> str:
        return "Fake response"

    async def feedback_classify(self, message: str) -> FeedbackResponse:
        return FeedbackResponse(
            feedback = message,
            sentiment = "positive",
            category = "product",
            priority = "low",
            confidence = 0.95,
        )
