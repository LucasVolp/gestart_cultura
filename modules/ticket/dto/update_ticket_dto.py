from pydantic import BaseModel, field_validator
from typing import Optional
from models.models import Status

class UpdateTicketDTO(BaseModel):
    """Data Transfer Object for updating a ticket.

    Attributes:
        ownerId (Optional[str]): The ID of the ticket owner (user).
        tierId (Optional[str]): The ID of the tier this ticket belongs to.
        sellerId (Optional[str]): The ID of the seller who sold this ticket.
        status (Optional[Status]): The status of the ticket.
    """
    ownerId: Optional[str] = None
    tierId: Optional[str] = None
    sellerId: Optional[str] = None
    status: Optional[Status] = None

    @field_validator('ownerId')
    @classmethod
    def validateOwnerId(cls, value):
        if value is not None and (not value or not value.strip()):
            raise ValueError('ownerId cannot be empty if provided')
        return value.strip() if value else value

    @field_validator('tierId')
    @classmethod
    def validateTierId(cls, value):
        if value is not None and (not value or not value.strip()):
            raise ValueError('tierId cannot be empty if provided')
        return value.strip() if value else value

    @field_validator('sellerId')
    @classmethod
    def validateSellerId(cls, value):
        if value is not None and (not value or not value.strip()):
            raise ValueError('sellerId cannot be empty if provided')
        return value.strip() if value else value

    def isEmpty(self) -> bool:
        """Check if all fields are None or empty."""
        return all(value is None for value in self.model_dump().values())

