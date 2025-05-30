from dataclasses import dataclass
from typing import Optional
from enums import PaymentStatus, PaymentMethods

@dataclass
class CreatePurchaseDTO:
    buyerId: str
    sellerId: str
    purchaseDate: str
    status: Optional[PaymentStatus] = None
    totalPrice: float = 0.0
    paymentMethod: PaymentMethods
