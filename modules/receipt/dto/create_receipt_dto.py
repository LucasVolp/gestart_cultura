from pydantic import BaseModel, field_validator
from typing import Optional

class CreateReceiptDTO(BaseModel):
    """Data Transfer Object for creating a receipt.
    
    Attributes:
        userId (str): The ID of the user who owns the receipt.
        purchaseId (str): The ID of the purchase associated with the receipt.
        description (Optional[str]): Optional description of the receipt.
    """
    userId: str
    purchaseId: str
    description: Optional[str] = None

    @field_validator('userId')
    def validate_user_id(cls, v):
        if not v or not v.strip():
            raise ValueError('userId cannot be empty')
        return v.strip()

    @field_validator('purchaseId')
    def validate_purchase_id(cls, v):
        if not v or not v.strip():
            raise ValueError('purchaseId cannot be empty')
        return v.strip()

    @field_validator('description')
    def validate_description(cls, v):
        if v is not None and not v.strip():
            raise ValueError('description cannot be empty if provided')
        return v.strip() if v else v
