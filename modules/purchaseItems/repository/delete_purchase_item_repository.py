from db import SessionLocal

class DeletePurchaseItemRepository:
    def __init__(self, session=None):
        self.session = session or SessionLocal()

    def delete(self, purchaseItem):
        """
        Deletes a purchase item from the database.
        Args:
            purchaseItem (PurchaseItem): PurchaseItem model instance to be deleted.
        Returns:
            bool: True if the purchase item was deleted successfully, False otherwise.
        """
        try:
            if purchaseItem not in self.session:
                self.session.merge(purchaseItem)
            self.session.delete(purchaseItem)
            self.session.commit()
            return True
        except Exception:
            self.session.rollback()
            return False
