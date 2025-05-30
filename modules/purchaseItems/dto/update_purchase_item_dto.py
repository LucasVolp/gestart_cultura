from typing import Optional
from dataclasses import dataclass


@dataclass
class UpdatePurchaseItemDTO:
    purchaseId: Optional[str] = None
    tierId: Optional[str] = None
    quantity: Optional[int] = None
    unitPrice: Optional[float] = None
    totalPrice: Optional[float] = None

    def isEmpty(self):
        return not any([
            self.purchaseId, self.tierId, self.quantity, self.unitPrice, self.totalPrice
        ])
