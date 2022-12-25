from aiogram.filters import Filter
from aiogram.types import Message

from classes.models import SuperAdmin, Admin

class SuperAdminFilter(Filter):
    async def __call__(self, message: Message) -> bool:
        id_user = message.from_user.id
        if SuperAdmin().get(SuperAdmin.id == id_user):
            return True
        return False

class AdminFilter(Filter):
    async def __call__(self, message: Message) -> bool:
        id_user = message.from_user.id
        if Admin().get(Admin.id == id_user):
            return True
        return False
