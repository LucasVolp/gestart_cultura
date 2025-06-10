from db import SessionLocal
from models.models import Receipt

class DeleteReceiptRepository:
    def __init__(self, session=None):
        self.session = session or SessionLocal()

    def delete(self, id):
        """
        Deletes a receipt from the database by ID.

        Args:
            id (str): Receipt ID to be deleted.
        Returns:
            bool: True if the receipt was deleted successfully, False otherwise.
        """
        try:
            receipt = self.session.query(Receipt).filter(Receipt.id == id).first()
            if not receipt:
                return False
            self.session.delete(receipt)
            self.session.commit()
            return True
        except Exception as e:
            self.session.rollback()
            return False
