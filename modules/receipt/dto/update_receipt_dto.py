from pydantic import BaseModel, validator
from typing import Optional

class UpdateReceiptDTO(BaseModel):
    """Data Transfer Object for updating a receipt.
    
    Attributes:
        userId (Optional[str]): The ID of the user who owns the receipt.
        purchaseId (Optional[str]): The ID of the purchase associated with the receipt.
        description (Optional[str]): Optional description of the receipt.
    """
    userId: Optional[str] = None
    purchaseId: Optional[str] = None
    description: Optional[str] = None

    @validator('userId')
    def validate_user_id(cls, value):
        if value is not None and (not value or not value.strip()):
            raise ValueError('userId cannot be empty if provided')
        return value.strip() if value else value

    @validator('purchaseId')
    def validate_purchase_id(cls, value):
        if value is not None and (not value or not value.strip()):
            raise ValueError('purchaseId cannot be empty if provided')
        return value.strip() if value else value

    @validator('description')
    def validate_description(cls, value):
        if value is not None and not value.strip():
            raise ValueError('description cannot be empty if provided')
        return value.strip() if value else value

    def isEmpty(self) -> bool:
        """Check if all fields are None or empty."""
        return all(value is None for value in self.__dict__.values())
