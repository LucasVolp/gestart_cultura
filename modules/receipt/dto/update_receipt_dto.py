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
    def validate_user_id(cls, v):
        if v is not None and (not v or not v.strip()):
            raise ValueError('userId cannot be empty if provided')
        return v.strip() if v else v

    @validator('purchaseId')
    def validate_purchase_id(cls, v):
        if v is not None and (not v or not v.strip()):
            raise ValueError('purchaseId cannot be empty if provided')
        return v.strip() if v else v

    @validator('description')
    def validate_description(cls, v):
        if v is not None and not v.strip():
            raise ValueError('description cannot be empty if provided')
        return v.strip() if v else v

    def isEmpty(self) -> bool:
        """Check if all fields are None or empty."""
        return all(value is None for value in self.__dict__.values())
