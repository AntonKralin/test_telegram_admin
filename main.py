from aiogram import Bot, Dispatcher
import asyncio

from classes.models import SuperAdmin, Admin, BlockUser
from handlers.DefaultRouter import default_router
from config_reader import config


async def main():
    """Start bot"""
    bot = Bot(token=config.get("BOT_TOKEN"))
    dispatcher = Dispatcher()

    dispatcher.include_router(default_router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dispatcher.start_polling(bot)

if __name__ == "__main__":
    SuperAdmin.create_table()
    if config.get("SuperAdmin"):
        s_admin = SuperAdmin(id=config.get("SuperAdmin"), name="SuperAdmin")
    Admin.create_table()
    BlockUser.create_table()

    asyncio.run(main())
