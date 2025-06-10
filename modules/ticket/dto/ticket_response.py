from datetime import datetime
from uuid import UUID
from pydantic import BaseModel

from models.models import Status


class TicketResponse(BaseModel):
    """Data Transfer Object for ticket response.

    Attributes:
        id (str): The unique identifier of the ticket.
        userId (str): The ID of the user who owns the ticket.
        eventId (str): The ID of the event associated with the ticket.
        tierId (str): The ID of the tier associated with the ticket.
        purchaseId (str): The ID of the purchase associated with the ticket.
        status (str): The status of the ticket.
    """
    id: UUID
    ownerId: UUID
    tierId: UUID
    sellerId: UUID
    status: Status
    code: str
    createdAt: datetime
    updatedAt: datetime