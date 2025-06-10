from pydantic import BaseModel, field_validator
from typing import List
from uuid import UUID
from datetime import date as Date
from models.models import TypeEvent

class CreateEventDTO(BaseModel):
    """Data Transfer Object for creating a new event.
    
    Attributes:
        name (str): The name of the event.
        description (str): The description of the event.
        date (Date): The date of the event.
        local (str): The location of the event.
        size (int): The capacity/size of the event.
        typeEvent (TypeEvent): The type of the event.
        producers (List[UUID]): List of producer IDs associated with the event.
    """
    name: str
    description: str
    date: Date
    local: str
    size: int
    typeEvent: TypeEvent
    producers: List[UUID]

    @field_validator('name')
    @classmethod
    def validateName(cls, value):
        if not value or not value.strip():
            raise ValueError('name cannot be empty')
        return value.strip()

    @field_validator('description')
    @classmethod
    def validateDescription(cls, value):
        if not value or not value.strip():
            raise ValueError('description cannot be empty')
        return value.strip()

    @field_validator('local')
    @classmethod
    def validateLocal(cls, value):
        if not value or not value.strip():
            raise ValueError('local cannot be empty')
        return value.strip()

    @field_validator('size')
    @classmethod
    def validateSize(cls, value):
        if value <= 0:
            raise ValueError('size must be greater than 0')
        return value
    
    @field_validator('date')
    @classmethod
    def validateDate(cls, value):
        if not isinstance(value, Date) or value < Date.today():
            raise ValueError('date must be a valid date and cannot be in the past')
        return value

    @field_validator('producers')
    @classmethod
    def validateProducers(cls, value):
        if not value or len(value) == 0:
            raise ValueError('at least one producer is required')
        return value