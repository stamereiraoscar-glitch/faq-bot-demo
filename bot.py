import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command
import config

bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher()

lang = config.LANGUAGE

if lang == "RU":
    main_menu = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📋 Услуги"), KeyboardButton(text="💰 Цены")],
            [KeyboardButton(text="📞 Контакты"), KeyboardButton(text="✉️ Связаться с менеджером")]
        ],
        resize_keyboard=True
    )

    back_menu = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="⬅️ Назад")]
        ],
        resize_keyboard=True
    )
else:
    main_menu = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📋 Services"), KeyboardButton(text="💰 Prices")],
            [KeyboardButton(text="📞 Contacts"), KeyboardButton(text="✉️ Contact manager")]
        ],
        resize_keyboard=True
    )

    back_menu = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="⬅️ Back")]
        ],
        resize_keyboard=True
    )


@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(
        config.TEXTS[lang]["start"],
        reply_markup=main_menu
    )


@dp.message(lambda message: message.text in ["📋 Услуги", "📋 Services"])
async def services(message: Message):
    await message.answer(
        config.TEXTS[lang]["services"],
        reply_markup=back_menu
    )


@dp.message(lambda message: message.text in ["💰 Цены", "💰 Prices"])
async def prices(message: Message):
    await message.answer(
        config.TEXTS[lang]["prices"],
        reply_markup=back_menu
    )


@dp.message(lambda message: message.text in ["📞 Контакты", "📞 Contacts"])
async def contacts(message: Message):
    await message.answer(
        config.TEXTS[lang]["contacts"],
        reply_markup=back_menu
    )


@dp.message(lambda message: message.text in ["✉️ Связаться с менеджером", "✉️ Contact manager"])
async def contact_manager(message: Message):
    await message.answer(
        config.TEXTS[lang]["contact_manager"],
        reply_markup=back_menu
    )


@dp.message(lambda message: message.text in ["⬅️ Назад", "⬅️ Back"])
async def go_back(message: Message):
    await message.answer(
        config.TEXTS[lang]["back_to_menu"],
        reply_markup=main_menu
    )


@dp.message()
async def forward_to_admin(message: Message):
    if message.text in [
        "📋 Услуги", "📋 Services",
        "💰 Цены", "💰 Prices",
        "📞 Контакты", "📞 Contacts",
        "✉️ Связаться с менеджером", "✉️ Contact manager",
        "⬅️ Назад", "⬅️ Back"
    ]:
        return

    await bot.send_message(
        config.ADMIN_ID,
        f"📩 New message from FAQ bot\n\n"
        f"Name: {message.from_user.full_name}\n"
        f"User ID: {message.from_user.id}\n"
        f"Username: @{message.from_user.username if message.from_user.username else 'no username'}\n\n"
        f"Message:\n{message.text}"
    )

    await message.answer(
        config.TEXTS[lang]["sent"],
        reply_markup=main_menu
    )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
