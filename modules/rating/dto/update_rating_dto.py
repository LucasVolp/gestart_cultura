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
    def validateRate(cls, v):
        if v is not None and (v < 1 or v > 5):
            raise ValueError('rate must be between 1 and 5 if provided')
        return v

    @field_validator('comment')
    @classmethod
    def validateComment(cls, v):
        if v is not None and not v.strip():
            raise ValueError('comment cannot be empty if provided')
        return v.strip() if v else v

    def isEmpty(self) -> bool:
        """Check if all fields are None or empty."""
        return all(value is None for value in self.model_dump().values())
