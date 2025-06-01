from dataclasses import dataclass
from typing import Optional, List
from pydantic import BaseModel
from models.models import TypeEvent
from datetime import date
from uuid import UUID

@dataclass
class UpdateEventDTO(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    date: Optional["date"] = None
    local: Optional[str] = None
    size: Optional[int] = None
    typeEvent: Optional[TypeEvent] = None
    producers: Optional[List[UUID]] = None

    def isEmpty(self) -> bool:
        return all(value is None for value in self.__dict__.values())