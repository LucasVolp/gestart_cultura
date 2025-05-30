from dataclasses import dataclass
from typing import Optional

@dataclass
class UpdateRatingDTO:
    rate: Optional[int] = None
    comment: Optional[str] = None

    def is_empty(self) -> bool:
        return all(value is None for value in self.__dict__.values())
