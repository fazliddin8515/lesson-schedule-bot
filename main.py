import os
import asyncio
import sqlite3
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from dotenv import load_dotenv

load_dotenv()

connection = sqlite3.connect("databese.sqlite")
cursor = connection.cursor()

create_lessons_table_query = '''
CREATE TABLE IF NOT EXISTS lessons (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    lesson_name VARCHAR NOT NULL,
    day_name VARCHAR NOT NULL,
    lesson_order INTEGER NOT NULL
)
'''

cursor.execute(create_lessons_table_query)

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_handler(message: Message):
    await message.answer(f"{message.from_user.first_name} bot xush kelibsiz!")

@dp.message(Command("add_lessons"))
async def add_lesson_handler(message: Message):
    text = message.text
    parts = text.split(" ", 2)
    day_name = parts[1]
    lessons = parts[2].split(",")
    insert_lessons_query = '''
    INSERT INTO lessons (lesson_name, day_name, lesson_order) VALUES (?, ?, ?)
    '''
    for i, lesson in enumerate(lessons):
        cursor.execute(insert_lessons_query, (lesson.strip(), day_name, i + 1))
    
    connection.commit() # INSERT, UPDATE, DELETE
    
    await message.answer(f"{lessons} darslar {day_name} kuniga qo'shildi.")
    

@dp.message(Command("schedule"))
async def schedule_handler(message: Message):
    select_lessons_query = '''
    SELECT lesson_name FROM lessons WHERE day_name = ? ORDER BY lesson_order;
    '''
    days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
    schedule = ""

    for day in days:
        day_lessons = f"{day}: \n"
        cursor.execute(select_lessons_query, (day,))
        fetched_lessons = cursor.fetchall()
        for i, lesson in enumerate(fetched_lessons):
            day_lessons += f"{i + 1}. {lesson[0]} \n"
        schedule += day_lessons + "\n"

    await message.answer(schedule)

async def main():
    print("bot has been started...")
    await dp.start_polling(bot)

asyncio.run(main())

