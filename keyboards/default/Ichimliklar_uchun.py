from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

Ichimliklar_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Fanta"),
            KeyboardButton(text="Cola")
        ],
        [
            KeyboardButton(text="Sprite"),
            KeyboardButton(text="Dena")
        ]
    ],
    resize_keyboard=True
)