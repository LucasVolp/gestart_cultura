from dataclasses import dataclass
from typing import Optional
from models.models import Status

@dataclass
class UpdateTicketDTO:
    ownerId: Optional[str] = None
    tierId: Optional[str] = None
    sellerId: Optional[str] = None
    status: Optional[Status] = None

    def isEmpty(self) -> bool:
        return all(value is None for value in self.__dict__.values())
