from sqlalchemy import select

from db.models import Users
from db.base_dao import BaseDAO


class UsersDAO(BaseDAO):

    async def find_by_id(self, id: int):
        """select * from table where id = id
        args:
            id
        return:
            Users
        """
        session = self.s_maker()
        stmt = select(Users).where(Users.id == id)
        for user in session.scalars(stmt):
            return user

    async def find_all(self):
        """abstractmethod select * from table"""
        session = self.s_maker()
        stmt = select(Users)
        for user in session.scalars(stmt):
            return user

    async def find_by_type(self, type_user: str) -> list:
        """select * from table where 'type'=type
        arg:
            type_user: str type of user UserType
        return:
            list of Users"""
        session = self.s_maker()
        stmt = select(Users).where(Users.type == type_user)
        l_user = list()
        for user in session.scalars(stmt):
            l_user.append(user)
        return l_user

    async def find_by_name(self, name: str) -> Users:
        """select * from table where `name`=name
        arg:
            name: username tg user
        return:
            User: class user"""
        session = self.s_maker()
        stmt = select(Users).filter(Users.name.ilike(name))
        l_user = list()
        for i_user in session.scalars(stmt):
            l_user.append(i_user)
        if len(l_user) == 0:
            return None
        else:
            return l_user[0]

    async def check_type(self, user_id: int, user_type: str) -> bool:
        """check user type
        arg:
            id: int id user
        return:
            bool"""
        l_user = await self.find_by_type(user_type)
        for i_user in l_user:
            if i_user.id == user_id:
                return True
        return False
