import openai
from openai import AsyncOpenAI
import time
import logging

from app.schemas.feedback import FeedbackResponse
from app.config.exceptions import (
    LLMAuthenticationError,
    LLMRateLimitError,
    LLMTimeoutError,
    LLMInvalidRequestError,
    LLMNotFoundError,
    LLMServiceUnavailableError,
    LLMConnectionError
)


logger = logging.getLogger(__name__)

class GoogleProvider:
    def __init__(
            self, 
            model: str, 
            api_key: str, 
            base_url: str,
            timeout_seconds: float = 30.0,
            max_retries: int = 2
        ) -> None:
        self.model = model
        self.client = AsyncOpenAI(
            base_url=base_url, 
            api_key=api_key, 
            timeout=timeout_seconds,
            max_retries=max_retries
        )
    
    async def generate(self, message: str):
        started_at = time.perf_counter()
        try:
            response = await self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": message}],
            )
            latency_ms = round((time.perf_counter() - started_at) * 1000, 2)
            # Log the request completion
            logger.info(
                "LLM request completed",
                extra={
                    "provider": "google",
                    "model": self.model,
                    "latency_ms": latency_ms,
                    "request_id": getattr(response, "_request_id", None),
                }
            )
            return response.choices[0].message.content

        except openai.AuthenticationError as error:
            logger.exception(
                "LLM authentication failed",
                extra={
                    "provider": "google",
                    "model": self.model
                }
            )
            raise LLMAuthenticationError(
                "LLM Provider Authentication Failed."
            ) from error
        
        except openai.NotFoundError as error:
            logger.exception(
                "LLM model not found",
                extra={
                    "provider": "google",
                    "model": self.model
                }
            )
            raise LLMNotFoundError("LLM Model Not Found.") from error
        
        except openai.RateLimitError as error:
            logger.exception(
                "LLM rate limit exceeded",
                extra={
                    "provider": "google",
                    "model": self.model
                }
            )
            raise LLMRateLimitError(
                "The LLM service is temporarily busy."
                "Please try again later",
            ) from error
        
        except openai.InternalServerError as error:
            raise LLMServiceUnavailableError(
                "The LLM provider is temporarily unavailable."
            ) from error

        except openai.APIConnectionError as error:
            logger.exception(
                "Could not connect to LLM provider",
                extra={
                    "provider": "openai",
                    "model": self.model,
                },
            )
            raise LLMConnectionError(
                "Could not connect to the LLM provider."
            ) from error

        except openai.Timeout as error:
            logger.warning(
                "LLM request timed out",
                extra={
                    "provider": "google",
                    "model": self.model,
                },
            )

            raise LLMTimeoutError(
                "The LLM provider did not respond in time."
            ) from error

        except openai.BadRequestError as error:
            raise LLMInvalidRequestError(
                "The LLM provider rejected the request."
            ) from error
    
    def generate_feedback_analysis(self, message: str):
        response = self.client.chat.completions.parse(
            model=self.model,
            messages=[
                {
                    "role": "system", 
                    "content": "You are a helpful assistant that analyzes feedback and provides a sentiment, category, priority, and confidence score."
                    },
                {
                    "role": "user", 
                    "content": "Analyze the following feedback and provide a sentiment, category, priority, and confidence score."
                },
                {"role": "user", "content": message}
            ],
            response_format=FeedbackResponse
        )
        return response.choices[0].message.parsed
