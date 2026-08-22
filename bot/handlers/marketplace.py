from aiogram import Router
from aiogram.types import CallbackQuery

from bot.user_settings import set_marketplace

router = Router()


@router.callback_query(lambda c: c.data == "market_wb")
async def wb(callback: CallbackQuery):

    set_marketplace(
        callback.from_user.id,
        "wildberries"
    )

    await callback.answer(
        "Wildberries выбран"
    )

    await callback.message.answer(
        "🟣 <b>Wildberries выбран</b>\n\n"
        "Теперь отправь фотографию товара."
    )


@router.callback_query(lambda c: c.data == "market_ozon")
async def ozon(callback: CallbackQuery):

    set_marketplace(
        callback.from_user.id,
        "ozon"
    )

    await callback.answer(
        "Ozon выбран"
    )

    await callback.message.answer(
        "🔵 <b>Ozon выбран</b>\n\n"
        "Теперь отправь фотографию товара."
    )


@router.callback_query(lambda c: c.data == "market_avito")
async def avito(callback: CallbackQuery):

    set_marketplace(
        callback.from_user.id,
        "avito"
    )

    await callback.answer(
        "Avito выбран"
    )

    await callback.message.answer(
        "🟠 <b>Avito выбран</b>\n\n"
        "Теперь отправь фотографию товара."
    )


@router.callback_query(lambda c: c.data == "market_yandex")
async def yandex(callback: CallbackQuery):

    set_marketplace(
        callback.from_user.id,
        "yandex_market"
    )

    await callback.answer(
        "Яндекс Маркет выбран"
    )

    await callback.message.answer(
        "🟡 <b>Яндекс Маркет выбран</b>\n\n"
        "Теперь отправь фотографию товара."
    )
