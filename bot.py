import os
import asyncio
from aiogram import Bot, Dispatcher, types
import openai

BOT_TOKEN = os.getenv("8318308827:AAETNYSdNhyNdihIWm29jTGMc1XNFaBOEdA")
OPENAI_API_KEY = os.getenv("")

bot = Bot(token=BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher()
openai.api_key = OPENAI_API_KEY

@dp.message()
async def rewrite(message: types.Message):
    user_text = message.text
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": f"Перефразуй цей текст українською: {user_text}"}]
    )
    text = response['choices'][0]['message']['content']
    prefix = "⚡️⚡️⚡️" if "Важлива" in user_text else "⚡️"
    text = f"{prefix} {text}\n\n<a href='https://t.me/factum_ua'>Фактум Новини | Підписатись</a>"
    await message.answer(text)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
