import asyncio
import os

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from bot.handlers.start import router as start_router
from bot.handlers.manual import router as manual_router
from bot.handlers.auto import router as auto_router
from bot.handlers.generation import router as generation_router
from bot.handlers.settings import router as settings_router
from bot.handlers.common import router as common_router


async def main():
    token = os.getenv("BOT_TOKEN")
    if not token:
        raise RuntimeError("BOT_TOKEN is not set in environment variables")

    bot = Bot(
        token=token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
    dp = Dispatcher()

    dp.include_router(start_router)
    dp.include_router(manual_router)
    dp.include_router(auto_router)
    dp.include_router(generation_router)
    dp.include_router(settings_router)
    dp.include_router(common_router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
