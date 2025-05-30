from models import Seller
from db import SessionLocal

class DeleteSellerRepository:
    def __init__(self, session=None):
        self.session = session or SessionLocal()

    def delete(self, seller):
        """
        Deletes a seller from the database.

        Args:
            seller (Seller): Seller model instance to be deleted.
        Returns:
            bool: True if the seller was deleted successfully, False otherwise.
        """
        try:
            self.session.delete(seller)
            self.session.commit()
            return True
        except Exception:
            self.session.rollback()
            return False
