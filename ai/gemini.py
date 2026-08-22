import os

from google import genai


def get_client():
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise RuntimeError(
            "GEMINI_API_KEY не найден в переменных окружения"
        )

    return genai.Client(
        api_key=api_key
    )


def get_text_model():
    return os.getenv(
        "GEMINI_TEXT_MODEL",
        "gemini-3.7-flash"
    )


def get_image_model():
    return os.getenv(
        "GEMINI_IMAGE_MODEL",
        "gemini-3.1-flash-image"
    )
