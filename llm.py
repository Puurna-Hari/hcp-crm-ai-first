from groq import Groq
import os

groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def call_llm(prompt: str):
    response = groq_client.chat.completions.create(
        model="gemma2-9b-it",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message["content"]
