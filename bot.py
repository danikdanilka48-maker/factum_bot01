import os
import openai
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.utils import executor

TG_TOKEN = os.getenv(
    "8318308827:AAETNYSdNhyNdihIWm29jTGMc1XNFaBOEdA")  # токен Telegram
OPENAI_KEY = os.getenv(
    "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"
)  # ключ OpenAI

bot = Bot(token=TG_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(bot)
openai.api_key = OPENAI_KEY


@dp.message_handler()
async def handle_message(message: types.Message):
    prompt = f"Перефразируй текст: {message.text}\nСделай формат: ⚡️ или ⚡️⚡️⚡️ в начале если нужно, и снизу: Фактум Новини | Підписатись"
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                            messages=[{
                                                "role": "user",
                                                "content": prompt
                                            }],
                                            max_tokens=500)
    text = response['choices'][0]['message']['content']
    await message.reply(text)


if __name__ == "__main__":
    executor.start_polling(dp)
