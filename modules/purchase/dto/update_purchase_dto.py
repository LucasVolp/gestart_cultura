from dataclasses import dataclass
from typing import Optional
from models.models import PaymentStatus, PaymentMethod

@dataclass
class UpdatePurchaseDTO:
    buyerId: Optional[str] = None
    sellerId: Optional[str] = None
    purchaseDate: Optional[str] = None
    status: Optional[PaymentStatus] = None
    totalPrice: Optional[float] = None
    paymentMethod: Optional[PaymentMethod] = None

    def isEmpty(self) -> bool:
        return all(value is None for value in self.__dict__.values())
