token = '6132542810:AAER-6ZD6pWBStfvJ-szaqed7gUy2Pr4Vqo'
from aiogram import types,Bot,Dispatcher
from aiogram.utils import executor
from states import Register
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
bot = Bot(token=token)
dp = Dispatcher(bot=bot,storage=MemoryStorage())
@dp.message_handler(commands='start',state=None)
async def test(message:types.Message):
    await message.answer(f'Salom {message.from_user.full_name}!\n'
                         f'Ro\'yxatdan o\'tish uchun /register buyrugini bosing!')
@dp.message_handler(commands='register')
async def started(msg:types.Message):
    await  msg.answer('Ismingizni kiriting:\n'\
               'Masalan: Behzod Asliddinov')
    await Register.name.set()
@dp.message_handler(state=Register.name)
async def get_name(msg:types.Message,state:FSMContext):
    name = msg.text
    await state.update_data({
        'name':name
    })
    await msg.answer("Yoshingizni kiriting:\n"
                     "Masalan:23")
    await Register.next()
@dp.message_handler(state=Register.age)
async def get_age(msg:types.Message,state:FSMContext):
    age = msg.text
    await state.update_data({
        'age':age
    })
    data  = await state.get_data()
    await msg.answer(f"Sizning ismingiz: {data['name']}\n"
                     f"Yoshingiz: {data['age']}")
    await state.finish()

if __name__ =='__main__':
    executor.start_polling(dispatcher=dp)