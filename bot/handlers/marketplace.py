from aiogram import Router, F
from aiogram.types import Message

from bot.user_settings import set_marketplace

router = Router()


@router.message(F.text == "🟣 Wildberries")
async def wildberries(message: Message):

    set_marketplace(
        message.from_user.id,
        "wildberries"
    )

    await message.answer(
        "🟣 <b>Wildberries</b>\n\n"
        "Теперь выбери режим:\n\n"
        "✍️ Ты задаёшь дизайн — "
        "сам пишешь фон, текст и пожелания.\n\n"
        "🤖 ИИ придумывает — "
        "я сам разработаю концепцию."
    )


@router.message(F.text == "🔵 Ozon")
async def ozon(message: Message):

    set_marketplace(
        message.from_user.id,
        "ozon"
    )

    await message.answer(
        "🔵 <b>Ozon выбран</b>\n\n"
        "Теперь отправь фото товара "
        "и выбери режим дизайна."
    )


@router.message(F.text == "🟠 Avito")
async def avito(message: Message):

    set_marketplace(
        message.from_user.id,
        "avito"
    )

    await message.answer(
        "🟠 <b>Avito выбран</b>\n\n"
        "Теперь отправь фото товара "
        "и выбери режим дизайна."
    )


@router.message(F.text == "🟡 Яндекс Маркет")
async def yandex(message: Message):

    set_marketplace(
        message.from_user.id,
        "yandex_market"
    )

    await message.answer(
        "🟡 <b>Яндекс Маркет выбран</b>\n\n"
        "Теперь отправь фото товара "
        "и выбери режим дизайна."
)
