from dataclasses import dataclass
from typing import Optional

@dataclass
class CreateRatingDTO:
    userId: str
    eventId: str
    rate: int
    comment: Optional[str] = None
