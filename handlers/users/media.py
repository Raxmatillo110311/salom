from aiogram import types
from aiogram.types import ContentTypes

from loader import dp,bot


# Echo bot
@dp.message_handler(content_types=ContentTypes.DOCUMENT)
async def bot_echo(message: types.Message):
    await message.document.download()
    await message.answer(text="DOCUMENT qabul qilindi")

@dp.message_handler(content_types=ContentTypes.DOCUMENT)
async def bot_echo(message: types.Message):
    await message.document.download()
    await message.answer(text="DOCUMENT qabul qilindi")

@dp.message_handler(content_types=ContentTypes.PHOTO)
async def bot_echo(message: types.Message):
    await message.photo[-1].download()
    await message.answer(text="rasm qabul qilindi")

@dp.message_handler(text='Huwavei')
async def bot_start(message: types.Message):
    user_id =message.from_user.id
    rasm = 'https://avatars.mds.yandex.net/get-mpic/5226176/img_id3396105367170087534.jpeg/orig'
    await bot.send_photo(chat_id=user_id, photo=rasm)


@dp.message_handler(text='Iphone')
async def bot_start(message: types.Message):
    user_id =message.from_user.id
    rasm = 'https://storeinua.com/image/cache/catalog/0Apple/368-800x800.jpg'
    await bot.send_photo(chat_id=user_id, photo=rasm)



@dp.message_handler(text='Samsung')
async def bot_start(message: types.Message):
    user_id =message.from_user.id
    rasm = 'https://www.sammyfans.com/wp-content/uploads/2022/07/Samsung-Galaxy-S23-Ultra-Bora-Purple-Unboxing-2.jpg'
    await bot.send_photo(chat_id=user_id, photo=rasm)





@dp.message_handler(text='Redmi')
async def bot_start(message: types.Message):
    user_id =message.from_user.id
    rasm = 'https://ae01.alicdn.com/kf/H0ada147eb0d141dcb2b8ea82832fe03eE.jpg'
    await bot.send_photo(chat_id=user_id, photo=rasm)




@dp.message_handler(text='Vivo')
async def bot_start(message: types.Message):
    user_id =message.from_user.id
    rasm = 'https://www.droidafrica.net/wp-content/uploads/2022/08/vivo-y22s-color-1024x959.jpg'
    await bot.send_photo(chat_id=user_id, photo=rasm)

@dp.message_handler(text='Flesgka')
async def bot_start(message: types.Message):
    user_id = message.from_user.id
    rasm = 'http://promoest.ru/upload/iblock/176/4333.08_3_psd_1000x1000.jpg'
    await bot.send_photo(chat_id=user_id, photo=rasm)




@dp.message_handler(text='Chip')
async def bot_start(message: types.Message):
    user_id = message.from_user.id
    rasm = 'https://imgaz3.staticbg.com/thumb/large/oaupload/banggood/images/5F/40/10cdb2e3-1324-41a8-9cf0-a4d93b107f78.jpg'
    await bot.send_photo(chat_id=user_id, photo=rasm)


@dp.message_handler(text='Airpods')
async def bot_start(message: types.Message):
    user_id = message.from_user.id
    rasm = 'https://www.gannett-cdn.com/presto/2019/03/20/USAT/d95ace61-71a2-4630-bc0b-8dec1ebef5c1-Apple-AirPods-worlds-most-popular-wireless-headphones_03202019.jpg'
    await bot.send_photo(chat_id=user_id, photo=rasm)




@dp.message_handler(text='Naushnik')
async def bot_start(message: types.Message):
    user_id = message.from_user.id
    rasm = 'https://user43214.clients-cdnnow.ru/image/cache/catalog/286/286968_645d1-500x500.jpg'
    await bot.send_photo(chat_id=user_id, photo=rasm)

@dp.message_handler(text='Muzlatgich')
async def bot_start(message: types.Message):
    user_id = message.from_user.id
    rasm = 'https://images.samsung.com/is/image/samsung/assets/gr/p6_gro2/p6_initial_pcd/p6_initial_home-appliances/1_PCD_cardlist_ref_MO.jpg?$720_1080_JPG$'
    await bot.send_photo(chat_id=user_id, photo=rasm)



@dp.message_handler(text='Mikrotolqinli pech')
async def bot_start(message: types.Message):
    user_id = message.from_user.id
    rasm = 'https://www.tech-dostavka.ru/image/cache/catalog/product/ME83MRTS-1000x1000.jpg'
    await bot.send_photo(chat_id=user_id, photo=rasm)


@dp.message_handler(text='Gaz plita')
async def bot_start(message: types.Message):
    user_id = message.from_user.id
    rasm = 'https://topsto-crimea.ru/images/detailed/6446/1651572916.907.jpg'
    await bot.send_photo(chat_id=user_id, photo=rasm)





@dp.message_handler(text='Kir yuvish mashinasi')
async def bot_start(message: types.Message):
    user_id = message.from_user.id
    rasm = 'https://elmakon.uz/images/detailed/35/1_8rlf-1t.jpg'
    await bot.send_photo(chat_id=user_id, photo=rasm)



@dp.message_handler(text='Changyutgich')
async def bot_start(message: types.Message):
    user_id = message.from_user.id
    rasm = 'https://tezz.uz/uploads/images/product/517/209254.jpg'
    await bot.send_photo(chat_id=user_id, photo=rasm)



@dp.message_handler(text='Asus')
async def bot_start(message: types.Message):
    user_id = message.from_user.id
    rasm = 'https://www.asus.com/media/Odin/Websites/global/Series/15.png'
    await bot.send_photo(chat_id=user_id, photo=rasm)


@dp.message_handler(text='Hp')
async def bot_start(message: types.Message):
    user_id = message.from_user.id
    rasm = 'https://1.bp.blogspot.com/-hEoTMGiaRGg/XRWLiLGFKVI/AAAAAAAAHZs/LG29GdgPF1cw_n5tYzASrveX5xq82ASXgCLcBGAs/s1600/Jual%2BLaptop%2BHP%2BPavilion%2BG4%2BCore%2Bi3%2BBekas.JPG'
    await bot.send_photo(chat_id=user_id, photo=rasm)


@dp.message_handler(text='Dell')
async def bot_start(message: types.Message):
    user_id = message.from_user.id
    rasm = 'https://www.pcplanet.ru/public_files/products/3c/30/3c3001085bb32aa7a4a0c539e4260cf8/original.jpg'
    await bot.send_photo(chat_id=user_id, photo=rasm)


@dp.message_handler(text='Acer')
async def bot_start(message: types.Message):
    user_id = message.from_user.id
    rasm = 'https://a-static.mlcdn.com.br/1500x1500/notebook-acer-aspire-5-a515-52g-577t-intel-core-i5-8265u-8ogeracao-ram-de-8gb-hd-de-1tb-geforce-mx130-2gb-tela-de-15-6-windows/aceroficial/366/ca8d5fd0ff7eba7df4acb2aa4009c2cb.jpg'
    await bot.send_photo(chat_id=user_id, photo=rasm)


@dp.message_handler(text='Lenovo')
async def bot_start(message: types.Message):
    user_id = message.from_user.id
    rasm = 'https://user43214.clients-cdnnow.ru/image/cache/catalog/347/347600_c3817-1000x1000.jpg'
    await bot.send_photo(chat_id=user_id, photo=rasm)
