import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from transformers import pipeline

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher()

# Создаём модель для перефразирования
rephraser = pipeline("text2text-generation", model="Vamsi/T5_Paraphrase_Paws")

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
        "Привет! Пришли текст новости, и я перефразирую его для канала.\n\n"
        "Формат:\n"
        "Важлива или Звичайна + до N символов\n"
        "Текст новости"
    )

@dp.message()
async def rewrite(message: types.Message):
    user_text = message.text
    result = rephraser(user_text, max_length=512, do_sample=False)
    text = result[0]['generated_text']
    # Добавляем ⚡️ или ⚡️⚡️⚡️ и ссылку
    if "Важлива" in user_text:
        prefix = "⚡️⚡️⚡️"
    else:
        prefix = "⚡️"
    text = f"{prefix} {text}\n\n<a href='https://t.me/factum_ua'>Фактум Новини | Підписатись</a>"
    await message.answer(text)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
