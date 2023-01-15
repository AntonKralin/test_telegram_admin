from aiogram import Router
from aiogram.types import Message
from aiogram.filters.command import Command

from other.enums import UserType
from filters.AdminFilter import UserTypeFilter
from db.db import get_session
from db.user_dao import UsersDAO
from other.logger import get_logger

admin_router = Router()


@admin_router.message(Command("removeadmin"), UserTypeFilter(UserType.superadmin.value))
async def remove_admin(message: Message):
    pass


@admin_router.message(Command("setadmin"), UserTypeFilter(UserType.superadmin.value))
async def set_admin(message: Message):
    entities = message.entities or []
    for item in entities:
        print(item)
        if item.type == 'mention':
            await message.answer(item.extract_from(message.text))


@admin_router.message(Command("adminlist"), UserTypeFilter(UserType.superadmin.value))
async def admin_list(message: Message):
    logger = get_logger()
    logger.info("adminlist")
    u_dao = UsersDAO(get_session())
    u_list = await u_dao.find_by_type(UserType.admin.value)
    u_list.append(u_list[0])
    s_user = ""
    for i_user in u_list:
        s_user = ",@".join([s_user, i_user.name])
    s_user = s_user[1:len(s_user)]
    await message.answer(s_user)


@admin_router.message(Command("superadminlist"), UserTypeFilter(UserType.superadmin.value))
async def superadmin_list(message: Message):
    logger = get_logger()
    logger.info("superadminlist")
    u_dao = UsersDAO(get_session())
    u_list = await u_dao.find_by_type(UserType.superadmin.value)
    u_list.append(u_list[0])
    s_user = ""
    for i_user in u_list:
        s_user = ",@".join([s_user, i_user.name])
    s_user = s_user[1:len(s_user)]
    await message.answer(s_user)
