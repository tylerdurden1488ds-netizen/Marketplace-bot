import asyncio

from aiogram.types import Message


class Progress:

    def __init__(self, message: Message):
        self.message = message
        self.progress_message = None

    async def update(
        self,
        percent: int,
        status: str,
    ):

        text = (
            f"🎨 <b>Создаю карточку</b>\n\n"
            f"📊 <b>{percent}%</b>\n"
            f"{status}"
        )

        if self.progress_message is None:

            self.progress_message = await self.message.answer(
                text
            )

            return

        try:

            await self.progress_message.edit_text(
                text
            )

        except Exception:
            pass

    async def delete(self):

        if self.progress_message is None:
            return

        try:

            await self.progress_message.delete()

        except Exception:
            pass
