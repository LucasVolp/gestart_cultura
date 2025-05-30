from dataclasses import dataclass
from typing import Optional

@dataclass
class UpdateProducerDTO:
    name: Optional[str] = None
    cpf: Optional[str] = None
    birth: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None
    phone: Optional[str] = None
    cnpj: Optional[str] = None
    enterprise: Optional[str] = None

    def isEmpty(self) -> bool:
        return all(value is None for value in self.__dict__.values())