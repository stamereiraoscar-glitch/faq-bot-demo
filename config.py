import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID", "898036971"))

COMPANY_NAME = os.getenv("COMPANY_NAME", "My Company")
CONTACT_USERNAME = os.getenv("CONTACT_USERNAME", "@yourusername")
CONTACT_EMAIL = os.getenv("CONTACT_EMAIL", "your@email.com")

LANGUAGE = os.getenv("LANGUAGE", "RU")

TEXTS = {
    "EN": {
        "start": f"Welcome to {COMPANY_NAME} 👋\n\nChoose a section:",
        "services": """Our services:

• Telegram bot development
• Discord bot development
• AI chatbot integration
• Business automation bots""",
        "prices": """Example prices:

• FAQ bot — from $60
• Lead bot — from $100
• AI bot — from $150""",
        "contacts": f"""Contacts:

Telegram: {CONTACT_USERNAME}
Email: {CONTACT_EMAIL}""",
        "contact_manager": "Write your message and it will be sent to the manager.",
        "sent": "Your message has been sent ✅",
        "back_to_menu": "You are back in the main menu."
    },
    "RU": {
        "start": f"Здравствуйте! Добро пожаловать в {COMPANY_NAME} 👋\n\nВыберите раздел:",
        "services": """Наши услуги:

• Разработка Telegram-ботов
• Разработка Discord-ботов
• Подключение AI в ботов
• Боты для автоматизации бизнеса""",
        "prices": """Примерные цены:

• FAQ-бот — от $60
• Бот заявок — от $100
• AI-бот — от $150""",
        "contacts": f"""Контакты:

Telegram: {CONTACT_USERNAME}
Email: {CONTACT_EMAIL}""",
        "contact_manager": "Напишите сообщение, и оно будет отправлено менеджеру.",
        "sent": "Ваше сообщение отправлено ✅",
        "back_to_menu": "Вы вернулись в главное меню."
    }
}
