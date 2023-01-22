from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters.command import Command
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram import Bot

from other.enums import UserType
from db.user_dao import UsersDAO
from db.db import get_session
from other.logger import get_logger
from filters.admin_filter import AdminsTypeFiler, UsersInMessageFilter


class SendState(StatesGroup):
    set_message = State()
    set_users = State()


class SendAllState(StatesGroup):
    send_message = State()


admin_router = Router()


@admin_router.message(Command("cancel"))
@admin_router.message(F.text.casefold() == "cancel")
async def admin_cancel(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("cancel")


@admin_router.message(Command("blockuser"), AdminsTypeFiler())
async def block_user(message: Message):
    logger = get_logger()
    entities = message.entities or []
    for item in entities:
        if item.type == 'mention':
            nickname = item.extract_from(message.text)
            nickname = nickname.replace("@", "")
            u_dao = UsersDAO(get_session())
            u_admin = await u_dao.find_by_name(nickname)
            if u_admin:
                u_admin.type = UserType.block.value
                u_dao.update(u_admin)
                logger.info(u_admin.name + " block")
                await message.answer(u_admin.name + " block")
            else:
                await message.answer("not find user")


@admin_router.message(Command("unblockuser"), AdminsTypeFiler())
async def unblock_user(message: Message):
    logger = get_logger()
    entities = message.entities or []
    for item in entities:
        if item.type == 'mention':
            nickname = item.extract_from(message.text)
            nickname = nickname.replace("@", "")
            u_dao = UsersDAO(get_session())
            u_admin = await u_dao.find_by_name(nickname)
            if u_admin:
                u_admin.type = UserType.user.value
                u_dao.update(u_admin)
                logger.info(u_admin.name + " unblock")
                await message.answer(u_admin.name + " unblock")
            else:
                await message.answer("not find user")


@admin_router.message(Command("userlist"), AdminsTypeFiler())
async def user_list(message: Message):
    logger = get_logger()
    logger.info("userlist")
    u_dao = UsersDAO(get_session())
    u_list = await u_dao.find_by_type(UserType.user.value)
    u_list.append(u_list[0])
    s_user = ""
    i = 0
    for i_user in u_list:
        i += 1
        s_user = ",@".join([s_user, i_user.name])
        if i % 10 == 0:
            s_user += "\n"
    s_user = s_user[1:len(s_user)]
    await message.answer(s_user)


@admin_router.message(Command("sendall"), AdminsTypeFiler())
async def send_all(message: Message, state: FSMContext):
    await message.answer("Введите сообщение:")
    await state.set_state(SendAllState.send_message)


@admin_router.message(SendAllState.send_message)
async def get_all_message(message: Message, bot: Bot, state: FSMContext):
    u_dao = UsersDAO(get_session())
    u_list = await u_dao.find_by_type(UserType.user.value)
    for i_user in u_list:
        await bot.send_message(i_user.id, message.html_text, parse_mode="HTML")
    await message.answer(f"Отправлено {len(u_list)} сообщений")
    await state.clear()


@admin_router.message(Command("senduser"), AdminsTypeFiler())
async def send_user(message: Message, state: FSMContext):
    await message.answer("Введите пользователей (cancel для отмены), разделитель пробел:")
    await state.set_state(SendState.set_users)


@admin_router.message(SendState.set_users, UsersInMessageFilter())
async def get_users(message: Message, state: FSMContext):
    await state.update_data(users_text=message.text)
    await message.answer("Введите сообщение")
    await state.set_state(SendState.set_message)


@admin_router.message(SendState.set_users)
async def get_wrong_users(message: Message):
    await message.answer("Введите пользователей (cancel для отмены), разделитель пробел:")


@admin_router.message(SendState.set_message)
async def get_message(message: Message, bot: Bot, state: FSMContext):
    user_dao = UsersDAO(get_session())
    u_data = await state.get_data()
    s_user = u_data.get("users_text")
    u_list = s_user.replace("@", "").split(" ")
    wrong_user = ''
    for i_user in u_list:
        user = await user_dao.find_by_name(i_user)
        if user:
            await bot.send_message(user.id, message.html_text, parse_mode="HTML")
        else:
            wrong_user = " ".join([wrong_user, i_user])
    await message.answer(f"не отправлено: {wrong_user}")
    await state.clear()

