# types/status.py
from enum import Enum

class Status(Enum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    DELETED = "DELETED"
    CANCELLED = "CANCELLED"
    OPEN = "OPEN"
    CLOSED = "CLOSED"
