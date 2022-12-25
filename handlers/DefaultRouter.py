from aiogram import Router
from aiogram.types import Message
from aiogram.filters.command import Command

default_router = Router()

@default_router.message(Command("start"))
async def user_start(message: Message):
    await message.answer("start")
