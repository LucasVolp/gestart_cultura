from pydantic import BaseModel, field_validator
from typing import Optional, List
from models.models import TypeEvent
from datetime import date as Date
from uuid import UUID

class UpdateEventDTO(BaseModel):
    """Data Transfer Object for updating an event.
    
    Attributes:
        name (Optional[str]): The name of the event.
        description (Optional[str]): The description of the event.
        date (Optional[Date]): The date of the event.
        local (Optional[str]): The location of the event.
        size (Optional[int]): The capacity/size of the event.
        typeEvent (Optional[TypeEvent]): The type of the event.
        producers (Optional[List[UUID]]): List of producer IDs associated with the event.
    """
    name: Optional[str] = None
    description: Optional[str] = None
    date: Optional[Date] = None
    local: Optional[str] = None
    size: Optional[int] = None
    typeEvent: Optional[TypeEvent] = None
    producers: Optional[List[UUID]] = None

    @field_validator('name')
    @classmethod
    def validate_name(cls, v):
        if v is not None and (not v or not v.strip()):
            raise ValueError('name cannot be empty if provided')
        return v.strip() if v else v

    @field_validator('local')
    @classmethod
    def validate_local(cls, v):
        if v is not None and (not v or not v.strip()):
            raise ValueError('local cannot be empty if provided')
        return v.strip() if v else v

    @field_validator('size')
    @classmethod
    def validate_size(cls, v):
        if v is not None and v <= 0:
            raise ValueError('size must be greater than 0 if provided')
        return v
    
    @field_validator('date')
    @classmethod
    def validate_date(cls, v):
        if v is not None and (not isinstance(v, Date) or v < Date.today()):
            raise ValueError('date must be a valid date and cannot be in the past if provided')
        return v

    def isEmpty(self) -> bool:
        """Check if all fields are None or empty."""
        return all(value is None for value in self.__dict__.values())