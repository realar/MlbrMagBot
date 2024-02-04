import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keep_alive import keep_alive
keep_alive()


bot = Bot(token=os.environ.get('token'))
dp = Dispatcher()

@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    web_app_button = InlineKeyboardButton(text="Открыть Web App",
                                          web_app=types.WebAppInfo(url="https://mlbr-plus.bubbleapps.io/version-test/index?debug_mode=true"))
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[web_app_button]])
    await message.answer("Нажмите кнопку, чтобы открыть Web App:", reply_markup=keyboard)

async def main():
    await dp.start_polling(bot)  # Передаем экземпляр бота в start_polling

if __name__ == '__main__':
    asyncio.run(main())
