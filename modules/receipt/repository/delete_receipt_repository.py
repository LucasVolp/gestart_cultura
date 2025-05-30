from db import SessionLocal

class DeleteReceiptRepository:
    def __init__(self, session=None):
        self.session = session or SessionLocal()

    def delete(self, receipt):
        """
        Deletes a receipt from the database.

        Args:
            receipt: Receipt model instance to be deleted.
        """
        try:
            self.session.delete(receipt)
            self.session.commit()
            return True
        except Exception as e:
            self.session.rollback()
            return False
