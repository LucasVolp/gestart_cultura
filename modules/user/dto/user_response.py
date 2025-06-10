from typing import Optional
from uuid import UUID
from pydantic import BaseModel
from datetime import datetime, date as Date
from models.models import Role, Status, TypeEvent
from modules.purchase.dto.purchase_response import PurchaseResponse
from modules.receipt.dto.receipt_response import ReceiptResponse
from modules.ticket.dto.ticket_response import TicketResponse
from modules.tier.dto.tier_response import TierResponse
from modules.rating.dto.rating_response import RatingResponse

class EventOut(BaseModel):
    """Data Transfer Object for user response.

    Attributes:
        id (UUID): The unique identifier of the user.
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
    producers: list['ProducerResponse'] = []
    tiers: list[TierResponse] = []
    ratings: list[RatingResponse] = []


    class Config:
        from_attributes = True


class UserResponse(BaseModel):
    """Data Transfer Object for user response.

    Attributes:
        id (UUID): The unique identifier of the user.
        name (str): The name of the user.
        email (str): The email of the user.
        role (str): The role of the user.
        events (list[EventOut]): List of events associated with the user.
    """
    id: UUID
    name: str
    cpf: str
    birth: Date
    email: str
    password: str
    phone: str
    status: Status
    role: Role
    balance: float
    cnpj: Optional[str]
    enterprise: Optional[str]
    createdAt: datetime
    updatedAt: datetime
    events: list[EventOut] = []
    sales: list[PurchaseResponse] = []
    tickets: list[TicketResponse] = []
    ratings: list[RatingResponse] = []
    purchases: list[PurchaseResponse] = []
    receipts: list[ReceiptResponse] = []

    class Config:
        from_attributes = True

class ProducerResponse(BaseModel):
    """Data Transfer Object for producer response.

    Attributes:
        id (UUID): The unique identifier of the producer.
        name (str): The name of the producer.
        cnpj (str): The CNPJ of the producer.
        enterprise (str): The enterprise name of the producer.
    """
    id: UUID
    name: str
    role: Role
    cnpj: Optional[str]
    enterprise: Optional[str]

    class Config:
        from_attributes = True