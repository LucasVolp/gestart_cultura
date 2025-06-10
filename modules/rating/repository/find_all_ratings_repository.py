from db import SessionLocal
from models.models import Rating

class FindAllRatingsRepository:
    def __init__(self, session=None):
        self.session = session or SessionLocal()

    def findAll(self):
        """
        Returns all ratings from the database.

        Returns:
            list[Rating]: List of Rating model instances.
        """
        return self.session.query(Rating).all()
