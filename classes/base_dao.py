from abc import ABC, abstractmethod
from sqlalchemy.orm import Session

class BaseDAO(ABC):
    def init(self, session: Session):
        self.session = session

    @abstractmethod
    def insert(self, obj):
        session = self.s_maker()
        try:
            session.add(obj)
            session.commit()
        except Exception:
            session.rollback()
        finally:
            session.close()

    @abstractmethod
    def update(self, obj):
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
        pass

    def find_all(self):
        pass

    @abstractmethod
    def dell(self, obj):
        session = self.s_maker()
        try:
            session.delete(obj)
            session.commit()
        except Exception:
            session.rollback()
        finally:
            session.close()
