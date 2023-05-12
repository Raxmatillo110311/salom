from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

Aksessuarlar_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Airpods'),
            KeyboardButton(text="Naushnik")
        ],
        [
            KeyboardButton(text="Flesgka"),
            KeyboardButton(text="Chip")
        ],
        [
            KeyboardButton(text="Orqaga")
        ]
    ],
    resize_keyboard=True
)