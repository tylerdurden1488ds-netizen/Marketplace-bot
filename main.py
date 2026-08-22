import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from bot.handlers.start import router as start_router
from bot.handlers.manual import router as manual_router
from bot.handlers.auto import router as auto_router
from bot.handlers.settings import router as settings_router
from bot.handlers.photo_flow import router as photo_router
from bot.handlers.marketplace import router as marketplace_router


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


async def main():

    token = os.getenv("BOT_TOKEN")

    if not token:
        raise RuntimeError(
            "BOT_TOKEN не найден в переменных окружения Bothost"
        )

    bot = Bot(
        token=token,
        default=DefaultBotProperties(
            parse_mode=ParseMode.HTML
        ),
    )

    dp = Dispatcher()

    # Основные обработчики
    dp.include_router(start_router)
    dp.include_router(manual_router)
    dp.include_router(auto_router)
    dp.include_router(settings_router)

    # Выбор маркетплейса
    dp.include_router(marketplace_router)

    # Фото + текст + генерация
    dp.include_router(photo_router)

    logging.info(
        "🚀 Marketplace Card AI запущен"
    )

    try:
        await dp.start_polling(
            bot,
            allowed_updates=dp.resolve_used_update_types(),
        )

    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())
