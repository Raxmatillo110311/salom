from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

orqaga_buttons = ReplyKeyboardMarkup(
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
        ]
    ],
    resize_keyboard=True
)