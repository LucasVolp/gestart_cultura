from db import SessionLocal
from models.models import Event
from sqlalchemy.orm import joinedload

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
        return (
            self.session.query(Event).filter(Event.id == id)
            .options(
                joinedload(Event.tiers),
                joinedload(Event.ratings),
                joinedload(Event.producers),
        ).first()
        )
