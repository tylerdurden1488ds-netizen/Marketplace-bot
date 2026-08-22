import json

from google.genai import types

from ai.gemini import get_client, get_text_model


ANALYSIS_PROMPT = """
Ты — профессиональный AI арт-директор
для e-commerce карточек товаров.

Твоя задача — внимательно изучить фотографию
товара и подготовить концепцию будущей карточки.

Определи:

1. Что за товар.
2. Категорию товара.
3. Главные визуальные особенности.
4. Цвет и материал.
5. Для какой аудитории он подходит.
6. Какой фон лучше всего подходит.
7. Какую композицию использовать.
8. Какое освещение использовать.
9. Какой визуальный стиль выбрать.
10. Какой короткий продающий заголовок предложить.
11. Какие 2-4 преимущества можно показать.
12. Какие цвета использовать для текста.
13. Нужны ли иконки.
14. Нужны ли эмодзи.
15. Где лучше разместить текст.

ВАЖНЫЕ ПРАВИЛА:

Товар на фотографии является главным источником истины.

Не изменяй:

- форму;
- пропорции;
- цвет;
- материал;
- реальные детали;
- логотип;
- количество предметов.

Не придумывай характеристики,
которых нельзя подтвердить по фотографии.

Если пользователь предоставил конкретный текст,
его нужно сохранить.

Ответь строго в JSON.
"""


def analyze_product(
    photo_bytes: bytes,
    mime_type: str,
    user_request: str,
):

    request = user_request.strip()

    if not request:

        request = (
            "Пользователь не дал инструкций. "
            "Самостоятельно разработай "
            "лучшую концепцию карточки."
        )

    prompt = (
        ANALYSIS_PROMPT
        + "\n\n"
        + "ЗАПРОС ПОЛЬЗОВАТЕЛЯ:\n"
        + request
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
            temperature=0.7,
        ),
    )

    try:

        return json.loads(
            response.text
        )

    except Exception:

        return {
            "product": "Товар",
            "category": "e-commerce",
            "visual_features": [],
            "background": "professional studio",
            "composition": "premium commercial composition",
            "lighting": "soft professional lighting",
            "style": "modern premium e-commerce",
            "headline": "",
            "benefits": [],
            "text_colors": [],
            "icons": [],
            "emojis": [],
            "text_position": "upper area",
        }
