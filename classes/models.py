from config_reader import config
from peewee import *

class BaseModel(Model):
    class Meta:
        database = SqliteDatabase(config.get("DB_NAME"))

class SuperAdmin(BaseModel):
    """SQL table that contains SuperAdmin user for telegram

    Args:
        id: int id user
        name: str admin name
    """
    id = PrimaryKeyField(null=False)
    name = CharField()

class Admin(BaseModel):
    """SQL table that contains admin user for telegram

    Args:
        id: int id user
        name: str admin name
    """
    id = PrimaryKeyField(null=False)
    name = CharField()

class BlockUser(BaseModel):
    """SQL table that contains user than block in telegram

    Args:
        id: int id user
        name: str admin name
    """
    id = PrimaryKeyField(null=False)
    name = CharField()
