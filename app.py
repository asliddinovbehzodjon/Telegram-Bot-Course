from aiogram import types,Bot,Dispatcher
from aiogram.utils import executor
from io import BytesIO
token = 'Bot Tokeniz'
bot = Bot(token=token)
dp = Dispatcher(bot=bot)
@dp.message_handler(commands='start')
async def test(message:types.Message):
    await message.answer(f'Salom {message.from_user.full_name}')
@dp.message_handler(content_types='photo') 
async def get_photo(msg:types.Message):
    file_id = msg.photo[-1].file_id
    file = await bot.get_file(file_id=file_id)
    file_url = bot.get_file_url(file_path=file.file_path)
    print(file_url)
    await msg.answer('Rasm qabul qilindi!')   
@dp.message_handler(content_types='document')
async def get_document(msg:types.Message):
    doc = BytesIO()
    document = msg.document
    await document.download(doc)
    # file_id = document.file_id
    # file = await bot.get_file(file_id=file_id)
    # file_url = bot.get_file_url(file_path=file.file_path)
    # print(file_url)
    doc.seek(0)
    file = types.InputFile(doc,filename='Behzod.pdf')
    await msg.answer_document(document=file)
    await msg.answer('Document qabul qilindi!')
# Media(Image,Audio,File(document),Video)
if __name__ == '__main__':
    executor.start_polling(dispatcher=dp)
