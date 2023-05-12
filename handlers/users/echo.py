from aiogram import types


from loader import dp
from filters.shahsiy import Shahsiy


# Echo bot
@dp.message_handler(Shahsiy(),state=None)
async def bot_echo(message: types.Message):
    await message.answer(message.text)


