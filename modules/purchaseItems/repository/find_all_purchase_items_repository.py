from db import SessionLocal
from models.models import PurchaseItem

class FindAllPurchaseItemsRepository:
    def __init__(self, session=None):
        self.session = session or SessionLocal()

    def findAll(self):
        """
        Returns all purchase items from the database.
        Returns:
            list[PurchaseItem]: List of PurchaseItem model instances.
        """
        return self.session.query(PurchaseItem).all()
