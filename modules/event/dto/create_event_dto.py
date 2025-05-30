from dataclasses import dataclass
from enums import TypeEvent

@dataclass
class CreateEventDTO:
    name: str
    description: str
    date: str
    local: str
    size: int
    typeEvent: TypeEvent