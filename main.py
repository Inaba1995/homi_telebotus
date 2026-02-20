import asyncio
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile
from aiogram import Bot, Dispatcher, F
from config import TOKEN
import random
from gtts import gTTS
import os
from googletrans import Translator
translator = Translator()

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp. message(CommandStart())
async def start(message: Message):
    await message.answer(f"Привет, {message.from_user.first_name}, гони свои фоточки, будем сохранять! А так же переводить твою белиберду на инглишь!")


@dp.message(F.text & ~Command())
async def reply(message: Message):
    user_text = message.text

    try:
        translation = translator.translate(user_text, src='ru', dest='en')
        translated_text = translation.text
    except Exception as e:
        translated_text = f"Ошибка перевода: {e}"


    response_text = (
        f"🗣 Ваш текст: {user_text}\n\n"
        f"🇬🇧 Перевод на английский: {translated_text}"
    )

    await message.answer(response_text)

    tts = gTTS(text=translated_text, lang='en')
    tts.save("reply.ogg")
    audio = FSInputFile('reply.ogg')
    await bot.send_voice(chat_id=message.chat.id, voice=audio)
    os.remove("reply.ogg")

@dp. message(F.photo)
async def save_photo(message: Message):
    await bot.download(message.photo[-1], destination=f'img/{message.photo[-1].file_id}.jpg')
    await message.answer(f"Сохранил!")


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())