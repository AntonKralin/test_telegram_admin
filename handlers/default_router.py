from aiogram import Router
from aiogram.types import Message
from aiogram.filters.command import Command

from db.models import Users
from filters.admin_filter import UserTypeFilter
from other.enums import UserType
from db.db import get_session
from db.user_dao import UsersDAO
import other.cons as cons

default_router = Router()


@default_router.message(Command("start"), UserTypeFilter(UserType.superadmin.value))
async def superadmin_start(message: Message):
    """Command start for superadmin"""
    user = Users()
    user.id = message.from_user.id
    user.name = message.from_user.username
    user.type = UserType.superadmin.value
    u_dao = UsersDAO(get_session())
    await u_dao.insert(user)
    await message.answer("welcome superadmin")


@default_router.message(Command("start"), UserTypeFilter(UserType.admin.value))
async def superadmin_start(message: Message):
    """Command start for admin"""
    user = Users()
    user.id = message.from_user.id
    user.name = message.from_user.username
    user.type = UserType.admin.value
    u_dao = UsersDAO(get_session())
    await u_dao.insert(user)
    await message.answer("welcome admin")


@default_router.message(Command("start"))
async def user_start(message: Message):
    """Command start for user"""
    user = Users()
    user.id = message.from_user.id
    user.name = message.from_user.username
    user.type = UserType.user.value
    u_dao = UsersDAO(get_session())
    await u_dao.insert(user)
    await message.answer("welcome")


@default_router.message(Command("help"), UserTypeFilter(UserType.superadmin.value))
async def superadmin_help(message: Message):
    """Command help for superadmin"""
    answer = ""
    for i_command in cons.syper_admin_command:
        answer += i_command + "\n"
    for i_command in cons.admin_command:
        answer += i_command + "\n"
    await message.answer(answer, parse_mode="HTML")


@default_router.message(Command("help"), UserTypeFilter(UserType.admin.value))
async def admin_help(message: Message):
    """Command help for admin"""
    answer = ""
    for i_command in cons.admin_command:
        answer += i_command + "\n"
    await message.answer(answer, parse_mode="HTML")


@default_router.message(Command("help"))
async def help(message: Message):
    """Command help for users"""
    answer = "1"
    for i_command in cons.user_command:
        answer += i_command + "\n"
    await message.answer(answer, parse_mode="HTML")
