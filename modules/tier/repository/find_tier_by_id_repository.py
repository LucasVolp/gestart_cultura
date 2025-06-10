from db import SessionLocal
from models.models import Tier

class FindTierByIdRepository:
    def __init__(self, session=None):
        self.session = session or SessionLocal()

    def findById(self, id: str):
        """Find a tier by its ID.

        Args:
            id (str): Tier ID to be found.

        Returns:
            Tier | None: Tier model instance or None if not found.
        """
        return self.session.query(Tier).filter(Tier.id == id).first()
