import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

SYSTEM_PROMPT = """
You are NorthstarFI, an educational FIRE planning assistant.
Give clear, practical, non-personalized financial education.
Do not claim to be a licensed financial advisor.
Focus on FIRE number, savings rate, allocation risk, tax-aware ideas, and next actions.
"""

def get_ai_advice(user_summary: str) -> str:
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key or api_key == "your_groq_api_key_here":
        return "Groq API key is missing. Add GROQ_API_KEY to your .env file to enable AI advice."

    client = Groq(api_key=api_key)

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_summary}
        ],
        temperature=0.3,
        max_tokens=500
    )
    return response.choices[0].message.content
