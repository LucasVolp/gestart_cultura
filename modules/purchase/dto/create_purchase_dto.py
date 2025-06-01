from pydantic import BaseModel, field_validator
from typing import Optional
from models.models import PaymentStatus, PaymentMethod

class CreatePurchaseDTO(BaseModel):
    """Data Transfer Object for creating a purchase.
    
    Attributes:
        buyerId (str): The ID of the buyer.
        sellerId (str): The ID of the seller.
        purchaseDate (str): The date of the purchase.
        status (Optional[PaymentStatus]): The payment status, default is None.
        totalPrice (float): The total price of the purchase, default is 0.0.
        paymentMethod (PaymentMethod): The payment method used.
    """
    buyerId: str
    sellerId: str
    status: Optional[PaymentStatus] = None
    totalPrice: float = 0.0
    paymentMethod: PaymentMethod

    @field_validator('buyerId')
    @classmethod
    def validateBuyerId(cls, v):
        if not v or not v.strip():
            raise ValueError('buyerId cannot be empty')
        return v.strip()

    @field_validator('sellerId')
    @classmethod
    def validateSellerId(cls, v):
        if not v or not v.strip():
            raise ValueError('sellerId cannot be empty')
        return v.strip()

    @field_validator('totalPrice')
    @classmethod
    def validateTotalPrice(cls, v):
        if v < 0:
            raise ValueError('totalPrice cannot be negative')
        return v
