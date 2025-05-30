from db import SessionLocal

class DeletePurchaseRepository:
    def __init__(self, session=None):
        self.session = session or SessionLocal()

    def delete(self, purchase):
        """
        Deletes a purchase from the database.

        Args:
            purchase (Purchase): Purchase model instance to be deleted.
        Returns:
            bool: True if the purchase was deleted successfully, False otherwise.
        """
        try:
            self.session.delete(purchase)
            self.session.commit()
            return True
        except Exception:
            self.session.rollback()
            return False
