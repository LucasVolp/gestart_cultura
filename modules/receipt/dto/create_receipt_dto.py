from uuid import UUID
from pydantic import BaseModel, field_validator
from typing import Optional

class CreateReceiptDTO(BaseModel):
    """Data Transfer Object for creating a receipt.
    
    Attributes:
        userId (str): The ID of the user who owns the receipt.
        purchaseId (str): The ID of the purchase associated with the receipt.
        description (Optional[str]): Optional description of the receipt.
    """
    userId: UUID
    purchaseId: UUID
    description: Optional[str] = None

    @field_validator('userId')
    def validate_user_id(cls, value):
        if not value:
            raise ValueError('userId cannot be empty')
        if not isinstance(value, UUID):
            raise ValueError('userId must be a valid UUID')
        return value

    @field_validator('purchaseId')
    def validate_purchase_id(cls, value):
        if not value:
            raise ValueError('purchaseId cannot be empty')
        if not isinstance(value, UUID):
            raise ValueError('purchaseId must be a valid UUID')
        return value

    @field_validator('description')
    def validate_description(cls, value):
        if value is not None and not value.strip():
            raise ValueError('description cannot be empty if provided')
        return value.strip() if value else value
