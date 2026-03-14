import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command

BOT_TOKEN = "8621904034:AAHc8l1qCJCKJPdlSVIQTi_C5RZPR-mwZ4w"
ADMIN_ID = 123456789

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

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
        "Welcome 👋\n\nChoose a section:",
        reply_markup=menu
    )

@dp.message(lambda message: message.text == "📋 Services")
async def services(message: Message):
    await message.answer(
        "Our services:\n\n"
        "• Telegram bots\n"
        "• Discord bots\n"
        "• AI chatbots\n"
        "• Business automation"
    )

@dp.message(lambda message: message.text == "💰 Prices")
async def prices(message: Message):
    await message.answer(
        "Example prices:\n\n"
        "• FAQ bot — from $60\n"
        "• Lead bot — from $100\n"
        "• AI bot — from $150"
    )

@dp.message(lambda message: message.text == "📞 Contacts")
async def contacts(message: Message):
    await message.answer(
        "Contacts:\n\nTelegram: @yourusername"
    )

@dp.message(lambda message: message.text == "✉️ Contact manager")
async def contact_manager(message: Message):
    await message.answer("Write your message and the manager will reply.")

@dp.message()
async def forward_to_admin(message: Message):
    await bot.send_message(
        ADMIN_ID,
        f"New message:\n\n"
        f"User: {message.from_user.full_name}\n"
        f"ID: {message.from_user.id}\n\n"
        f"{message.text}"
    )
    await message.answer("Message sent to manager ✅")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
