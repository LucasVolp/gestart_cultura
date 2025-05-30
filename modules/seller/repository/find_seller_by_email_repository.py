from models import Seller
from db import SessionLocal

class FindSellerByEmailRepository:
    def __init__(self, session=None):
        self.session = session or SessionLocal()

    def findByEmail(self, email: str):
        """
        Finds a seller by email in the database.

        Args:
            email (str): Seller email to be found.
        Returns:
            Seller | None: Seller model instance or None if not found.
        """
        return self.session.query(Seller).filter(Seller.email == email).first()
