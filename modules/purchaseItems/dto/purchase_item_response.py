from uuid import UUID
from pydantic import BaseModel


class PurchaseItemsResponse(BaseModel):
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
    eventId: UUID
    tierId: UUID
    quantity: int
    price: float

    class Config:
        from_attributes = True