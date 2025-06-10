from datetime import datetime
from typing import List
from uuid import UUID
from pydantic import BaseModel
from models.models import PaymentMethod, PaymentStatus


class PurchaseItemResponse(BaseModel):
    """Data Transfer Object for purchase items response.

    Attributes:
        id (str): The unique identifier of the purchase item.
        purchaseId (str): The ID of the purchase associated with the item.
        eventId (str): The ID of the event associated with the item.
        tierId (str): The ID of the tier associated with the item.
        quantity (int): The quantity of the item purchased.
        price (float): The price of the item.
    """
    id: UUID
    purchaseId: UUID
    tierId: UUID
    quantity: int
    unitPrice: float
    totalPrice: float
    createdAt: datetime
    updatedAt: datetime

    class Config:
        from_attributes = True

class PurchaseResponse(BaseModel):
    """Data Transfer Object for purchase response.

    Attributes:
        id (str): The unique identifier of the purchase.
        userId (str): The ID of the user who made the purchase.
        eventId (str): The ID of the event associated with the purchase.
        totalPrice (float): The total price of the purchase.
        status (str): The status of the purchase.
    """
    id: UUID
    buyerId: UUID
    sellerId: UUID
    purchaseDate: datetime
    status: PaymentStatus
    totalPrice: float
    paymentMethod: PaymentMethod
    createdAt: datetime
    updatedAt: datetime
    items: List[PurchaseItemResponse] = []

    class Config:
        from_attributes = True
