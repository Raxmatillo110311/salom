from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton

tillar_button=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="o'zbek tili",callback_data='til1'),
            InlineKeyboardButton(text="rus tili",callback_data='til2')
        ],
        [
            InlineKeyboardButton(text="eng tili",callback_data='til3')
        ],
        [
            InlineKeyboardButton(text="Ulashish",switch_inline_query='')
        ]
    ]
)

























