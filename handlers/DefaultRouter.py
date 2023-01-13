from aiogram import Router
from aiogram.types import Message
from aiogram.filters.command import Command

from filters.AdminFilter import UserTypeFilter
from classes.Enums import UserType

default_router = Router()


@default_router.message(Command("start"), UserTypeFilter(UserType.superadmin.value))
async def superadmin_start(message: Message):
    await message.answer("welcome superadmin")


@default_router.message(Command("start"))
async def user_start(message: Message):
    await message.answer("welcome")
