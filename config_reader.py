from dotenv import dotenv_values

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

try:
    config = dotenv_values(".env")
    if not config.get("BOT_TOKEN"):
        raise ValueNoException("BOT_TOKEN")
    if not config.get("SuperAdmin"):
        raise ValueNoException("SuperAdmin")
    if not config.get("DB_NAME"):
        config["DB_NAME"] = "sqllite.db"
except ValueNoException as exc:
    print(exc)
else:
    print ("Config load")
