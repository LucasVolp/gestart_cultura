from pydantic import BaseModel, field_validator
from typing import Optional
from models.models import Status

class CreateTicketDTO(BaseModel):
    """Data Transfer Object for creating a ticket.
    Attributes:
        ownerId (str): The ID of the ticket owner (user).
        tierId (str): The ID of the tier this ticket belongs to.
        sellerId (str): The ID of the seller who sold this ticket.
        status (Optional[Status]): The status of the ticket, default is None.
    """
    ownerId: str
    tierId: str
    sellerId: str
    status: Optional[Status] = None

    @field_validator('ownerId')
    @classmethod
    def validateOwnerId(cls, v):
        if not v or not v.strip():
            raise ValueError('ownerId cannot be empty')
        return v.strip()

    @field_validator('tierId')
    @classmethod
    def validateTierId(cls, v):
        if not v or not v.strip():
            raise ValueError('tierId cannot be empty')
        return v.strip()

    @field_validator('sellerId')
    @classmethod
    def validateSellerId(cls, v):
        if not v or not v.strip():
            raise ValueError('sellerId cannot be empty')
        return v.strip()

