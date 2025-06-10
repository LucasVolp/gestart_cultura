from db import SessionLocal
from models.models import Tier

class FindTiersByEventRepository:
    def __init__(self, session=None):
        self.session = session or SessionLocal()

    def findByEventId(self, eventId: str):
        """
        Returns all tiers for a specific event.

        Args:
            eventId (str): The ID of the event.

        Returns:
            list[Tier]: List of Tier model instances for the event.
        """
        tiers = self.session.query(Tier).filter(Tier.eventId == eventId).all()
        return tiers
