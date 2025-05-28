from dataclasses import dataclass

@dataclass
class CreateProducerDTO:
    name: str
    cpf: str
    birth: str
    email: str
    password: str
    phone: str
    cnpj: str
    enterprise: str