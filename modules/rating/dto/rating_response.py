from uuid import UUID
from pydantic import BaseModel


class RatingResponse(BaseModel):
    """Data Transfer Object for rating response.

    Attributes:
        id (str): The unique identifier of the rating.
        userId (str): The unique identifier of the user who made the rating.
        eventId (str): The unique identifier of the event being rated.
        score (int): The score given by the user.
        comment (str): The comment provided by the user.
    """
    id: UUID
    userId: str
    eventId: str
    rate: int
    comment: str

    class Config:
        from_attributes = True