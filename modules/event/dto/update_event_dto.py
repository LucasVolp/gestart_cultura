from dataclasses import dataclass
from enums import TypeEvent

@dataclass
class UpdateEventDTO:
    name: str | None = None
    description: str | None = None
    date: str | None = None
    local: str | None = None
    size: int | None = None
    typeEvent: TypeEvent | None = None

    def isEmpty(self) -> bool:
        return all(value is None for value in self.__dict__.values())