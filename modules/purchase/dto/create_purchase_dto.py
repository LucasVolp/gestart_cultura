from uuid import UUID
from pydantic import BaseModel, field_validator
from typing import Optional, List
from models.models import PaymentStatus, PaymentMethod

class ItemDataForPurchase(BaseModel):
    """Dados de um item para incluir em uma nova compra."""
    tierId: UUID
    quantity: int

    @field_validator('tierId')
    @classmethod
    def validateTierId(cls, value):
        if not value:
            raise ValueError('tierId do item não pode ser vazio')
        return value

    @field_validator('quantity')
    @classmethod
    def validateQuantity(cls, value):
        if value <= 0:
            raise ValueError('A quantidade do item deve ser maior que 0')
        return value

class CreatePurchaseDTO(BaseModel):
    """Data Transfer Object for creating a purchase.
    
    Attributes:
        buyerId (str): The ID of the buyer.
        sellerId (str): The ID of the seller.
        paymentMethod (PaymentMethod): The payment method used.
        status (Optional[PaymentStatus]): The payment status, default is PENDING.
        items (List[ItemDataForPurchase]): Lista de itens a serem comprados.
    """
    buyerId: UUID
    sellerId: UUID
    paymentMethod: PaymentMethod
    status: Optional[PaymentStatus] = PaymentStatus.PENDING
    items: List[ItemDataForPurchase]

    @field_validator('buyerId')
    @classmethod
    def validateBuyerId(cls, value):
        if not value:
            raise ValueError('buyerId não pode ser vazio')
        return value

    @field_validator('sellerId')
    @classmethod
    def validateSellerId(cls, value):
        if not value:
            raise ValueError('sellerId não pode ser vazio')
        return value

    @field_validator('items')
    @classmethod
    def validateItemsNotEmpty(cls, value):
        if not value:
            raise ValueError('A compra deve conter pelo menos um item.')
        return value
