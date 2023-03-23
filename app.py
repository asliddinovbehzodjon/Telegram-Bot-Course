token ='Telegram bot tokeniz'
from aiogram import types,Dispatcher,Bot
from aiogram.dispatcher.filters.builtin import Command,CommandHelp,CommandPrivacy,CommandSettings,CommandStart
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text,Regexp
bot = Bot(token=token)
dp  = Dispatcher(bot=bot)
phone_check=r'^[\+]?[0-9]{3}?[0-9]{2}[0-9]{7}$'
@dp.message_handler(hashtags=['behzod'])
async def phone(message:types.Message):
    await message.answer('Behzod Milliarder!')
# @dp.message_handler(content_types=types.ContentType.TEXT)
# @dp.message_handler(content_types=types.ContentType.ANY)
# async def analyze_type(message:types.Message):
#     print(message.content_type)
#     await message.answer('Nomalum tip yubordiz')
#### Commands ############################
# @dp.message_handler(CommandStart(deep_link='uzmovicom'))
# async def uzmovi(message:types.Message):
#     await message.answer('Uzmovi saytidan kelgan mehmon!')
# @dp.message_handler(CommandStart())   # Command('start')  commands='start'
# async def start(message:types.Message):
#     await message.answer('Salom')
# # @dp.message_handler(commands='test')
# @dp.message_handler(Command('test'))
# async def test(message:types.Message):
#     await message.answer('Test ishlaysizmi?')
# @dp.message_handler(commands='settings')
# async def settings(message:types.Message):
#     await message.answer("Sozlamar bo'limiga o'tasizmi?")
if __name__ =='__main__':
    executor.start_polling(dispatcher=dp)