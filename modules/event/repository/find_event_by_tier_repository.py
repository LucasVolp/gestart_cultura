from db import SessionLocal
from models.models import Event
from sqlalchemy.orm import joinedload

class FindEventByTierRepository:
    def __init__(self, session=None):
        self.session = session or SessionLocal()

    def findByTier(self, tierId: str):
        """
        Retrieves an event by its tier ID from the database.

        Args:
            tierId (str): ID of the tier to be used for finding the event.

        Returns:
            Event | None: Event model instance if found, None otherwise.
        """
        return (
            self.session.query(Event)
            .filter(Event.tiers.any(id=tierId))
            .options(
                joinedload(Event.tiers),
                joinedload(Event.ratings),
                joinedload(Event.producers),
            )
            .first()
        )