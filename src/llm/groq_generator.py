import os

from groq import Groq
from dotenv import load_dotenv

load_dotenv()


class GroqGenerator:

    def __init__(self):

        self.client = Groq(
            api_key=os.getenv("GROQ_API_KEY")
        )

    def generate_answer(self, query, context):

        prompt = f"""
You are a grounded manuscript assistant.

Only answer from provided context.
If answer not found say:
'Insufficient information found in manuscript.'

Context:
{context}

Question:
{query}
"""

        response = self.client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.2,
            max_tokens=512
        )

        return response.choices[0].message.content