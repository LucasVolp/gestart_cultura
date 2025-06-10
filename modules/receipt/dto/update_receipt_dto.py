from uuid import UUID
from pydantic import BaseModel, field_validator
from typing import Optional

class UpdateReceiptDTO(BaseModel):
    """Data Transfer Object for updating a receipt.
    
    Attributes:
        userId (Optional[str]): The ID of the user who owns the receipt.
        purchaseId (Optional[str]): The ID of the purchase associated with the receipt.
        description (Optional[str]): Optional description of the receipt.
    """
    userId: Optional[UUID] = None
    purchaseId: Optional[UUID] = None
    description: Optional[str] = None

    @field_validator('userId')
    def validate_user_id(cls, value):
        if value is not None and (not value or not value.strip()):
            raise ValueError('userId cannot be empty if provided')
        return value.strip() if value else value

    @field_validator('purchaseId')
    def validate_purchase_id(cls, value):
        if value is not None and (not value or not value.strip()):
            raise ValueError('purchaseId cannot be empty if provided')
        return value.strip() if value else value

    @field_validator('description')
    def validate_description(cls, value):
        if value is not None and not value.strip():
            raise ValueError('description cannot be empty if provided')
        return value.strip() if value else value

    def isEmpty(self) -> bool:
        """Check if all fields are None or empty."""
        return all(value is None for value in self.__dict__.values())
