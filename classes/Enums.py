import enum

class UserType(enum.Enum):
    """enum with admin, superadmin, user, block"""
    admin = 'admin'
    superadmin = 'superadmin'
    user = 'user'
    block = 'block'