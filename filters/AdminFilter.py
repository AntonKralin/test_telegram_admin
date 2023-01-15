from aiogram.filters import Filter
from aiogram.types import Message

from db.user_dao import UsersDAO
from db.db import get_session
from other.enums import UserType


class UserTypeFilter(Filter):
    """Filter messages by type user
    use: @default_router.message(Command("start"), UserTypeFilter(UserType.superadmin.value))"""
    def __init__(self, user_type: UserType):
        self.user_type = user_type

    async def __call__(self, message: Message) -> bool:
        user_dao = UsersDAO(get_session())
        return await user_dao.check_type(message.from_user.id, self.user_type)



