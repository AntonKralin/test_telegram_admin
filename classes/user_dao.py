from sqlalchemy import select

from classes.models import Users
from classes.base_dao import BaseDAO


class UsersDAO(BaseDAO):

    def find_by_id(self, id):
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

    def find_all(self):
        """abstractmethod select * from table"""
        session = self.s_maker()
        stmt = select(Users)
        for user in session.scalars(stmt):
            return user

    def find_by_type(self, type_user: str) -> list:
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

    def check_type(self, user_id: int, user_type: str) -> bool:
        """check user type
        arg:
            id: int id user
        return:
            bool"""
        session = self.s_maker
        l_user = self.find_by_type(user_type)
        for i_user in l_user:
            if i_user.id == user_id:
                return True
        return False
