from dataclasses import dataclass
from typing import Optional
from enums import Status

@dataclass
class CreateTierDTO:
    """Data Transfer Object for creating a tier.
    Attributes:
        amount (int): The number of tickets available for this tier.
        name (str): The name of the tier.
        price (float): The price of the tier.
        startDate (str): The start date for the tier's availability.
        endDate (str): The end date for the tier's availability.
        status (Optional[Status]): The status of the tier, default is None.
        eventId (str): The ID of the event this tier belongs to, default is None.
    """
    amount: int
    name: str
    price: float
    startDate: str
    endDate: str
    status: Optional[Status] = None
    eventId: str = None
