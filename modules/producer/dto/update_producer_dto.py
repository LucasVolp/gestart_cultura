from dataclasses import dataclass

@dataclass
class UpdateProducerDTO:
    name: str | None = None
    cpf: str | None = None
    birth: str | None = None
    email: str | None = None
    password: str | None = None
    phone: str | None = None
    cnpj: str | None = None
    enterprise: str | None = None

    def is_empty(self) -> bool:
        return all(value is None for value in self.__dict__.values())