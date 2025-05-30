from db import SessionLocal
from models.models import Rating

class FindRatingByIdRepository:
    def __init__(self, session=None):
        self.session = session or SessionLocal()

    def findById(self, id: str):
        """
        Finds a rating by ID in the database.

        Args:
            id (str): Rating ID to be found.
        Returns:
            Rating | None: Rating model instance or None if not found.
        """
        return self.session.query(Rating).filter(Rating.id == id).first()
