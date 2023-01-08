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
