from dataclasses import dataclass

@dataclass
class CreateSellerDTO:
    name: str
    cpf: str
    birth: str
    email: str
    password: str
    phone: str 
