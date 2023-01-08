from aiogram.filters import Filter
from aiogram.types import Message

from classes.models import Users

class SuperAdminFilter(Filter):
    async def __call__(self, message: Message) -> bool:
        pass

class AdminFilter(Filter):
    async def __call__(self, message: Message) -> bool:
        pass
