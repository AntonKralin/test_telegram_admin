from aiogram import Bot, Dispatcher
import asyncio
from handlers.DefaultRouter import default_router

from other.configs import config
from other.logger import get_logger
from classes.user_dao import UsersDAO
from classes.models import Users
from classes.Enums import UserType
from middlewares.outer_midleware import UserCheckBlock
import classes.db as db


async def main():
    """Start bot"""
    bot = Bot(token=config.get("BOT_TOKEN"))
    dispatcher = Dispatcher()

    #register routers
    dispatcher.include_router(default_router)

    #register midleware
    dispatcher.message.outer_middleware(UserCheckBlock())

    await bot.delete_webhook(drop_pending_updates=True)
    await dispatcher.start_polling(bot)

if __name__ == "__main__":
    logger = get_logger()
    id_super = config.get("SUPER_ADMIN")
    superadmin = Users(id=id_super, type=UserType.superadmin.value)
    user_dao = UsersDAO(db.get_session())
    user_dao.insert(superadmin)
    logger.info(id_super)
    asyncio.run(main())
