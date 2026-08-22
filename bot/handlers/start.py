from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from bot.keyboards.main_menu import main_menu

router = Router()


@router.message(CommandStart())
async def start(message: Message):

    await message.answer(
        "🎨 <b>Marketplace Card AI</b>\n\n"
        "Я помогу создать профессиональную "
        "карточку товара для маркетплейса.\n\n"
        "Сначала выбери площадку:",
        reply_markup=main_menu(),
    )
