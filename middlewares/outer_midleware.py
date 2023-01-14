from aiogram import BaseMiddleware
from aiogram.types import Update, Message
from typing import Dict, Callable, Any, Awaitable

from other.logger import get_logger
from classes.user_dao import UsersDAO
from classes.Enums import UserType
from classes.db import get_session


class UserCheckBlock(BaseMiddleware):
    """outer midleware to skip block user"""
    async def __call__(self,
                handler: Callable[[Update, Dict[str, Any]], Awaitable[Any]],
                event: Message,
                data: Dict[str, Any]) -> Any:
        user_dao = UsersDAO(get_session())
        user_list = user_dao.find_by_type(UserType.block.value)
        for i_user in user_list:
            if i_user.id == event.from_user.id:
                logger = get_logger()
                logger.info("UsercheckBlock, block_user: " + str(event.from_user.id))
                await event.answer(event.from_user.id)
                return
        return await handler(event, data)
