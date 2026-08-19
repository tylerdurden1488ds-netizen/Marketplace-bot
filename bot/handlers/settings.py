from aiogram import Router, F
from aiogram.types import Message

router = Router()


@router.message(F.text == "⚙️ Настройки")
async def settings(message: Message):
    await message.answer(
        "⚙️ Настройки пока находятся в разработке.\n\n"
        "Здесь будут площадка, формат, стиль и другие параметры."
    )
