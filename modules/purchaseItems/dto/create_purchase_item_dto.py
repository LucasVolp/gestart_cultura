from dataclasses import dataclass, field

@dataclass
class CreatePurchaseItemDTO:
    purchaseId: str
    tierId: str
    quantity: int
    unitPrice: float
    totalPrice: float

    def isEmpty(self):
        return not any([
            self.purchaseId, self.tierId, self.quantity, self.unitPrice, self.totalPrice
        ])
