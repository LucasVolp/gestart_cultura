from dataclasses import dataclass
from typing import Optional

@dataclass
class UpdateReceiptDTO:
    userId: Optional[str] = None
    purchaseId: Optional[str] = None
    description: Optional[str] = None

    def isEmpty(self) -> bool:
        return all(value is None for value in self.__dict__.values())
