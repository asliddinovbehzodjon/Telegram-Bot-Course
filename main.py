token = 'Sizning tokeningiz'
from aiogram import types,Bot,Dispatcher
from aiogram.utils import executor
from keyboards import btn
bot = Bot(token=token)
dp = Dispatcher(bot=bot)
@dp.message_handler(commands='start')
async def test(message:types.Message):
    await message.answer('Assalomu alaykum!',reply_markup=btn)
@dp.message_handler(content_types='contact',is_sender_contact=True)
async def test(message:types.Message):
    await message.answer('Raqam qabul qilindi!')
@dp.message_handler(content_types='location')
async def test(message:types.Message):
    print(message.location)
    await message.answer('Manzil qabul qilindi!')
@dp.callback_query_handler(text='python')
async def test(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    # await call.answer('Inline tugma bosildi!',show_alert=True)
    await call.message.answer('Inline tugma bosildi!')

if __name__=='__main__':
    executor.start_polling(dispatcher=dp)