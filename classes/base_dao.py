from sqlalchemy.orm import Session

class BaseDAO:
    def init(self, session: Session):
        self.session = session

    def insert(self, obj):
        session = self.s_maker()
        try:
            session.add(obj)
            session.commit()
        except Exception:
            session.rollback()
        finally:
            session.close()

    def update(self, obj):
        session = self.s_maker()
        try:
            session.add(obj)
            session.commit()
        except Exception:
            session.rollback()
        finally:
            session.close()

    def find_by_id(self, id):
        pass

    def find_all(self):
        pass

    def dell(self, obj):
        session = self.s_maker()
        try:
            session.delete(obj)
            session.commit()
        except Exception:
            session.rollback()
        finally:
            session.close()
