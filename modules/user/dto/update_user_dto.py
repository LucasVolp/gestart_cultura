from pydantic import BaseModel, field_validator
from typing import Optional
from models.models import Role
import re

class UpdateUserDTO(BaseModel):
    """Data Transfer Object for updating a user.
    
    Attributes:
        name (Optional[str]): The name of the user.
        cpf (Optional[str]): The CPF of the user.
        birth (Optional[str]): The birth date of the user.
        email (Optional[str]): The email of the user.
        password (Optional[str]): The password of the user.
        phone (Optional[str]): The phone number of the user.
        role (Optional[Role]): The role of the user.
        balance (Optional[float]): The balance of the user.
        cnpj (Optional[str]): The CNPJ for business users.
        enterprise (Optional[str]): The enterprise name for business users.
    """
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

    @field_validator('name')
    @classmethod
    def validateName(cls, v):
        if v is not None and (not v or not v.strip()):
            raise ValueError('name cannot be empty if provided')
        return v.strip() if v else v

    @field_validator('cpf')
    @classmethod
    def validateCpf(cls, v):
        if v is not None:
            if not v or not v.strip():
                raise ValueError('cpf cannot be empty if provided')
            cpf_clean = re.sub(r'\D', '', v.strip())
            if len(cpf_clean) != 11:
                raise ValueError('cpf must have exactly 11 digits if provided')
            return cpf_clean
        return v

    @field_validator('email')
    @classmethod
    def validateEmail(cls, v):
        if v is not None:
            if not v or not v.strip():
                raise ValueError('email cannot be empty if provided')
            email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
            if not re.match(email_regex, v.strip()):
                raise ValueError('email must be a valid email address if provided')
            return v.strip().lower()
        return v

    @field_validator('password')
    @classmethod
    def validatePassword(cls, v):
        if v is not None:
            if not v or not v.strip():
                raise ValueError('password cannot be empty if provided')
            if len(v.strip()) < 6:
                raise ValueError('password must have at least 6 characters if provided')
            return v.strip()
        return v

    @field_validator('phone')
    @classmethod
    def validatePhone(cls, v):
        if v is not None:
            if not v or not v.strip():
                raise ValueError('phone cannot be empty if provided')
            phone_clean = re.sub(r'\D', '', v.strip())
            if len(phone_clean) < 10 or len(phone_clean) > 11:
                raise ValueError('phone must have 10 or 11 digits if provided')
            return phone_clean
        return v

    @field_validator('balance')
    @classmethod
    def validateBalance(cls, v):
        if v is not None and v < 0:
            raise ValueError('balance cannot be negative if provided')
        return v

    @field_validator('cnpj')
    @classmethod
    def validateCnpj(cls, v):
        if v is not None:
            if not v.strip():
                raise ValueError('cnpj cannot be empty if provided')
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

    def isEmpty(self) -> bool:
        """Check if all fields are None or empty."""
        return all(value is None for value in self.model_dump().values())
