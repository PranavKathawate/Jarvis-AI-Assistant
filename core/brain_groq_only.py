import os
from openai import OpenAI

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY not set in environment variables.")

client = OpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1"
)

MODEL_NAME = "llama-3.1-8b-instant"

def process(text, history=None):
    try:
        messages = []

        if history:
            messages = history[-4:].copy()

        messages.append({"role": "user", "content": text})

        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=messages,
            temperature=0.3,
            max_tokens=300
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error: {e}"