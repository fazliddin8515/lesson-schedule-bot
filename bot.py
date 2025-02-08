import os
from aiogram import Bot
from dotenv import load_dotenv
from aiogram.types import BotCommand

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(BOT_TOKEN)

commands = [
    BotCommand(command="start", description="botni boshlash"),
    BotCommand(command="edit_lessons", description="dars qo'shish"),
    BotCommand(command="schedule", description="jadvalni ko'rish"),
]


async def set_commands(commands):
    await bot.set_my_commands(commands)
