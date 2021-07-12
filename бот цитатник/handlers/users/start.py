from aiogram.types import Message
from loader import dp
from keyboards.default import murkup1
from aiogram.dispatcher.filters import Text


@dp.message_handler(commands=['start'])
async def bot_start(message: Message):
    await message.answer(f"Привет, {message.from_user.full_name}!", reply_markup = murkup1)