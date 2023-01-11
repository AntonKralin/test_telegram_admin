from dotenv import dotenv_values
import logging

from other.logger import get_logger
class ValueNoException(Exception):
    """exception class"""
    def __init__(self, *args: object) -> None:
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self) -> str:
        if self.message:
            return f"ValueNoException: {self.message}"
        else:
            return "ValueNoException"


def get_config():
    """return result of read .env file"""
    try:
        config = dotenv_values(".env")
        if not config.get("BOT_TOKEN"):
            raise ValueNoException("BOT_TOKEN")
        if not config.get("SUPER_ADMIN"):
            raise ValueNoException("SUPER_ADMIN")
        if not config.get("DB_NAME"):
            config["DB_NAME"] = "sqllite.db"
        if not config.get("LOG_LEVEL"):
            config["LOG_LEVEL"] = logging.ERROR
    except ValueNoException as exc:
        logger = get_logger()
        logger.error(str(exc))
    else:
        logger = get_logger()
        logger.info("Config load")
        return config
