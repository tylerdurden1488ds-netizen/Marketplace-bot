from aiogram.types import (
    KeyboardButton,
    ReplyKeyboardMarkup,
)


def main_menu():

    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(
                    text="🟣 Wildberries"
                ),
                KeyboardButton(
                    text="🔵 Ozon"
                ),
            ],
            [
                KeyboardButton(
                    text="🟠 Avito"
                ),
                KeyboardButton(
                    text="🟡 Яндекс Маркет"
                ),
            ],
            [
                KeyboardButton(
                    text="⚙️ Настройки"
                ),
            ],
        ],
        resize_keyboard=True,
        is_persistent=True,
    )
