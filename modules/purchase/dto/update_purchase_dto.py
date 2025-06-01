from pydantic import BaseModel, field_validator
from typing import Optional
from models.models import PaymentStatus, PaymentMethod

class UpdatePurchaseDTO(BaseModel):
    """Data Transfer Object for updating a purchase.
    
    Attributes:
        buyerId (Optional[str]): The ID of the buyer.
        sellerId (Optional[str]): The ID of the seller.
        purchaseDate (Optional[str]): The date of the purchase.
        status (Optional[PaymentStatus]): The payment status.
        totalPrice (Optional[float]): The total price of the purchase.
        paymentMethod (Optional[PaymentMethod]): The payment method used.
    """
    buyerId: Optional[str] = None
    sellerId: Optional[str] = None
    status: Optional[PaymentStatus] = None
    totalPrice: Optional[float] = None
    paymentMethod: Optional[PaymentMethod] = None

    @field_validator('buyerId')
    @classmethod
    def validateBuyerId(cls, value):
        if value is not None and (not value or not value.strip()):
            raise ValueError('buyerId cannot be empty if provided')
        return value.strip() if value else value

    @field_validator('sellerId')
    @classmethod
    def validateSellerId(cls, value):
        if value is not None and (not value or not value.strip()):
            raise ValueError('sellerId cannot be empty if provided')
        return value.strip() if value else value

    @field_validator('totalPrice')
    @classmethod
    def validateTotalPrice(cls, value):
        if value is not None and value < 0:
            raise ValueError('totalPrice cannot be negative if provided')
        return value

    def isEmpty(self) -> bool:
        """Check if all fields are None or empty."""
        return all(value is None for value in self.model_dump().values())
