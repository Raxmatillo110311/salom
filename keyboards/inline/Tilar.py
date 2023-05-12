from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton

tilar_buttons = InlineKeyboardMarkup(
    keyboard=[
        [
            InlineKeyboardButton(text='Uzb'),
            InlineKeyboardButton(text='RU')
        ],
        [
            InlineKeyboardButton(text='ENG')
        ]
    ]
)
