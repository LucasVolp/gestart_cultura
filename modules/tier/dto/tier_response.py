from uuid import UUID
from pydantic import BaseModel
from datetime import date as Date, datetime
from models.models import Status

class TierResponse(BaseModel):
    """Data Transfer Object for tier response.

    Attributes:
        id (str): The unique identifier of the tier.
        name (str): The name of the tier.
        description (str): The description of the tier.
        price (float): The price of the tier.
    """
    id: UUID
    amount: int
    name: str
    price: float
    startDate: Date
    endDate: Date
    status: Status
    eventId: UUID
    createdAt: datetime
    updatedAt: datetime

    class Config:
        from_attributes = True