from pydantic import BaseModel, field_validator

class CreatePurchaseItemDTO(BaseModel):
    """Data Transfer Object for creating a purchase item.
    
    Attributes:
        purchaseId (str): The ID of the purchase.
        tierId (str): The ID of the tier.
        quantity (int): The quantity of items.
        unitPrice (float): The unit price of the item.
        totalPrice (float): The total price for all items.
    """
    purchaseId: str
    tierId: str
    quantity: int
    unitPrice: float
    totalPrice: float

    @field_validator('purchaseId')
    @classmethod
    def validatePurchaseId(cls, value):
        if not value or not value.strip():
            raise ValueError('purchaseId cannot be empty')
        return value.strip()

    @field_validator('tierId')
    @classmethod
    def validateTierId(cls, value):
        if not value or not value.strip():
            raise ValueError('tierId cannot be empty')
        return value.strip()

    @field_validator('quantity')
    @classmethod
    def validateQuantity(cls, value):
        if value <= 0:
            raise ValueError('quantity must be greater than 0')
        return value

    @field_validator('unitPrice')
    @classmethod
    def validateUnitPrice(cls, value):
        if value < 0:
            raise ValueError('unitPrice cannot be negative')
        return value

    @field_validator('totalPrice')
    @classmethod
    def validateTotalPrice(cls, value):
        if value < 0:
            raise ValueError('totalPrice cannot be negative')
        return value
