from db import SessionLocal
from models.models import Tier

class FindTierByNameRepository:
    def __init__(self, session=None):
        self.session = session or SessionLocal()

    def findByName(self, name: str) -> Tier:
        """Finds a tier by its name in the database.

        Args:
            name (str): Name of the tier to be found.

        Returns:
            Tier: Tier model instance or None if not found.
        """
        return self.session.query(Tier).filter(Tier.name == name).first()