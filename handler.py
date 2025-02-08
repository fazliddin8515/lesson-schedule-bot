from aiogram.types import Message
from my_mysql import Session
from sqlalchemy import delete, insert, select
from models import Lesson


async def start_handler(message: Message):
    await message.answer(f"{message.from_user.first_name} bot xush kelibsiz!")


async def edit_lessons_handler(message: Message):
    text = message.text
    parts = text.split(" ", 2)
    day_name = parts[1]
    lessons = parts[2].split(",")

    session = Session()
    delete_stmt = delete(Lesson).where(Lesson.day_name == day_name)
    session.execute(delete_stmt)

    for i, lesson in enumerate(lessons):
        insert_stmt = insert(Lesson).values(
            lesson_name=lesson.strip(), day_name=day_name, lesson_order=i + 1
        )
        session.execute(insert_stmt)

    session.commit()
    session.close()
    await message.answer(f"{lessons} darslar {day_name} kuniga qo'shildi.")


async def schedule_handler(message: Message):
    days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
    schedule = ""

    for day in days:
        day_lessons = f"{day}: \n"
        session = Session()
        select_stmt = select(Lesson).where(Lesson.day_name == day)
        result = session.execute(select_stmt)
        lessons = result.scalars().all()

        for i, lesson in enumerate(lessons):
            day_lessons += f"{i + 1}. {lesson.lesson_name} \n"
        schedule += day_lessons + "\n"
        session.close()

    await message.answer(schedule)
