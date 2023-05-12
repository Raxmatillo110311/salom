from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.inline.tillar_uchun import tillar_button

from states.holat import Murojaat

from loader import dp,bot
# Echo bot
@dp.message_handler(text="Adminga murojat")
async def bot_echo(message: types.Message):
    await message.answer(text="Isimni kiriting", reply_markup=tillar_button)



@dp.message_handler(states= Murojaat.ism_qabul_qilish)
async def bot_echo(message: types.Message, state:FSMContext):
    matn = message.text
    await state.update_data({"ism":matn})
    await message.answer(text="Hududni kiriting")
    await Murojaat.hudud_qabul_qilish.set()




@dp.message_handler(states=Murojaat.hudud_qabul_qilish)
async def bot_echo(message: types.Message, state:FSMContext):
    matn = message.text
    await state.update_data({"hud":matn})
    await message.answer(text="Yoshni kiriting")
    await Murojaat.yosh_qabul_qilish.set()




@dp.message_handler(states=Murojaat.yosh_qabul_qilish)
async def bot_echo(message: types.Message, state:FSMContext):
    matn = message.text
    await state.update_data({"yosh":matn})
    await message.answer(text="Telefon qamni kiriting")
    await Murojaat.hudud_qabul_qilish.set()




@dp.message_handler(states=Murojaat.tel_qabul_qilish)
async def bot_echo(message: types.Message, state:FSMContext):
    matn = message.text
    await state.update_data({"tel":matn})
    await message.answer(text="Murojaatni kiriting")
    await Murojaat.hudud_qabul_qilish.set()

@dp.message_handler(states=Murojaat.murojat_qabul_qilish)
async def bot_echo(message: types.Message, state:FSMContext):
    matn = message.text
    await state.update_data({"murojaat":matn})
    malumot = await state.get_data()
    ismi = malumot.get('ism')
    hudud = malumot.get('hud')
    yoshi = malumot.get('yosh')
    tel = malumot.get('tel')
    murojat = malumot.get('murojaat')

    txtt= f"Ism : {ismi}\n"\
          f"Hudud : {hudud}\n"\
          f"Yosh : {yoshi}\n"\
          f"Tel : {tel}\n"\
          f"Murojaat : {murojat}\n"
    user_id = message.from_user.id
    await bot.send_message(chat_id=user_id,text=txtt)