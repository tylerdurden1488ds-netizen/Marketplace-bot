from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def mode_keyboard():

    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="✍️ Я задаю дизайн",
                    callback_data="mode_manual"
                )
            ],
            [
                InlineKeyboardButton(
                    text="🤖 ИИ придумывает дизайн",
                    callback_data="mode_auto"
                )
            ],
        ]
    )
