import os
from google import genai


def get_client():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY is not set in environment variables")
    return genai.Client(api_key=api_key)
