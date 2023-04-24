from aiogram.types import  ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardMarkup,InlineKeyboardButton
# btn = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
# btn.add(KeyboardButton(text="Raqamni ulashish",request_contact=True))
# btn.add(KeyboardButton(text="Manzilni ulashing",request_location=True))
# btn.add(KeyboardButton(text="Youtube",web_app={"url":'https://youtube.com/@BehzodAsliddinov'}))
btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Python",callback_data='python'),
            InlineKeyboardButton(text="Python kursi",url='https://youtube.com/')
        ],
        [
            InlineKeyboardButton(text="Botni ulashish", switch_inline_query="Bu bot o'quv markazlar uchun"),
            InlineKeyboardButton(text="Qidirish", switch_inline_query_current_chat='python')
        ],
[
            InlineKeyboardButton(text="Youtube", web_app={'url':'https://youtube.com'}),

        ]
    ]
)
