import json

from google.genai import types

from ai.gemini import (
    get_client,
    get_text_model,
)


ANALYSIS_PROMPT = """
Ты профессиональный арт-директор
для e-commerce маркетплейсов.

Проанализируй фотографию товара.

Определи:

1. Что это за товар.
2. Его форму и основные визуальные особенности.
3. Цвет.
4. Материалы и фактуру.
5. Для кого он предназначен.
6. Какой фон лучше всего подойдет.
7. Какой стиль карточки подойдет.
8. Какой заголовок можно использовать.
9. Какие 2-4 преимущества можно показать.

ВАЖНО:

Не придумывай характеристики,
которых нет на фото или в запросе пользователя.

Не меняй форму и внешний вид товара.

Ответ верни ТОЛЬКО в JSON.
"""


def analyze_product(
    photo_bytes: bytes,
    mime_type: str,
    user_request: str,
):

    prompt = (
        ANALYSIS_PROMPT
        + "\n\nЗапрос пользователя:\n"
        + (user_request or "Пользователь ничего не указал.")
    )

    response = get_client().models.generate_content(
        model=get_text_model(),
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
            response_mime_type="application/json",
            temperature=0.4,
        ),
    )

    try:

        return json.loads(
            response.text
        )

    except Exception:

        return {
            "category": "unknown",
            "product": response.text,
            "background": "clean premium studio",
            "style": "modern e-commerce",
            "headline": "",
            "benefits": [],
        }
