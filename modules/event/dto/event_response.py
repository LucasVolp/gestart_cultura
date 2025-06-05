from uuid import UUID
from pydantic import BaseModel
from datetime import date as Date, datetime
from models.models import TypeEvent, Status
from modules.user.dto import ProducerResponse
from modules.tier.dto import TierResponse
from modules.rating.dto import RatingResponse

class EventResponse(BaseModel):
    """Data Transfer Object for user response.

    Attributes:
        id (str): The unique identifier of the user.
        name (str): The name of the user.
        email (str): The email of the user.
        role (str): The role of the user.
    """
    id: UUID
    name: str
    description: str
    local: str
    size: int
    date: Date
    typeEvent: TypeEvent
    status: Status
    producers: list[ProducerResponse] = []
    tiers: list[TierResponse] = []
    ratings: list[RatingResponse] = []
    createdAt: datetime
    updatedAt: datetime

    class Config:
        from_attributes = True