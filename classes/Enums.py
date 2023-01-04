import enum

class UserType(enum.Enum):
    admin = 'admin'
    superadmin = 'superadmin'
    user = 'user'
    block = 'block'