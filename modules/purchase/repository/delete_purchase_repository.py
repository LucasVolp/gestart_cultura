from db import SessionLocal
from models.models import Purchase

class DeletePurchaseRepository:
    def __init__(self, session=None):
        self.session = session or SessionLocal()

    def delete(self, id):
        """
        Deletes a purchase from the database by ID.

        Args:
            id (str): Purchase ID to be deleted.
        Returns:
            bool: True if the purchase was deleted successfully, False otherwise.
        """
        try:
            purchase = self.session.query(Purchase).filter(Purchase.id == id).first()
            if not purchase:
                return False
            self.session.delete(purchase)
            self.session.commit()
            return True
        except Exception:
            self.session.rollback()
            return False
