from dataclasses import dataclass

@dataclass
class CreateUserDTO:
    name: str
    cpf: str
    birth: str
    email: str
    password: str
    phone: str
