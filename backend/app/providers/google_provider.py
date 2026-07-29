from openai import OpenAI

from app.schemas.feedback import FeedbackResponse


class GoogleProvider:
    def __init__(self, model: str, api_key: str) -> None:
        self.model = model
        self.client = OpenAI(
            base_url=f"https://generativelanguage.googleapis.com/v1beta/openai/",
            api_key=api_key,
        )
    
    def generate(self, message: str):
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": message}],
        )
        return response.choices[0].message.content
    
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
