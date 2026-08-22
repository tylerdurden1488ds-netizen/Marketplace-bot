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
    progress = Progress(message)

    try:
        await progress.update(20, "Анализирую товар")

        result = await run_pipeline(
            photo_bytes=photo_bytes,
            mime_type=mime_type,
            user_request=user_request,
            auto_mode=(get_mode(message.from_user.id) == "auto"),
            progress=progress,
        )

        await progress.update(100, "Готово")

        await asyncio.sleep(0.5)
        await progress.delete()

        await message.answer_photo(
            photo=result.image_bytes,
            caption=(
                "✅ <b>Карточка готова!</b>\n\n"
                + result.caption
            ),
            reply_markup=main_menu(),
        )

        clear_user(message.from_user.id)

    except Exception as error:
        logging.exception("Generation error")

        await progress.delete()

        await message.answer(
            "❌ <b>Не удалось создать карточку.</b>\n\n"
            f"<code>{type(error).__name__}: "
            f"{str(error)[:500]}</code>"
        )


@router.message(F.photo)
async def receive_photo(message: Message):

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
        if telegram_file.file_path.lower().endswith(".png"):
            mime_type = "image/png"
        elif telegram_file.file_path.lower().endswith(".webp"):
            mime_type = "image/webp"

    # Если пользователь сразу написал текст
    if message.caption:

        await process_photo(
            message=message,
            photo_bytes=photo_bytes,
            mime_type=mime_type,
            user_request=message.caption,
        )

        return

    # Если текст будет отправлен следующим сообщением
    set_pending_photo(
        message.from_user.id,
        photo_bytes,
        mime_type,
    )

    await message.answer(
        "📸 <b>Фото получил.</b>\n\n"
        "Теперь отправь сообщение с описанием дизайна.\n\n"
        "Например:\n"
        "<i>Сделай современную светлую кухню, "
        "добавь заголовок «НОВАЯ КАРТОЧКА» "
        "и 3 преимущества товара.</i>"
    )


@router.message(F.text)
async def receive_text(message: Message):

    pending = get_pending_photo(
        message.from_user.id
    )

    if not pending:
        return

    await process_photo(
        message=message,
        photo_bytes=pending["photo_bytes"],
        mime_type=pending["mime_type"],
        user_request=message.text,
      )
  
