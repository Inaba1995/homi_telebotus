import asyncio
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile
from aiogram import Bot, Dispatcher, F
from config import TOKEN
import random
from gtts import gTTS
import os
from googletrans import Translator

bot = Bot(token=TOKEN)
dp = Dispatcher()



@dp.message()
async def reply (message: Message):
    ms = "Бу! Испугался? Не бойся! Я всего лишь бот, способный сохранять твои фоточки и переводить твой текст на инглиш!"
    mss= ms
    await message.answer(f"{mss}")

    tts = gTTS(text=mss, lang='ru')
    tts.save("reply.mp3")
    audio = FSInputFile('reply.mp3')
    await bot.send_audio(message.chat.id, audio)
    os.remove("reply.mp3")



@dp. message(CommandStart())
async def start(message: Message):
    await message.answer(f"Привет, {message.from_user.first_name}, гони свои фоточки, будем сохранять! А так же переводить твою белиберду на инглишь!")

@dp. message(F.photo)
async def save_photo(message: Message):
    await bot.download(message.photo[-1], destination=f'img/{message.photo[-1].file_id}.jpg')
    await message.answer(f"Сохранил!")


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())