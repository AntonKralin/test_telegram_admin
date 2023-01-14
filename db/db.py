from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from other.configs import config
from db.models import Base


engine = create_engine("sqlite:///" + config.get("DB_NAME"))
Base.metadata.create_all(engine)

def get_session() -> Session:
    """get bd session"""
    return sessionmaker(bind=engine)
