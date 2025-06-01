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
    def validateName(cls, v):
        if not v or not v.strip():
            raise ValueError('name cannot be empty')
        return v.strip()

    @field_validator('description')
    @classmethod
    def validateDescription(cls, v):
        if not v or not v.strip():
            raise ValueError('description cannot be empty')
        return v.strip()

    @field_validator('local')
    @classmethod
    def validateLocal(cls, v):
        if not v or not v.strip():
            raise ValueError('local cannot be empty')
        return v.strip()

    @field_validator('size')
    @classmethod
    def validateSize(cls, v):
        if v <= 0:
            raise ValueError('size must be greater than 0')
        return v
    
    @field_validator('date')
    @classmethod
    def validateDate(cls, v):
        if not isinstance(v, Date) or v < Date.today():
            raise ValueError('date must be a valid date and cannot be in the past')
        return v

    @field_validator('producers')
    @classmethod
    def validateProducers(cls, v):
        if not v or len(v) == 0:
            raise ValueError('at least one producer is required')
        return v