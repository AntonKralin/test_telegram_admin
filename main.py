from aiogram import Bot, Dispatcher
import asyncio

from handlers.DefaultRouter import default_router
from config_reader import config
import classes.db


async def main():
    """Start bot"""
    bot = Bot(token=config.get("BOT_TOKEN"))
    dispatcher = Dispatcher()

    dispatcher.include_router(default_router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dispatcher.start_polling(bot)

if __name__ == "__main__":

    asyncio.run(main())
