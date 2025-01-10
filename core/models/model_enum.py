from enum import Enum


class StatusPay(Enum):
    OK = 'OK'
    NOTOK = 'NOTOK'
    WAIT = 'WAIT'


class RoleUserService(Enum):
    SUPER_ADMIN = 'SUPER_ADMIN'
    ADMIN = 'ADMIN'
    BOT = 'BOT'
