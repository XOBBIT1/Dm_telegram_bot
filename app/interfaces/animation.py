import time

from aiogram import types

from app.core.config_settings import bot


async def loading(message: types.Message, string, icon):
    load = string
    sent_message = await message.answer(load.format(icon), parse_mode="HTML")

    for i in range(2, 7):
        time.sleep(1)
        updated_text = load.format(icon * i)
        updated_text += " "
        await bot.edit_message_text(chat_id=sent_message.chat.id, message_id=sent_message.message_id, text=updated_text,
                                    parse_mode="HTML")
