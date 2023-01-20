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


class AdminsTypeFiler(Filter):
    """Fileter messages by admins type (superadmin and admin)"""
    async def __call__(self, message: Message) -> bool:
        user_dao = UsersDAO(get_session())
        user = await user_dao.find_by_id(message.from_user.id)
        if (user.type == UserType.admin.value) or (user.type == UserType.superadmin.value):
            return True
        return False


class UsersInMessageFilter(Filter):
    """check is message list of users"""
    async def __call__(self, message: Message) -> bool:
        user_dao = UsersDAO(get_session())
        u_list = message.text.replace("@", "").split(" ")
        for i_user in u_list:
            user = await user_dao.find_by_name(i_user)
            if user:
                return True
        await message.reply("Не найдено ни одного пользователя")
        return False


