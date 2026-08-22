import os

from google.genai import types

from ai.gemini import get_client, get_image_model


def generate_image(
    photo_bytes: bytes,
    mime_type: str,
    prompt: str,
) -> bytes:

    aspect_ratio = os.getenv(
        "IMAGE_ASPECT_RATIO",
        "3:4",
    )

    image_size = os.getenv(
        "IMAGE_SIZE",
        "2K",
    )

    response = get_client().models.generate_content(
        model=get_image_model(),
        contents=[
            types.Part.from_text(
                text=prompt
            ),
            types.Part.from_bytes(
                data=photo_bytes,
                mime_type=mime_type,
            ),
        ],
        config=types.GenerateContentConfig(
            response_modalities=["IMAGE"],
            image_config=types.ImageConfig(
                aspect_ratio=aspect_ratio,
                image_size=image_size,
            ),
        ),
    )

    for part in response.parts:

        if getattr(part, "inline_data", None):

            if part.inline_data.data:
                return part.inline_data.data

    raise RuntimeError(
        "Gemini не вернул изображение."
  )
