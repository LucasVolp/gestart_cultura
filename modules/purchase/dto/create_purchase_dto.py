from dataclasses import dataclass
from typing import Optional
from models.models import PaymentStatus, PaymentMethod

@dataclass
class CreatePurchaseDTO:
    buyerId: str
    sellerId: str
    purchaseDate: str
    status: Optional[PaymentStatus] = None
    totalPrice: float = 0.0
    paymentMethod: PaymentMethod
