from aiogram import Bot, Dispatcher
import asyncio

from handlers.DefaultRouter import default_router
from config_reader import config
from classes.user_dao import UsersDAO
from classes.models import Users
from classes.Enums import UserType
import classes.db as db


async def main():
    """Start bot"""
    bot = Bot(token=config.get("BOT_TOKEN"))
    dispatcher = Dispatcher()

    dispatcher.include_router(default_router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dispatcher.start_polling(bot)

if __name__ == "__main__":
    id_super = config.get("")
    superadmin = Users(id=id_super, type=UserType.superadmin.value)
    user_dao = UsersDAO(db.get_session())
    user_dao.insert(superadmin)
    asyncio.run(main())
