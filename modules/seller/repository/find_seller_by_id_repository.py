from models import Seller
from db import SessionLocal

class FindSellerByIdRepository:
    def __init__(self, session=None):
        self.session = session or SessionLocal()

    def findById(self, id: str):
        """
        Finds a seller by ID in the database.

        Args:
            id (int): Seller ID to be found.
        Returns:
            Seller | None: Seller model instance or None if not found.
        """
        return self.session.query(Seller).filter(Seller.id == id).first()
