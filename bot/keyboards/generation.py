from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def generation_confirm():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="✅ Создать", callback_data="generate"),
                InlineKeyboardButton(text="🔄 Другой вариант", callback_data="new_concept"),
            ]
        ]
    )
