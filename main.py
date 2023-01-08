from aiogram import Bot, Dispatcher
import asyncio

from handlers.DefaultRouter import default_router
from classes.user_dao import UsersDAO
from classes.models import Users
from classes.Enums import UserType
import classes.db as db
import config_reader as cr


async def main():
    """Start bot"""
    bot = Bot(token=cr.config.get("BOT_TOKEN"))
    dispatcher = Dispatcher()

    dispatcher.include_router(default_router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dispatcher.start_polling(bot)

if __name__ == "__main__":
    logger = cr.get_logger()
    id_super = cr.config.get("")
    superadmin = Users(id=id_super, type=UserType.superadmin.value)
    user_dao = UsersDAO(db.get_session())
    user_dao.insert(superadmin)
    logger.info(id_super)
    asyncio.run(main())
