from dataclasses import dataclass
from typing import Optional

@dataclass
class CreateReceiptDTO:
    userId: str
    purchaseId: str
    description: Optional[str] = None
