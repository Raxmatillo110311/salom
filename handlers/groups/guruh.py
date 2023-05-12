from aiogram import types
from filters import Guruh
from loader import dp


@dp.message_handler(Guruh(), commands="start")
async def bot_echo(message: types.Message):
    user = message.from_user.full_name
    await message.answer(text=f'guruhga hush kelibsiz {user}')








