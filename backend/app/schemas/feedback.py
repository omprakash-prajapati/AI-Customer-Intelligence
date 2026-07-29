from pydantic import BaseModel
from enum import Enum

class FeedbackRequest(BaseModel):
    feedback: str

class FeedbackSentiments(str, Enum):
    NEGATIVE = "negative"
    POSITIVE = "positive"
    NEUTRAL = "neutral"

class FeedbackCategory(str, Enum):
    BILLING = "billing"
    DELIVERY = "delivery"
    PRODUCT = "product"
    SUPPORT = "support"
    REFUND = "refund"
    TECHNICAL = "technical"

class FeedbackPriority(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

class FeedbackResponse(BaseModel):
    feedback: str
    sentiment: FeedbackSentiments
    category: FeedbackCategory
    priority: FeedbackPriority
    confidence: float
