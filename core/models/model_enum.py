from enum import Enum

class StatusTask(Enum):
    ACTIVE = 'ACTIVE'
    NONACTIVE = 'NONACTIVE'

class StatusPay(Enum):
    OK = 'OK'
    NOTOK = 'NOTOK'
    WAIT = 'WAIT'

class RoleUser(Enum):
    SUPER_ADMIN = 'SUPER_ADMIN'
    ADMIN = 'ADMIN'
    CLIENT = 'CLIENT'