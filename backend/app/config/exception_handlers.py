from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse

from app.config.exceptions import (
    LLMAuthenticationError,
    LLMConnectionError,
    LLMInvalidRequestError,
    LLMNotFoundError,
    LLMPermissionError,
    LLMProviderError,
    LLMRateLimitError,
    LLMServiceUnavailableError,
    LLMTimeoutError,
)

def register_exception_handlers(app: FastAPI) -> None:

    @app.exception_handler(LLMInvalidRequestError)
    def invalid_request_handler(
        request: Request,
        error: LLMInvalidRequestError
    ) -> JSONResponse:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "error": {
                    "code": "llm_invalid_request",
                    "message": str(error),
                    "retryable": False,
                }
            },
        )

    @app.exception_handler(LLMNotFoundError)
    async def model_not_found_handler(
        request: Request,
        error: LLMNotFoundError,
    ) -> JSONResponse:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "error": {
                    "code": "llm_model_configuration_error",
                    "message": (
                        "The AI model is incorrectly configured."
                    ),
                    "retryable": False,
                }
            },
        )

    @app.exception_handler(LLMRateLimitError)
    async def rate_limit_handler(
        request: Request,
        error: LLMRateLimitError,
    ) -> JSONResponse:
        return JSONResponse(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            content={
                "error": {
                    "code": "llm_rate_limit",
                    "message": str(error),
                    "retryable": True,
                }
            },
            headers={
                "Retry-After": "5",
            },
        )