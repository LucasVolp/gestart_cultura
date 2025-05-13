from uuid import UUID
from datetime import date, datetime
import logging
import re
import bcrypt
from abc import ABC, abstractmethod
from enums.status import Status

class Authenticable(ABC):
    @abstractmethod
    def auth(self, email: str, senha: str) -> bool:
        """_summary_

        Args:
            email (str): _description_
            senha (str): _description_

        Returns:
            bool: _description_
        """
        pass

    @abstractmethod
    def updateProfile(self, name: str, birth: date, email: str, password: str) -> None:
        """_summary_

        Args:
            name (str): _description_
            birth (date): _description_
            email (str): _description_
            password (str): _description_
        """
        pass

    @abstractmethod
    def recoverPassword(self, email: str, cpf: str) -> bool:
        """_summary_

        Args:
            email (str): _description_
            cpf (str): _description_

        Returns:
            bool: _description_
        """
        pass

class Notifications(ABC):
    @abstractmethod
    def sendNotification(self, recipient: str, message: str) -> None:
        """_summary_

        Args:
            recipient (str): _description_
            message (str): _description_
        """
        pass

    @abstractmethod
    def scheduleNotification(self, recipient: str, message: str, datetime: date) -> None:
        """_summary_

        Args:
            recipient (str): _description_
            message (str): _description_
            datetime (date): _description_
        """
        pass

class Person(ABC):
    def __init__(self, id: UUID, name: str, cpf: str, birth: date, email: str, password: str, phone: str, status: Status):
        self.__id = id
        self.__name = name
        self.__cpf = cpf
        self.__birth = birth
        self.__email = email
        self.__password = password
        self._phone = phone
        self.__status = status

    def __str__(self):
        tipo = self.__class__.__name__
        return f"[{tipo}] Nome: {self.__name} | Email: {self.__email}"

    @staticmethod
    def _validate_cpf(cpf: str) -> bool:
        """_summary_

        Args:
            cpf (str): _description_

        Returns:
            bool: _description_
        """
        pattern = re.compile(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$')
        return bool(re.match(pattern, cpf))

    @staticmethod
    def _validate_email(email: str) -> bool:
        """_summary_

        Args:
            email (str): _description_

        Returns:
            bool: _description_
        """
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return bool(re.match(pattern, email))

    @staticmethod
    def _validate_password(password: str) -> bool:
        """_summary_

        Args:
            password (str): _description_

        Returns:
            bool: _description_
        """
        return len(password) >= 8 and any(c.isalpha() for c in password) and any(c.isdigit() for c in password)

    @staticmethod
    def _validate_phone(phone: str) -> bool:
        """_summary_

        Args:
            phone (str): _description_

        Returns:
            bool: _description_
        """
        pattern = r"^\(\d{2}\)\s9\d{4}-\d{4}$"
        return bool(re.match(pattern, phone))

    @staticmethod
    def _hash_password(password: str) -> bytes:
        """_summary_

        Args:
            password (str): _description_

        Returns:
            bytes: _description_
        """
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    @staticmethod
    def _check_password(password: str, hashed: bytes) -> bool:
        """_summary_

        Args:
            password (str): _description_
            hashed (bytes): _description_

        Returns:
            bool: _description_
        """
        return bcrypt.checkpw(password.encode('utf-8'), hashed)

    @property
    def id(self) -> UUID:
        return self.__id

    @property
    def name(self) -> str:
        return self.__name

    @property
    def cpf(self) -> str:
        return self.__cpf

    @property
    def birth(self) -> date:
        return self.__birth

    @property
    def email(self) -> str:
        return self.__email

    @property
    def phone(self) -> str:
        return self.__phone

    @property
    def status(self) -> Status:
        return self.__status

    def auth(self, email: str, senha: str) -> bool:
        """_summary_

        Args:
            email (str): _description_
            senha (str): _description_

        Raises:
            ValueError: _description_
            ValueError: _description_
            ValueError: _description_
            ValueError: _description_

        Returns:
            bool: _description_
        """
        try:
            if not self._validate_email(email):
                raise ValueError("Email inválido.")
            if email != self.__email:
                raise ValueError("Email não encontrado.")
            if not self._check_password(senha, self.__password):
                raise ValueError("Senha incorreta.")
            if self.__status != Status.ACTIVE:
                raise ValueError("Conta inativa.")
            return True
        except ValueError as e:
            logging.error(f"Erro na autenticação para {email}: {str(e)}")
            return False
        except Exception as e:
            logging.error(f"Erro inesperado na autenticação para {email}: {str(e)}")
            return False

    def updateProfile(self, name: str, birth: date, email: str, password: str) -> None:
        """_summary_

        Args:
            name (str): _description_
            birth (date): _description_
            email (str): _description_
            password (str): _description_

        Raises:
            ValueError: _description_
            ValueError: _description_
            ValueError: _description_
            ValueError: _description_
        """
        try:
            if name and not name.strip():
                raise ValueError("O nome não pode ser vazio.")
            if birth and birth >= date.today():
                raise ValueError("A data de nascimento deve ser no passado.")
            if email and not self._validate_email(email):
                raise ValueError("Email inválido.")
            if password and not self._validate_password(password):
                raise ValueError("A senha deve ter pelo menos 8 caracteres, incluindo letras e números.")
            self.__name = name if name else self.__name
            self.__birth = birth if birth else self.__birth
            self.__email = email if email else self.__email
            self.__password = self._hash_password(password) if password else self.__password
        except ValueError as e:
            logging.error(f"Erro ao atualizar perfil para {self.__email}: {str(e)}")
            raise
        except Exception as e:
            logging.error(f"Erro inesperado ao atualizar perfil para {self.__email}: {str(e)}")
            raise
    
    def recoverPassword(self, email: str, cpf: str) -> bool:
        """_summary_

        Args:
            email (str): _description_
            cpf (str): _description_

        Raises:
            ValueError: _description_
            ValueError: _description_
            ValueError: _description_

        Returns:
            bool: _description_
        """
        try:
            if not self._validate_email(email):
                raise ValueError("Email inválido.")
            if not self._validate_cpf(cpf):
                raise ValueError("CPF inválido.")
            if email != self.__email or cpf != self.__cpf:
                raise ValueError("Email ou CPF não correspondem.")
            # Simula envio de link de recuperação (implementação real teria que enviar um email)
            logging.info(f"Link de recuperação de senha enviado para {email}")
            return True
        except ValueError as e:
            logging.error(f"Erro na recuperação de senha para {email}: {str(e)}")
            return False
        except Exception as e:
            logging.error(f"Erro inesperado na recuperação de senha para {email}: {str(e)}")
            return False

    @abstractmethod
    def sendNotification(self, recipient: str, message: str) -> None:
        """_summary_

        Args:
            recipient (str): _description_
            message (str): _description_
        """
        pass

    @abstractmethod
    def scheduleNotification(self, recipient: str, message: str, datetime: date) -> None:
        """_summary_

        Args:
            recipient (str): _description_
            message (str): _description_
            datetime (date): _description_
        """
        pass

