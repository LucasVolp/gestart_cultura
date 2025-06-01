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
    def validateUserId(cls, v):
        if not v or not v.strip():
            raise ValueError('userId cannot be empty')
        return v.strip()

    @field_validator('eventId')
    @classmethod
    def validateEventId(cls, v):
        if not v or not v.strip():
            raise ValueError('eventId cannot be empty')
        return v.strip()

    @field_validator('rate')
    @classmethod
    def validateRate(cls, v):
        if v < 1 or v > 5:
            raise ValueError('rate must be between 1 and 5')
        return v

    @field_validator('comment')
    @classmethod
    def validateComment(cls, v):
        if v is not None and not v.strip():
            raise ValueError('comment cannot be empty if provided')
        return v.strip() if v else v
