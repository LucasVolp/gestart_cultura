from dataclasses import dataclass
from typing import Optional
from enums import Status

@dataclass
class UpdateTierDTO:
    """Data Transfer Object for updating a tier.

    Returns:
        _type_: This class represents the data required to update a tier.
    """
    amount: Optional[int] = None
    name: Optional[str] = None
    price: Optional[float] = None
    startDate: Optional[str] = None
    endDate: Optional[str] = None
    status: Optional[Status] = None
    eventId: Optional[str] = None

    def isEmpty(self) -> bool:
        return all(value is None for value in self.__dict__.values())
