import asyncio
from bot import bot
from dispatcher import dp
from models import Base
from my_mysql import engine

Base.metadata.create_all(engine)


def on_start():
    print("bot has been started....")


async def main():
    dp.startup.register(on_start)
    await dp.start_polling(bot)


asyncio.run(main())
