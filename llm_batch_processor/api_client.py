from openai import OpenAI
from llm_batch_processor.config import  CONFIG
import json

class OpenAIClient:
    def __init__(self, model="gpt-4o-mini", is_project=False):

        self.model = model
        if is_project:
            self.client = OpenAI(
                api_key=CONFIG["OPENAI_API_KEY"],
                organization=CONFIG["PROJECT_ID"]
            )
        else:
            self.client = OpenAI(
                api_key=CONFIG["OPENAI_API_KEY"]
            )

    def get_response(self, prompt):
        """Send prompt to OpenAI API and return the response"""
        try:
            response = self.client.chat.completions.create(model=self.model,
            messages=[{"role": "user", "content": prompt}])
            return response.choices[0].message.content.strip()
        except Exception as e:
            print(f"Error in API call: {e}")
            return "Error in API call"
