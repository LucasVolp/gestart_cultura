from pydantic import BaseModel, field_validator
from typing import Optional

class UpdateRatingDTO(BaseModel):
    """Data Transfer Object for updating a rating.
    
    Attributes:
        rate (Optional[int]): The rating value (1-5).
        comment (Optional[str]): Optional comment about the rating.
    """
    rate: Optional[int] = None
    comment: Optional[str] = None

    @field_validator('rate')
    @classmethod
    def validateRate(cls, value):
        if value is not None and (value < 1 or value > 5):
            raise ValueError('rate must be between 1 and 5 if provided')
        return value

    @field_validator('comment')
    @classmethod
    def validateComment(cls, value):
        if value is not None and not value.strip():
            raise ValueError('comment cannot be empty if provided')
        return value.strip() if value else value

    def isEmpty(self) -> bool:
        """Check if all fields are None or empty."""
        return all(value is None for value in self.model_dump().values())
