token = 'Sizning tokeningiz'
from aiogram import types,Dispatcher,Bot
from aiogram.utils import  executor
from keyboards import buttons
bot = Bot(token=token)
dp = Dispatcher(bot=bot)
@dp.message_handler(commands='start')
async def test(message:types.Message):
    fruits = [
        'Olma','Nok','Apelsin','O\'rik','Shaftoli'
    ]
    await message.answer(f'Salom {message.from_user.full_name}\n'
                         f'Mevalardan birini tanlang!',reply_markup=buttons(fruits))
@dp.message_handler(text=[ 'Olma','Nok','Apelsin','O\'rik','Shaftoli'])
async def fruit(message:types.Message):
    await message.answer(f"Siz tanlagan {message.text} meva juda zo'r!")
if __name__ =='__main__':
    executor.start_polling(dispatcher=dp)
