from dataclasses import asdict
from db import SessionLocal
from models.models import Rating
from modules.rating import UpdateRatingDTO

class UpdateRatingRepository:
    def __init__(self, session=None):
        self.session = session or SessionLocal()

    def update(self, rating, data: UpdateRatingDTO):
        """
        Updates an existing rating in the database.

        Args:
            rating (Rating): Rating model instance to be updated.
            data (UpdateRatingDTO): Data Transfer Object containing the updated rating information.
        Returns:
            Rating: Updated Rating instance.
        """
        data = asdict(data)
        for key, value in data.items():
            if value is not None:
                setattr(rating, key, value)
        self.session.commit()
        self.session.refresh(rating)
        return rating
