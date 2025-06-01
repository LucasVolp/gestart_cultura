from dataclasses import dataclass
from typing import Optional
from models.models import Status

@dataclass
class CreateTicketDTO:
    ownerId: str
    tierId: str
    sellerId: str
    status: Optional[Status] = None
