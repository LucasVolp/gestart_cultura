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
    def validateBuyerId(cls, v):
        if v is not None and (not v or not v.strip()):
            raise ValueError('buyerId cannot be empty if provided')
        return v.strip() if v else v

    @field_validator('sellerId')
    @classmethod
    def validateSellerId(cls, v):
        if v is not None and (not v or not v.strip()):
            raise ValueError('sellerId cannot be empty if provided')
        return v.strip() if v else v

    @field_validator('totalPrice')
    @classmethod
    def validateTotalPrice(cls, v):
        if v is not None and v < 0:
            raise ValueError('totalPrice cannot be negative if provided')
        return v

    def isEmpty(self) -> bool:
        """Check if all fields are None or empty."""
        return all(value is None for value in self.model_dump().values())
