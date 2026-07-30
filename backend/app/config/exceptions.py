class LLMProviderError(Exception):
    pass

class LLMRateLimitError(LLMProviderError):
    pass

class LLMInvalidRequestError(LLMProviderError):
    pass

class LLMAuthenticationError(LLMProviderError):
    pass

class LLMPermissionError(LLMProviderError):
    pass

class LLMTimeoutError(LLMProviderError):
    pass

class LLMConnectionError(LLMProviderError):
    pass

class LLMServiceUnavailableError(LLMProviderError):
    pass

class LLMNotFoundError(LLMProviderError):
    pass
