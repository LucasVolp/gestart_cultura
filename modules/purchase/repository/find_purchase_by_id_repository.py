from db import SessionLocal
from models.models import Purchase

class FindPurchaseByIdRepository:
    def __init__(self, session=None):
        self.session = session or SessionLocal()

    def findById(self, id: str):
        """
        Finds a purchase by ID in the database.

        Args:
            id (str): Purchase ID to be found.
        Returns:
            Purchase | None: Purchase model instance or None if not found.
        """
        return self.session.query(Purchase).filter(Purchase.id == id).first()
