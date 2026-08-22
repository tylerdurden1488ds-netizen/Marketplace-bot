import asyncio

from ai.analyzer import analyze_product
from ai.router import get_skill_context
from ai.prompt_builder import build_prompt
from ai.image_generator import generate_image


class GenerationResult:

    def __init__(
        self,
        image_bytes: bytes,
        caption: str,
    ):
        self.image_bytes = image_bytes
        self.caption = caption


async def run_pipeline(
    photo_bytes: bytes,
    mime_type: str,
    user_request: str,
    auto_mode: bool,
    progress,
    marketplace: str = "universal",
):

    # 20% — анализируем товар

    analysis = await asyncio.to_thread(
        analyze_product,
        photo_bytes,
        mime_type,
        user_request,
    )

    await progress.update(
        40,
        "Придумываю концепцию",
    )

    # AI Director
    if auto_mode:

        user_request = (
            "Самостоятельно разработай "
            "профессиональную концепцию карточки "
            "товара для выбранного маркетплейса. "
            "Проанализируй товар и выбери лучший "
            "фон, композицию, заголовок, "
            "преимущества, типографику и "
            "минимальные декоративные элементы. "
            "Не изменяй реальный внешний вид товара."
        )

    # 60% — выбираем локальные Skills

    skills = await asyncio.to_thread(
        get_skill_context,
        user_request,
        marketplace,
    )

    await progress.update(
        60,
        "Собираю дизайн",
    )

    # Создаём финальный prompt

    final_prompt = await asyncio.to_thread(
        build_prompt,
        analysis,
        user_request,
        skills,
    )

    await progress.update(
        80,
        "Генерирую изображение",
    )

    # Gemini генерирует изображение

    image_bytes = await asyncio.to_thread(
        generate_image,
        photo_bytes,
        mime_type,
        final_prompt,
    )

    await progress.update(
        100,
        "Готово",
    )

    headline = analysis.get(
        "headline",
        "Готовая карточка",
    )

    return GenerationResult(
        image_bytes=image_bytes,
        caption=headline,
    )
