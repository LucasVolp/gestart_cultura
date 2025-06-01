from dataclasses import dataclass
from typing import Optional
from models.models import Role

@dataclass
class CreateUserDTO:
    name: str
    cpf: str
    birth: str
    email: str
    password: str
    phone: str
    role: Role
    cnpj: Optional[str] = None
    enterprise: Optional[str] = None
