from aiogram import Router
from aiogram.types import CallbackQuery

from bot.state_store import set_mode

router = Router()


@router.callback_query(lambda c: c.data == "mode_auto")
async def auto_mode(callback: CallbackQuery):

    set_mode(
        callback.from_user.id,
        "auto",
    )

    await callback.answer()

    await callback.message.answer(
        "🤖 <b>AI Director</b>\n\n"
        "Отправь только фотографию товара.\n\n"
        "Я сам определю:\n"
        "• подходящий фон;\n"
        "• композицию;\n"
        "• заголовок;\n"
        "• преимущества;\n"
        "• типографику;\n"
        "• визуальные элементы.\n\n"
        "После анализа начнётся генерация."
    )
