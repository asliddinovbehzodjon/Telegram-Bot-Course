from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
# btn = ReplyKeyboardMarkup(resize_keyboard=True,
#     keyboard=[
#
#         [
#             KeyboardButton(text="Maktab")
#         ],
#         [
#             KeyboardButton(text="Universitet"),
#             KeyboardButton(text="Kollej")
#         ],
#     ]
# )
# btn  = ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)
# btn1 = KeyboardButton(text="Universitet")
# btn2 = KeyboardButton(text="Kollej")
# btn3 = KeyboardButton(text="Maktab")
# btn4 = KeyboardButton(text="Bog'cha")
# add,insert,row
# btn.insert(btn4).insert(btn3).insert(btn2).insert(btn1)
# btn.row(btn4,btn3,btn2).row(btn1)
# centers = ["Universitet","Kollej","Maktab","Bog'cha"]
# for i in centers:
#     btn.insert(i)
def buttons(fruits):
    btn = ReplyKeyboardMarkup(resize_keyboard=True,row_width=3)
    for i in fruits:
        btn.insert(i)
    return btn
