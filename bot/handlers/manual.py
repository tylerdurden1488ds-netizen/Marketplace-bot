from aiogram import Router
from aiogram.types import CallbackQuery

from bot.state_store import set_mode

router = Router()


@router.callback_query(lambda c: c.data == "mode_manual")
async def manual_mode(callback: CallbackQuery):

    set_mode(
        callback.from_user.id,
        "manual",
    )

    await callback.answer()

    await callback.message.answer(
        "✍️ <b>Ручной режим</b>\n\n"
        "Отправь фотографию товара.\n\n"
        "Лучший вариант — отправить фото "
        "сразу с подписью.\n\n"
        "<b>Например:</b>\n"
        "«Светлая современная кухня, "
        "добавь заголовок НОВИНКА и "
        "3 преимущества товара»"
    )
