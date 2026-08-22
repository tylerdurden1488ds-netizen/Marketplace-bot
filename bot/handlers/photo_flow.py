import asyncio
import logging
from io import BytesIO

from aiogram import Router, F
from aiogram.types import Message

from bot.state_store import (
    get_mode,
    set_pending_photo,
    get_pending_photo,
    clear_user,
)
from bot.user_settings import get_marketplace
from bot.progress import Progress
from bot.keyboards.main_menu import main_menu
from ai.pipeline import run_pipeline


router = Router()

logging.basicConfig(level=logging.INFO)


async def process_photo(
    message: Message,
    photo_bytes: bytes,
    mime_type: str,
    user_request: str,
):

    user_id = message.from_user.id

    progress = Progress(message)

    try:

        # Получаем настройки пользователя

        mode = get_mode(user_id)

        marketplace = get_marketplace(user_id)

        auto_mode = mode == "auto"

        # 20%

        await progress.update(
            20,
            "Анализирую товар",
        )

        # Запускаем генерацию

        result = await run_pipeline(
            photo_bytes=photo_bytes,
            mime_type=mime_type,
            user_request=user_request,
            auto_mode=auto_mode,
            progress=progress,
            marketplace=marketplace,
        )

        # 100%

        await progress.update(
            100,
            "Готово",
        )

        await asyncio.sleep(0.5)

        await progress.delete()

        # Отправляем изображение

        await message.answer_photo(
            photo=result.image_bytes,
            caption=(
                "✅ <b>Карточка готова!</b>\n\n"
                f"{result.caption}"
            ),
            reply_markup=main_menu(),
        )

        clear_user(user_id)

    except Exception as error:

        logging.exception(
            "Generation error"
        )

        await progress.delete()

        await message.answer(
            "❌ <b>Ошибка при создании карточки.</b>\n\n"
            f"<code>{type(error).__name__}: "
            f"{str(error)[:800]}</code>"
        )


@router.message(F.photo)
async def receive_photo(
    message: Message,
):

    user_id = message.from_user.id

    photo = message.photo[-1]

    telegram_file = await message.bot.get_file(
        photo.file_id
    )

    buffer = BytesIO()

    await message.bot.download_file(
        telegram_file.file_path,
        destination=buffer,
    )

    photo_bytes = buffer.getvalue()

    mime_type = "image/jpeg"

    if telegram_file.file_path:

        file_path = telegram_file.file_path.lower()

        if file_path.endswith(".png"):
            mime_type = "image/png"

        elif file_path.endswith(".webp"):
            mime_type = "image/webp"

    # Если пользователь отправил
    # фото сразу с текстом

    if message.caption:

        await process_photo(
            message=message,
            photo_bytes=photo_bytes,
            mime_type=mime_type,
            user_request=message.caption,
        )

        return

    # Иначе сохраняем фото
    # и ждём текст

    set_pending_photo(
        user_id,
        photo_bytes,
        mime_type,
    )

    await message.answer(
        "📸 <b>Фото получил.</b>\n\n"
        "Теперь отправь описание дизайна.\n\n"
        "<b>Например:</b>\n"
        "«Сделай современный светлый фон, "
        "добавь заголовок НОВИНКА и "
        "3 преимущества товара»"
