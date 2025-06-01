from dataclasses import dataclass
from typing import Optional

from models.models import Role

@dataclass
class UpdateUserDTO:
    name: Optional[str] = None
    cpf: Optional[str] = None
    birth: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None
    phone: Optional[str] = None
    role: Optional[Role] = None
    balance: Optional[float] = None
    cnpj: Optional[str] = None
    enterprise: Optional[str] = None

    def isEmpty(self) -> bool:
        return all(value is None for value in self.__dict__.values())
