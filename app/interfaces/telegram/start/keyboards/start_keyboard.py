from aiogram import types


def keyboard_start():

    buttons = [
        [types.InlineKeyboardButton(text="🧾 Меню", callback_data="fortune")],
        [types.InlineKeyboardButton(text="🛒 Моя корзина", callback_data="layout")],
        [types.InlineKeyboardButton(text="🎁 Ввести промокод", callback_data="library")],
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard
