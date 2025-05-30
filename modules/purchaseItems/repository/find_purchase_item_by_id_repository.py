from db import SessionLocal
from models.models import PurchaseItem

class FindPurchaseItemByIdRepository:
    def __init__(self, session=None):
        self.session = session or SessionLocal()

    def findById(self, id: str):
        """
        Finds a purchase item by ID in the database.
        Args:
            id (str): PurchaseItem ID to be found.
        Returns:
            PurchaseItem | None: PurchaseItem model instance or None if not found.
        """
        return self.session.query(PurchaseItem).filter(PurchaseItem.id == id).first()
