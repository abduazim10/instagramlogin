# bot.py
import asyncio
from aiogram import Bot
from aiogram.types import ParseMode

API_TOKEN = '7262421808:AAFBbJHOUYw40r9WBdc8t2c2XiIzAEkQ2Ew'
USER_ID = '6313238207'  # твой Telegram ID

bot = Bot(token=API_TOKEN)

# Функция отправки сообщения в Telegram
async def send_telegram_message(message):
    await bot.send_message(USER_ID, message, parse_mode=ParseMode.HTML)

# Функция, которая будет выполняться при запуске бота (не обязательна)
async def on_start():
    print("Бот запущен и готов отправлять сообщения.")

# Запуск бота в фоновом режиме
if __name__ == '__main__':
    asyncio.run(on_start())
