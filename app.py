from aiogram import types,Bot,Dispatcher
from aiogram.utils import executor
import asyncio
token = 'Telegram bot tokeningiz'
bot = Bot(token=token)
dp = Dispatcher(bot=bot)
@dp.message_handler(commands='start')
async def start(message:types.Message):
    chat_id = message.from_user.id
    # await bot.send_message(chat_id=chat_id,text='Salom !')
    image = open('Resources/photo.png','rb')
    video = open('Resources/video.mp4','rb')
    document = open('Resources/document.docx','rb')
    audio = open('Resources/audio.mp3','rb')
    gif = open('Resources/gif.mp4','rb')
    contact = '+998910080886'
    latitude=41.2995
    longitude =69.2401 
    sticker = open('Resources/sticker.tgs','rb')
    voice = open('Resources/voice.ogg','rb')
    # media_group = types.MediaGroup()
    # # media_group.attach_document(document,caption='Bu Document')
    # media_group.attach_photo(image,caption='Bu Rasm')
    # media_group.attach_video(video,caption='Bu Video')
    black='◼️'
    white='◻️'
    xabar = await bot.send_message(chat_id=chat_id,text=10*white)
    for i in range(1,11):
        qora = i*black
        oq  = (10-i) * white
        await bot.send_chat_action(chat_id=chat_id,action=types.ChatActions.UPLOAD_VIDEO)
        await xabar.edit_text(f"{qora}{oq}\n"
                              f"{i*10} % yuklandi")
        await asyncio.sleep(1)
    await xabar.delete()
    await message.answer('Yuklandi!')
if __name__ =='__main__':
    executor.start_polling(dispatcher=dp)