from pydantic import BaseModel, field_validator
from typing import Optional, List
from models.models import Status, TypeEvent
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
    status: Optional[Status] = None
    producers: Optional[List[UUID]] = None

    @field_validator('name')
    @classmethod
    def validate_name(cls, value):
        if value is not None and (not value or not value.strip()):
            raise ValueError('name cannot be empty if provided')
        return value.strip() if value else value

    @field_validator('local')
    @classmethod
    def validate_local(cls, value):
        if value is not None and (not value or not value.strip()):
            raise ValueError('local cannot be empty if provided')
        return value.strip() if value else value

    @field_validator('size')
    @classmethod
    def validate_size(cls, value):
        if value is not None and value <= 0:
            raise ValueError('size must be greater than 0 if provided')
        return value
    
    @field_validator('date')
    @classmethod
    def validate_date(cls, value):
        if value is not None and (not isinstance(value, Date) or value < Date.today()):
            raise ValueError('date must be a valid date and cannot be in the past if provided')
        return value
    
    @field_validator('producers')
    @classmethod
    def validate_producers(cls, value):
        if value is not None and not isinstance(value, list):
            raise ValueError('producers must be a list of UUIDs if provided')
        return value
    
    @field_validator('typeEvent')
    @classmethod
    def validate_type_event(cls, value):
        if value is not None and not isinstance(value, TypeEvent):
            raise ValueError('typeEvent must be a valid TypeEvent enum if provided')
        return value

    def isEmpty(self) -> bool:
        """Check if all fields are None or empty."""
        return all(value is None for value in self.__dict__.values())