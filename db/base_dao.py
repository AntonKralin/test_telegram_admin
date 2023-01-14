from abc import ABC, abstractmethod
from sqlalchemy.orm import sessionmaker

from other.logger import get_logger


class BaseDAO(ABC):
    """abstract class
        abstractmethod: find_by_id, find_all
    """
    def __init__(self, s_maker: sessionmaker):
        """init class
        args:
            s_maker: sessionmaker
        """
        self.s_maker = s_maker
        self.logger = get_logger()

    async def insert(self, obj):
        """insert object
        args:
            obj
        """
        session = self.s_maker()
        try:
            session.merge(obj)
            session.commit()
        except Exception as e:
            self.logger.error("error insert:" + str(e))
            session.rollback()
        finally:
            self.logger.info("insert:" + str(obj))
            session.close()

    async def update(self, obj):
        """update object
        args:
            obj
        """
        session = self.s_maker()
        try:
            session.merge(obj)
            session.commit()
        except Exception as e:
            self.logger.error("error update:" + str(e))
            session.rollback()
        finally:
            session.close()
            self.logger.info("update")

    @abstractmethod
    async def find_by_id(self, id: int):
        """abstractmethod select * from table where id = id
        args:
            id
        """
        pass

    @abstractmethod
    async def find_all(self):
        """abstractmethod select * from table"""
        pass

    async def dell(self, obj):
        """dell object
        args:
            obj
        """
        session = self.s_maker()
        try:
            session.delete(obj)
            session.commit()
        except Exception as e:
            session.rollback()
            self.logger.error("error delete: " + str(e))
        finally:
            session.close()
            self.logger.info("delete")
