from aiogram import Router, F
from aiogram.types import Message

router = Router()


@router.message(F.photo)
async def receive_photo(message: Message):
    photo = message.photo[-1]

    caption = message.caption or "Фото получено ✅"

    await message.answer_photo(
        photo=photo.file_id,
        caption=f"📸 Получено!\n\n{caption}"
    )
