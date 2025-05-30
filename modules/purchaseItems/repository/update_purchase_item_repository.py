from dataclasses import asdict
from db import SessionLocal
from modules.purchaseItems import UpdatePurchaseItemDTO

class UpdatePurchaseItemRepository:
    def __init__(self, session=None):
        self.session = session or SessionLocal()

    def update(self, purchaseItems, data: UpdatePurchaseItemDTO):
        """
        Updates an existing purchase item in the database.
        Args:
            purchaseItems (PurchaseItem): PurchaseItem model instance to be updated.
            data (UpdatePurchaseItemDTO): Data Transfer Object containing the updated purchase item information.
        Returns:
            PurchaseItem: Updated PurchaseItem instance.
        """
        data = asdict(data)
        for key, value in data.items():
            if value is not None:
                setattr(purchaseItems, key, value)
        self.session.commit()
        self.session.refresh(purchaseItems)
        return purchaseItems
