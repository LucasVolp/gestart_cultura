from pydantic import BaseModel, field_validator, model_validator
from typing import Optional
from models.models import Role
from datetime import date as Date
import re

class CreateUserDTO(BaseModel):
    """Data Transfer Object for creating a user.
    
    Attributes:
        name (str): The name of the user.
        cpf (str): The CPF of the user.
        birth (str): The birth date of the user.
        email (str): The email of the user.
        password (str): The password of the user.
        phone (str): The phone number of the user.
        role (Role): The role of the user.
        cnpj (Optional[str]): The CNPJ for business users.
        enterprise (Optional[str]): The enterprise name for business users.
    """
    name: str
    cpf: str
    birth: Date
    email: str
    password: str
    phone: str
    role: Role
    cnpj: Optional[str] = None
    enterprise: Optional[str] = None

    @model_validator(mode='after')
    def checkProducerFields(self):
        if self.role == Role.PRODUCER:
            if not self.cnpj or not self.enterprise:
                raise ValueError('cnpj and enterprise must be provided for producers')
        else:
            if self.cnpj or self.enterprise:
                raise ValueError('cnpj and enterprise should not be provided for non-producer roles')
        return self

    @field_validator('name')
    @classmethod
    def validateName(cls, value):
        if not value or not value.strip():
            raise ValueError('name cannot be empty')
        return value.strip()

    @field_validator('cpf')
    @classmethod
    def validateCpf(cls, value):
        if not value or not value.strip():
            raise ValueError('cpf cannot be empty')
        cpf_clean = re.sub(r'\D', '', value.strip())
        if len(cpf_clean) != 11:
            raise ValueError('cpf must have exactly 11 digits')
        return cpf_clean

    @field_validator('email')
    @classmethod
    def validateEmail(cls, value):
        if not value or not value.strip():
            raise ValueError('email cannot be empty')
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_regex, value.strip()):
            raise ValueError('email must be a valid email address')
        return value.strip().lower()

    @field_validator('password')
    @classmethod
    def validatePassword(cls, value):
        if not value or not value.strip():
            raise ValueError('password cannot be empty')
        if len(value.strip()) < 6:
            raise ValueError('password must have at least 6 characters')
        return value.strip()

    @field_validator('phone')
    @classmethod
    def validatePhone(cls, value):
        if not value or not value.strip():
            raise ValueError('phone cannot be empty')
        phone_clean = re.sub(r'\D', '', value.strip())
        if len(phone_clean) < 10 or len(phone_clean) > 11:
            raise ValueError('phone must have 10 or 11 digits')
        return phone_clean

    @field_validator('cnpj')
    @classmethod
    def validateCnpj(cls, value):
        if value is not None:
            if not value.strip():
                raise ValueError('cnpj cannot be empty if provided')
            cnpj_clean = re.sub(r'\D', '', value.strip())
            if len(cnpj_clean) != 14:
                raise ValueError('cnpj must have exactly 14 digits if provided')
            return cnpj_clean
        return value

    @field_validator('enterprise')
    @classmethod
    def validateEnterprise(cls, value):
        if value is not None and not value.strip():
            raise ValueError('enterprise cannot be empty if provided')
        return value.strip() if value else value
