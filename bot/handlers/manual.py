from aiogram import Router, F
from aiogram.types import Message

router = Router()


@router.message(F.text == "✍️ Я задаю дизайн")
async def manual_mode(message: Message):
    await message.answer(
        "✍️ <b>Ручной режим</b>\n\n"
        "Отправь фотографию товара, затем напиши:\n"
        "• какой нужен фон;\n"
        "• какой текст добавить;\n"
        "• какие преимущества показать;\n"
        "• любые пожелания по стилю.\n\n"
        "После этого бот соберёт профессиональный промпт."
    )
