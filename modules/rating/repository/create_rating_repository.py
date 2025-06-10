from dataclasses import asdict
from db import SessionLocal
from models.models import Rating
from modules.rating import CreateRatingDTO
from sqlalchemy.exc import IntegrityError

class CreateRatingRepository:
    def __init__(self, session=None):
        self.session = session or SessionLocal()

    def create(self, data: CreateRatingDTO):
        """
        Creates a new rating in the database.

        Args:
            data (CreateRatingDTO): Data of the rating to be created.
        Returns:
            Rating: Created Rating model instance.
        Raises:
            ValueError: If an integrity error occurs while creating the rating.
        """
        try:
            data = data.model_dump()
            rating = Rating(**data)
            self.session.add(rating)
            self.session.commit()
            self.session.refresh(rating)
            return rating
        except IntegrityError as e:
            self.session.rollback()
            raise ValueError("Integrity error while creating rating.") from e
