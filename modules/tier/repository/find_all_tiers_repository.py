from db import SessionLocal
from models.models import Tier

class FindAllTiersRepository:
    def __init__(self, session=None):
        self.session = session or SessionLocal()

    def findAll(self):
        """
        Returns all tiers from the database.

        Returns:
            list[Tier]: List of Tier model instances.
        """
        return self.session.query(Tier).all()
