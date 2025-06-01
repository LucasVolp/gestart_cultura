from pydantic import BaseModel, field_validator, model_validator
from typing import Optional
from datetime import date
from models.models import Status

class UpdateTierDTO(BaseModel):
    """Data Transfer Object for updating a tier.

    Attributes:
        amount (Optional[int]): The number of tickets available for this tier.
        name (Optional[str]): The name of the tier.
        price (Optional[float]): The price of the tier.
        startDate (Optional[date]): The start date for the tier's availability.
        endDate (Optional[date]): The end date for the tier's availability.
        status (Optional[Status]): The status of the tier.
        eventId (Optional[str]): The ID of the event this tier belongs to.
    """
    amount: Optional[int] = None
    name: Optional[str] = None
    price: Optional[float] = None
    startDate: Optional[date] = None
    endDate: Optional[date] = None
    status: Optional[Status] = None
    eventId: Optional[str] = None

    @field_validator('name')
    @classmethod
    def validateName(cls, v):
        if v is not None and (not v or not v.strip()):
            raise ValueError('name cannot be empty if provided')
        return v.strip() if v else v

    @field_validator('amount')
    @classmethod
    def validateAmount(cls, v):
        if v is not None and v <= 0:
            raise ValueError('amount must be greater than 0 if provided')
        return v

    @field_validator('price')
    @classmethod
    def validatePrice(cls, v):
        if v is not None and v < 0:
            raise ValueError('price must be greater than or equal to 0 if provided')
        return v

    @field_validator('eventId')
    @classmethod
    def validateEventId(cls, v):
        if v is not None and (not v or not v.strip()):
            raise ValueError('eventId cannot be empty if provided')
        return v.strip() if v else v

    @model_validator(mode='after')
    def validateDates(self):
        if self.startDate is not None and self.endDate is not None:
            if self.endDate <= self.startDate:
                raise ValueError('endDate must be after startDate if both are provided')
        return self

    def isEmpty(self) -> bool:
        """Check if all fields are None or empty."""
        return all(value is None for value in self.model_dump().values())
