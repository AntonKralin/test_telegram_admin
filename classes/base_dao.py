from abc import ABC, abstractmethod
from sqlalchemy.orm import sessionmaker

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

    def insert(self, obj):
        """insert object
        args:
            obj
        """
        print('start insert')
        session = self.s_maker()
        try:
            session.add(obj)
            session.commit()
            print('data add')
        except Exception as e:
            print(str(e))
            session.rollback()
        finally:
            session.close()

    def update(self, obj):
        """update object
        args:
            obj
        """
        session = self.s_maker()
        try:
            session.add(obj)
            session.commit()
        except Exception:
            session.rollback()
        finally:
            session.close()

    @abstractmethod
    def find_by_id(self, id):
        """abstractmethod select * from table where id = id
        args:
            id
        """
        pass

    @abstractmethod
    def find_all(self):
        """abstractmethod select * from table"""
        pass

    def dell(self, obj):
        """dell object
        args:
            obj
        """
        session = self.s_maker()
        try:
            session.delete(obj)
            session.commit()
        except Exception:
            session.rollback()
        finally:
            session.close()
