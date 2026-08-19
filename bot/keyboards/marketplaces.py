from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def marketplaces():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="🟣 Wildberries", callback_data="market_wb"),
                InlineKeyboardButton(text="🔵 Ozon", callback_data="market_ozon"),
            ],
            [
                InlineKeyboardButton(text="🟡 Avito", callback_data="market_avito"),
                InlineKeyboardButton(text="🔴 Яндекс Маркет", callback_data="market_ym"),
            ],
        ]
    )
