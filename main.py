import asyncio
from bot import bot
from dispatcher import dp
from models import Base
from my_mysql import engine
from bot import set_commands, commands

Base.metadata.create_all(engine)


async def on_start():
    await set_commands(commands)
    print("bot has been started....")


async def main():
    dp.startup.register(on_start)
    await dp.start_polling(bot)


asyncio.run(main())
