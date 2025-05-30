from db import SessionLocal
from models.models import Receipt

class FindReceiptByIdRepository:
    def __init__(self, session=None):
        self.session = session or SessionLocal()

    def findById(self, id: str):
        """
        Finds a receipt by ID in the database.

        Args:
            id (str): Receipt ID to be found.
        Returns:
            Receipt | None: Receipt model instance or None if not found.
        """
        return self.session.query(Receipt).filter(Receipt.id == id).first()
