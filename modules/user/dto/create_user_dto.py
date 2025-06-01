from pydantic import BaseModel, field_validator
from typing import Optional
from models.models import Role
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
    birth: str
    email: str
    password: str
    phone: str
    role: Role
    cnpj: Optional[str] = None
    enterprise: Optional[str] = None

    @field_validator('name')
    @classmethod
    def validateName(cls, v):
        if not v or not v.strip():
            raise ValueError('name cannot be empty')
        return v.strip()

    @field_validator('cpf')
    @classmethod
    def validateCpf(cls, v):
        if not v or not v.strip():
            raise ValueError('cpf cannot be empty')
        # Remove caracteres não numéricos
        cpf_clean = re.sub(r'\D', '', v.strip())
        if len(cpf_clean) != 11:
            raise ValueError('cpf must have exactly 11 digits')
        return cpf_clean

    @field_validator('email')
    @classmethod
    def validateEmail(cls, v):
        if not v or not v.strip():
            raise ValueError('email cannot be empty')
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_regex, v.strip()):
            raise ValueError('email must be a valid email address')
        return v.strip().lower()

    @field_validator('password')
    @classmethod
    def validatePassword(cls, v):
        if not v or not v.strip():
            raise ValueError('password cannot be empty')
        if len(v.strip()) < 6:
            raise ValueError('password must have at least 6 characters')
        return v.strip()

    @field_validator('phone')
    @classmethod
    def validatePhone(cls, v):
        if not v or not v.strip():
            raise ValueError('phone cannot be empty')
        # Remove caracteres não numéricos
        phone_clean = re.sub(r'\D', '', v.strip())
        if len(phone_clean) < 10 or len(phone_clean) > 11:
            raise ValueError('phone must have 10 or 11 digits')
        return phone_clean

    @field_validator('cnpj')
    @classmethod
    def validateCnpj(cls, v):
        if v is not None:
            if not v.strip():
                raise ValueError('cnpj cannot be empty if provided')
            # Remove caracteres não numéricos
            cnpj_clean = re.sub(r'\D', '', v.strip())
            if len(cnpj_clean) != 14:
                raise ValueError('cnpj must have exactly 14 digits if provided')
            return cnpj_clean
        return v

    @field_validator('enterprise')
    @classmethod
    def validateEnterprise(cls, v):
        if v is not None and not v.strip():
            raise ValueError('enterprise cannot be empty if provided')
        return v.strip() if v else v
