from aiogram import types
from aiogram.types import CallbackQuery
from aiogram.dispatcher.filters.builtin import CommandStart
from handlers.users import Adminga_mur
from keyboards.default.Maishiy_texnikalar_uchun import Maishiy_texnikalar_uchun_buttons
from keyboards.default.Telefonlar_uchun import Telefonlar_buttons
from keyboards.default.Kompyuterlar_uchun import Kompyuterlar_buttons
from keyboards.default.Aksessuarlar import Aksessuarlar_buttons
from keyboards.default.dokon import dokon_buttons
from keyboards.default.orqaga import orqaga_buttons
from loader import dp
from keyboards.inline.tillar_uchun import tillar_button
from filters import Shahsiy

@dp.message_handler(commands='start')
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!",reply_markup=tillar_button)

@dp.callback_query_handler(text="til1")
async def bot_start(message:CallbackQuery):
    await message.message.answer(text=f"Salom mijoz,menyuni tanlang!",reply_markup=dokon_buttons)

@dp.message_handler(text='Maishiy texnikalar')
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!",reply_markup=Maishiy_texnikalar_uchun_buttons)

@dp.message_handler(text='Orqaga')
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!",reply_markup=orqaga_buttons)

@dp.message_handler(text='Kompyuterlar')
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!",reply_markup=Kompyuterlar_buttons)

@dp.message_handler(text='Telefonlar')
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!",reply_markup=Telefonlar_buttons)

@dp.message_handler(text='Aksessuarlar')
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!",reply_markup=Aksessuarlar_buttons)


