from aiogram import Router, F
from aiogram.types import Message

from bot.user_settings import set_marketplace
from bot.keyboards.mode import mode_keyboard

router = Router()


async def marketplace_selected(
    message: Message,
    marketplace: str,
    title: str,
):

    set_marketplace(
        message.from_user.id,
        marketplace,
    )

    await message.answer(
        f"{title}\n\n"
        "Теперь выбери режим создания карточки:",
        reply_markup=mode_keyboard(),
    )


@router.message(F.text == "🟣 Wildberries")
async def wildberries(message: Message):

    await marketplace_selected(
        message,
        "wildberries",
        "🟣 <b>Wildberries выбран</b>",
    )


@router.message(F.text == "🔵 Ozon")
async def ozon(message: Message):

    await marketplace_selected(
        message,
        "ozon",
        "🔵 <b>Ozon выбран</b>",
    )


@router.message(F.text == "🟠 Avito")
async def avito(message: Message):

    await marketplace_selected(
        message,
        "avito",
        "🟠 <b>Avito выбран</b>",
    )


@router.message(F.text == "🟡 Яндекс Маркет")
async def yandex(message: Message):

    await marketplace_selected(
        message,
        "yandex_market",
        "🟡 <b>Яндекс Маркет выбран</b>",
    )
