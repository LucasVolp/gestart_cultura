from db import SessionLocal
from models.models import Event

class FindEventByIdRepository:
    def __init__(self, session=None):
        self.session = session or SessionLocal()

    def findById(self, id):
        """
        Returns an event by its ID from the database.
        This

        Args:
            id (_type_): ID of the event to be retrieved.

        Returns:
            _type_: Event model instance if found, otherwise None.
        """
        return self.session.query(Event).filter(Event.id == id).first()
