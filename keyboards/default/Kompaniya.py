from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

kompaniya = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Iphone'),
            KeyboardButton(text='Samsung')
        ],
        [
            KeyboardButton(text='Xiaomi'),
            KeyboardButton(text='LG')
        ],
        [
            KeyboardButton(text='Microsoft'),
            KeyboardButton(text='Nokia')
        ],
        [
            KeyboardButton(text='NOVEY'),
            KeyboardButton(text='VIVO')
        ],
        [
            KeyboardButton(text='POCO'),
            KeyboardButton(text='Xonor')
        ],
        [
            KeyboardButton(text='Tecno')
        ]
    ],
    resize_keyboard=True
)