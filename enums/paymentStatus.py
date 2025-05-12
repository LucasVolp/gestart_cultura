from enum import Enum


class PaymentStatus(Enum):
    PAID = "PAID"
    PENDING = "PENDING"
    FAILED = "FAILED"
    REFUNDED = "REFUNDED"
    CANCELLED = "CANCELLED"