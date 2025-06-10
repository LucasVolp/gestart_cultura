from pydantic import BaseModel, field_validator, model_validator
from typing import Optional
from datetime import date
from models.models import Status

class CreateTierDTO(BaseModel):
    """Data Transfer Object for creating a tier.
    Attributes:
        amount (int): The number of tickets available for this tier.
        name (str): The name of the tier.
        price (float): The price of the tier.
        startDate (date): The start date for the tier's availability.
        endDate (date): The end date for the tier's availability.
        status (Optional[Status]): The status of the tier, default is None.
        eventId (str): The ID of the event this tier belongs to.
    """
    amount: int
    name: str
    price: float
    startDate: date
    endDate: date
    status: Optional[Status] = None
    eventId: str

    @field_validator('name')
    @classmethod
    def validateName(cls, value):
        if not value or not value.strip():
            raise ValueError('name cannot be empty')
        return value.strip()

    @field_validator('amount')
    @classmethod
    def validateAmount(cls, value):
        if value <= 0:
            raise ValueError('amount must be greater than 0')
        return value

    @field_validator('price')
    @classmethod
    def validatePrice(cls, value):
        if value < 0:
            raise ValueError('price must be greater than or equal to 0')
        return value

    @field_validator('eventId')
    @classmethod
    def validateEventId(cls, value):
        if not value or not value.strip():
            raise ValueError('eventId cannot be empty')
        return value.strip()

    @model_validator(mode='after')
    def validateDates(self):
        if self.endDate <= self.startDate:
            raise ValueError('endDate must be after startDate')
        return self
