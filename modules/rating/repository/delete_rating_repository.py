from db import SessionLocal
from models.models import Rating
from sqlalchemy.exc import IntegrityError

class DeleteRatingRepository:
    def __init__(self, session=None):
        self.session = session or SessionLocal()

    def delete(self, rating):
        """
        Deletes a rating from the database.

        Args:
            rating (Rating): Rating model instance to be deleted.
        Returns:
            bool: True if the rating was deleted successfully, False otherwise.
        """
        try:
            self.session.delete(rating)
            self.session.commit()
            return True
        except Exception:
            self.session.rollback()
            return False
