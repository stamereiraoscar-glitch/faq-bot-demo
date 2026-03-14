import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command
import config

bot = Bot(token=config.8621904034:AAHc8l1qCJCKJPdlSVIQTi_C5RZPR-mwZ4w)
dp = Dispatcher()

lang = config.LANGUAGE

menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📋 Services")],
        [KeyboardButton(text="💰 Prices")],
        [KeyboardButton(text="📞 Contacts")],
        [KeyboardButton(text="✉️ Contact manager")]
    ],
    resize_keyboard=True
)

@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(
        config.TEXTS[lang]["start"],
        reply_markup=menu
    )

@dp.message(lambda message: message.text == "📋 Services")
async def services(message: Message):
    await message.answer(config.TEXTS[lang]["services"])

@dp.message(lambda message: message.text == "💰 Prices")
async def prices(message: Message):
    await message.answer(config.TEXTS[lang]["prices"])

@dp.message(lambda message: message.text == "📞 Contacts")
async def contacts(message: Message):
    await message.answer(config.TEXTS[lang]["contacts"])

@dp.message(lambda message: message.text == "✉️ Contact manager")
async def contact_manager(message: Message):
    await message.answer(config.TEXTS[lang]["contact_manager"])

@dp.message()
async def forward_to_admin(message: Message):
    await bot.send_message(
        config.ADMIN_ID,
        f"New message:\n\n"
        f"User: {message.from_user.full_name}\n"
        f"ID: {message.from_user.id}\n\n"
        f"{message.text}"
    )
    await message.answer(config.TEXTS[lang]["sent"])

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
