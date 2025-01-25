from aiogram import Dispatcher
from aiogram.filters import Command
from handler import start_handler, edit_lessons_handler, schedule_handler

dp = Dispatcher()

dp.message.register(start_handler, Command("start"))
dp.message.register(edit_lessons_handler, Command("edit_lessons"))
dp.message.register(schedule_handler, Command("schedule"))
