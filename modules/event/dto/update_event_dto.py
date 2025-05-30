from dataclasses import dataclass
from typing import Optional
from enums import TypeEvent

@dataclass
class UpdateEventDTO:
    name: Optional[str] = None
    description: Optional[str] = None
    date: Optional[str] = None
    local: Optional[str] = None
    size: Optional[int] = None
    typeEvent: Optional[TypeEvent] = None

    def isEmpty(self) -> bool:
        return all(value is None for value in self.__dict__.values())