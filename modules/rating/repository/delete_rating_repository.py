from db import SessionLocal
from models.models import Rating
from sqlalchemy.exc import IntegrityError

class DeleteRatingRepository:
    def __init__(self, session=None):
        self.session = session or SessionLocal()

    def delete(self, id):
        """
        Deletes a rating from the database by ID.

        Args:
            id (int): ID of the rating to be deleted.
        Returns:
            bool: True if the rating was deleted successfully, False otherwise.
        """
        try:
            rating = self.session.query(Rating).filter(Rating.id == id).first()
            if not rating:
                return False
            self.session.delete(rating)
            self.session.commit()
            return True
        except Exception:
            self.session.rollback()
            return False
