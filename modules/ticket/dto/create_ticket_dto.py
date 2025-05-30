from dataclasses import dataclass
from typing import Optional

@dataclass
class CreateTicketDTO:
    ownerId: str
    tierId: str
    sellerId: str
    status: Optional[str] = None
