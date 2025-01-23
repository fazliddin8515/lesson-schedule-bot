from aiogram import Dispatcher
from aiogram.filters import Command
from handler import start_handler, add_lessons_handler, schedule_handler

dp = Dispatcher()

dp.message.register(start_handler, Command("start"))
dp.message.register(add_lessons_handler, Command("add_lessons"))
dp.message.register(schedule_handler, Command("schedule"))
