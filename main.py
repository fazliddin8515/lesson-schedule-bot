import asyncio
from bot import bot
from dispatcher import dp

def on_start():
    print("bot has been started....")

async def main():   
    dp.startup.register(on_start)
    await dp.start_polling(bot)

asyncio.run(main())
