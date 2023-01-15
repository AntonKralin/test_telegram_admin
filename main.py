from aiogram import Bot, Dispatcher
import asyncio

from handlers.default_router import default_router
from handlers.superadmin_router import admin_router
from other.configs import config
from other.logger import get_logger
from db.user_dao import UsersDAO
from db.models import Users
from other.enums import UserType
from middlewares.outer_midleware import UserCheckBlock
import db.db as db


async def main():
    """Start bot"""
    bot = Bot(token=config.get("BOT_TOKEN"))
    dispatcher = Dispatcher()

    id_super = config.get("SUPER_ADMIN")
    superadmin = Users(id=id_super, type=UserType.superadmin.value)
    user_dao = UsersDAO(db.get_session())
    await user_dao.insert(superadmin)
    logger.info(id_super)

    #register routers
    dispatcher.include_router(default_router)
    dispatcher.include_router(admin_router)

    #register midleware
    dispatcher.message.outer_middleware(UserCheckBlock())

    await bot.delete_webhook(drop_pending_updates=True)
    await dispatcher.start_polling(bot)

if __name__ == "__main__":
    logger = get_logger()
    asyncio.run(main())
