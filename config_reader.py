from dotenv import dotenv_values
import logging

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


def get_logger() -> logging:
    logger = logging.getLogger(__name__)
    f_handler = logging.FileHandler('file.log')
    #f_handler.setLevel(int(config.get("LOG_LEVEL")))
    f_format = logging.Formatter('%(asctime)s: %(name)s: %(levelname)s: %(message)s')
    f_handler.setFormatter(f_format)
    logger.addHandler(f_handler)
    logger.setLevel(int(config.get("LOG_LEVEL")))
    return logger

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
    print("Config load")
    logger = get_logger()
    logger.info("Config load")
