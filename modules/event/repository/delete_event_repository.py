from db import SessionLocal
from models.models import Event, Status

class DeleteEventRepository:
    def __init__(self, session=None):
        self.session = session or SessionLocal()

    def delete(self, id):
        """
        Deletes an existing id from the database.

        Args:
            id (_type_): id model instance to be deleted.

        Returns:
            _type_: True if deletion was successful, False otherwise.
        """
        try:
            event = self.session.query(Event).filter(Event.id == id).first()
            if event:
                self.session.delete(event)
                self.session.commit()
                return True
            return False
        except Exception as e:
            self.session.rollback()
            return False
        
    def softDelete(self, id):
        """
        Soft deletes an existing id by setting the 'is_deleted' flag to True.

        Args:
            id (_type_): id model instance to be soft deleted.

        Returns:
            _type_: True if soft deletion was successful, False otherwise.
        """
        try:
            event = self.session.query(Event).filter(Event.id == id).first()
            event.status = Status.DELETED
            self.session.add(event)
            self.session.commit()
            return True
        except Exception as e:
            self.session.rollback()
            print(f"Error during soft delete: {e}")
            return False