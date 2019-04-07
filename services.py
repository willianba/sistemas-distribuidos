from enum import Enum


class Service(Enum):
    SIGN_UP = 5000
    QUERY = 5100
    HEARTBEAT = 5200
    RETRIEVE = 5300
    SEND = 5400
