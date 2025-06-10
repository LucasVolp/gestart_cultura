from datetime import datetime
from pydantic import BaseModel
from uuid import UUID


class ReceiptResponse(BaseModel):
    """Data Transfer Object for receipt response.

    Attributes:
        id (str): The unique identifier of the receipt.
        purchaseId (str): The ID of the purchase associated with the receipt.
        total (float): The total amount of the receipt.
        status (str): The status of the receipt.
    """
    id: UUID
    userId: UUID
    purchaseId: UUID
    description: str
    createdAt: datetime
    updatedAt: datetime

    class Config:
        from_attributes = True