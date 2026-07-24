from openai import AsyncOpenAI


class OpenAIProvider:
    def __init__(self, model, api_key) -> None:
        self.client = AsyncOpenAI(api_key=api_key)
        self.model = model
    
    async def generate(self, message) -> str:
        response = await self.client.responses.create(
            model=self.model,
            input=message,
        )
        return response.output_text
