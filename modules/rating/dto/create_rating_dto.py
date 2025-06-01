from pydantic import BaseModel, field_validator
from typing import Optional

class CreateRatingDTO(BaseModel):
    """Data Transfer Object for creating a rating.
    
    Attributes:
        userId (str): The ID of the user who is rating.
        eventId (str): The ID of the event being rated.
        rate (int): The rating value (1-5).
        comment (Optional[str]): Optional comment about the rating.
    """
    userId: str
    eventId: str
    rate: int
    comment: Optional[str] = None

    @field_validator('userId')
    @classmethod
    def validateUserId(cls, value):
        if not value or not value.strip():
            raise ValueError('userId cannot be empty')
        return value.strip()

    @field_validator('eventId')
    @classmethod
    def validateEventId(cls, value):
        if not value or not value.strip():
            raise ValueError('eventId cannot be empty')
        return value.strip()

    @field_validator('rate')
    @classmethod
    def validateRate(cls, value):
        if value < 1 or value > 5:
            raise ValueError('rate must be between 1 and 5')
        return value

    @field_validator('comment')
    @classmethod
    def validateComment(cls, value):
        if value is not None and not value.strip():
            raise ValueError('comment cannot be empty if provided')
        return value.strip() if value else value
