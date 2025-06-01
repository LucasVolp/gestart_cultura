from pydantic import BaseModel, field_validator
from typing import Optional

class UpdatePurchaseItemDTO(BaseModel):
    """Data Transfer Object for updating a purchase item.
    
    Attributes:
        purchaseId (Optional[str]): The ID of the purchase.
        tierId (Optional[str]): The ID of the tier.
        quantity (Optional[int]): The quantity of items.
        unitPrice (Optional[float]): The unit price of the item.
        totalPrice (Optional[float]): The total price for all items.
    """
    purchaseId: Optional[str] = None
    tierId: Optional[str] = None
    quantity: Optional[int] = None
    unitPrice: Optional[float] = None
    totalPrice: Optional[float] = None

    @field_validator('purchaseId')
    @classmethod
    def validatePurchaseId(cls, v):
        if v is not None and (not v or not v.strip()):
            raise ValueError('purchaseId cannot be empty if provided')
        return v.strip() if v else v

    @field_validator('tierId')
    @classmethod
    def validateTierId(cls, v):
        if v is not None and (not v or not v.strip()):
            raise ValueError('tierId cannot be empty if provided')
        return v.strip() if v else v

    @field_validator('quantity')
    @classmethod
    def validateQuantity(cls, v):
        if v is not None and v <= 0:
            raise ValueError('quantity must be greater than 0 if provided')
        return v

    @field_validator('unitPrice')
    @classmethod
    def validateUnitPrice(cls, v):
        if v is not None and v < 0:
            raise ValueError('unitPrice cannot be negative if provided')
        return v

    @field_validator('totalPrice')
    @classmethod
    def validateTotalPrice(cls, v):
        if v is not None and v < 0:
            raise ValueError('totalPrice cannot be negative if provided')
        return v

    def isEmpty(self) -> bool:
        """Check if all fields are None or empty."""
        return all(value is None for value in self.model_dump().values())
