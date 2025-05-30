from db import SessionLocal
from models.models import Event

class DeleteEventRepository:
    def __init__(self, session=None):
        self.session = session or SessionLocal()

    def delete(self, event):
        """
        Deletes an existing event from the database.

        Args:
            event (_type_): Event model instance to be deleted.

        Returns:
            _type_: True if deletion was successful, False otherwise.
        """
        try:
            self.session.delete(event)
            self.session.commit()
            return True
        except Exception as e:
            self.session.rollback()
            return False