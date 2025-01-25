from aiogram.types import Message
from my_mysql import cursor, connection
from queries import insert_lessons_query, select_lessons_query, delete_lessons_query

async def start_handler(message: Message):
    await message.answer(f"{message.from_user.first_name} bot xush kelibsiz!")

async def edit_lessons_handler(message: Message):
    text = message.text
    parts = text.split(" ", 2)
    day_name = parts[1]
    lessons = parts[2].split(",")
    
    cursor.execute(delete_lessons_query, (day_name,))

    for i, lesson in enumerate(lessons):
        cursor.execute(insert_lessons_query, (lesson.strip(), day_name, i + 1))
    
    connection.commit() # INSERT, UPDATE, DELETE
    
    await message.answer(f"{lessons} darslar {day_name} kuniga qo'shildi.")
  
async def schedule_handler(message: Message):
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
