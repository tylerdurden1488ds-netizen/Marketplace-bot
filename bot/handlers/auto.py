from aiogram import Router, F
from aiogram.types import Message

router = Router()


@router.message(F.text == "🤖 ИИ придумывает дизайн")
async def auto_mode(message: Message):
    await message.answer(
        "🤖 <b>Автоматический режим</b>\n\n"
        "Отправь только фотографию товара.\n"
        "ИИ сам определит подходящий фон, композицию, заголовок, "
        "преимущества, типографику и визуальные элементы."
    )
