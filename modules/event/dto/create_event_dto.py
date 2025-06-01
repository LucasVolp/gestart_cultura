from dataclasses import dataclass
from pydantic import BaseModel
from typing import List
from uuid import UUID
from datetime import date
from models.models import TypeEvent

@dataclass
class CreateEventDTO(BaseModel):
    name: str
    description: str
    date: date
    local: str
    size: int
    typeEvent: TypeEvent
    producers: List[UUID]