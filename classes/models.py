from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Integer, String
from sqlalchemy.orm import mapped_column

class Base(DeclarativeBase):
    pass

class Users(Base):
    """SQL table that contains users for telegram

    Args:
        id: int id user
        name: str admin name
        type: str type of user (admin, superadmin, user, block)
    """
    __tablename__ = "users"

    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String, nullable=True)
    type = mapped_column(String(11), nullable=False)

    def __repr__(self) -> str:
        return f"{self.id}: {self.type}, {self.name}"
