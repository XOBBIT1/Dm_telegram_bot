from aiogram import types
from aiogram.fsm.context import FSMContext

from app.interfaces.states.user_states import UserState
from app.interfaces.telegram.start.keyboards.start_keyboard import keyboard_start
from app.services.user_services import create_user_service


async def day_card(message: types.Message, state: FSMContext):
    await create_user_service(message)
    await message.answer(
        f"Привет, <b>{message.from_user.first_name}</b>! 👋\n"
        "Голоден? Или просто хочешь вкусненького? 😋\n\n"
        "Здесь ты можешь:\n"
        "🍔 Посмотреть меню\n"
        "🛒 Заглянуть в свою корзину\n"
        "🎟 Ввести промокод на скидку\n\n"
        "Жми на кнопки ниже — и еда сама тебя найдёт! 👇\n\n"
        "<b>P.S.</b> Не стесняйся писать мне — я всегда на связи 😎",
        parse_mode="HTML", reply_markup=keyboard_start())
    await state.set_state(UserState.any_text)
