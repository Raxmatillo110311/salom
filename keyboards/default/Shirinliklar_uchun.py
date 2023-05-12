from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

shirinliklar_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Xolva"),
            KeyboardButton(text="Pechenee")
         ],
        [
            KeyboardButton(text="Shokolad"),
            KeyboardButton(text="Chupa-chups")
        ]
    ],
    resize_keyboard=True
)