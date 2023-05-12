from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

dokon_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Telefonlar"),
            KeyboardButton(text="Kompyuterlar")
        ],
        [
            KeyboardButton(text="Maishiy texnikalar"),
            KeyboardButton(text="Aksessuarlar")
        ],
        [
            KeyboardButton(text='Kontakt',request_contact=True),
            KeyboardButton(text='Lokatsiya',request_location=True)
        ],
        [
            KeyboardButton(text='Adminga murojat')
        ]
    ],
    resize_keyboard=True
)