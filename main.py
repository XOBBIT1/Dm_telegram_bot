import logging
import asyncio

from app.interfaces.telegram.start.commands.base_command import day_card
from app.core import logging_settings
from aiogram.filters.command import Command
from aiogram import types
from aiogram.fsm.context import FSMContext
from app.core.config_settings import bot_engine, dp, router


@router.message(Command("start"))
async def cmd_day_card(message: types.Message, state: FSMContext):
    await message.answer_sticker(sticker="CAACAgIAAxkBAAEOUmtoAWt-kof_TX5iLZRD7N9cxHaeZQACHAADc1CHFcp19sVStGe1NgQ")
    await day_card(message, state)


async def main():
    await dp.start_polling(bot_engine, allowed_updates=dp.resolve_used_update_types())

if __name__ == "__main__":
    logging_settings.setup_logger()
    logging.info("Bot nachal rabotu !")
    dp.include_router(router)

    asyncio.run(main())
