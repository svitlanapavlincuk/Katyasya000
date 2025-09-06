import logging
import os
from aiogram import Bot, Dispatcher, executor, types
import openai

# Витягуємо токени з Environment Variables (Render -> Environment)
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

openai.api_key = OPENAI_API_KEY

# Налаштування бота
bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

@dp.message_handler()
async def chat_with_ai(message: types.Message):
    try:
        # Виклик до ChatGPT
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # можна змінити на "gpt-4"
            messages=[{"role": "user", "content": message.text}],
            max_tokens=200,
            temperature=0.7
        )
        answer = response["choices"][0]["message"]["content"].strip()
        await message.answer(answer)

    except Exception as e:
        await message.answer("⚠️ Помилка: " + str(e))

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
