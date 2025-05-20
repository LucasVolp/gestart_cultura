from uuid import UUID
from datetime import date, datetime
import re
import bcrypt
from abc import ABC, abstractmethod
from enums.status import Status

class Authenticable(ABC):
    @abstractmethod
    def auth(self, email: str, password: str) -> bool:
        """_summary_

        Args:
            email (str): _description_
            password (str): _description_

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

class Person(Authenticable, ABC):
    def __init__(self, id: UUID, name: str, cpf: str, birth: date, email: str, password: str, phone: str, status: Status):
        if isinstance(birth, str):
            birth = datetime.strptime(birth, "%d/%m/%Y").date()
        self.__id = id
        self.__name = name
        self.__cpf = cpf if self.validateCPF(cpf) else None
        self.__birth = birth if birth < date.today() else None
        self.__email = email if self.validateEmail(email) else None
        self.__password = self.hashPassword(password) if self.validatePassword(password) else None
        self._phone = phone if self.validatePhone(phone) else None
        self.__status = status

    def __str__(self):
        tipo = self.__class__.__name__
        return f"[{tipo}] Nome: {self.__name} | Email: {self.__email}"

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
    
    
    @staticmethod
    def validateCPF(cpf: str) -> bool:
        """_summary_

        Args:
            cpf (str): _description_

        Returns:
            bool: _description_
        """
        cpf = re.sub(r'\D', '', cpf)
        if len(cpf) != 11 or cpf == cpf[0] * 11:
            return False

        soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
        resto = soma % 11
        d10 = 0 if resto < 2 else 11 - resto

        soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
        resto = soma % 11
        d11 = 0 if resto < 2 else 11 - resto

        return int(cpf[9]) == d10 and int(cpf[10]) == d11

    
    @staticmethod
    def validateEmail(email: str) -> bool:
        """_summary_

        Args:
            email (str): _description_

        Returns:
            bool: _description_
        """
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return bool(re.match(pattern, email))

    @staticmethod
    def validatePassword(password: str) -> bool:
        """_summary_

        Args:
            password (str): _description_

        Returns:
            bool: _description_
        """
        return len(password) >= 8 and any(c.isalpha() for c in password) and any(c.isdigit() for c in password)

    @staticmethod
    def validatePhone(phone: str) -> bool:
        """_summary_

        Args:
            phone (str): _description_

        Returns:
            bool: _description_
        """
        pattern = r"^\(\d{2}\)\s9\d{4}-\d{4}$"
        return bool(re.match(pattern, phone))

    @staticmethod
    def hashPassword(password: str) -> bytes:
        """_summary_

        Args:
            password (str): _description_

        Returns:
            bytes: _description_
        """
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    @staticmethod
    def checkPassword(password: str, hashed: bytes) -> bool:
        """_summary_

        Args:
            password (str): _description_
            hashed (bytes): _description_

        Returns:
            bool: _description_
        """
        return bcrypt.checkpw(password.encode('utf-8'), hashed)

    def auth(self, email: str, password: str) -> bool:
        """_summary_

        Args:
            email (str): _description_
            password (str): _description_

        Raises:
            ValueError: _description_
            ValueError: _description_
            ValueError: _description_
            ValueError: _description_

        Returns:
            bool: _description_
        """
        try:
            if not self.validateEmail(email):
                raise ValueError("Email inválido.")
            if email != self.__email:
                raise ValueError("Email não encontrado.")
            if not self.checkPassword(password, self.__password):
                raise ValueError("password incorreta.")
            if self.__status != Status.ACTIVE:
                raise ValueError("Conta inativa.")
            return True
        except ValueError as e:
            print(f"Erro na autenticação para {email}: {str(e)}")
            return False
        except Exception as e:
            print(f"Erro inesperado na autenticação para {email}: {str(e)}")
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
                print("O nome não pode ser vazio.")
                return
            if birth and birth >= date.today():
                print("A data de nascimento deve ser no passado.")
                return
            if email and not self.validateEmail(email):
                print("Email inválido.")
                return
            if password and not self.validatePassword(password):
                print("A senha deve ter pelo menos 8 caracteres, incluindo letras e números.")
                return
            self.__name = name if name else self.__name
            self.__birth = birth if birth else self.__birth
            self.__email = email if email else self.__email
            self.__password = self.hashPassword(password) if password else self.__password
        except Exception as e:
            print(f"Erro inesperado ao atualizar perfil para {self.__email}: {str(e)}")

    def deleteAccount(self) -> bool:
        """_summary_

        Raises:
            ValueError: _description_
        """
        try:
            if self.__status == Status.DELETED:
                print("Conta já excluída.")
                return False
            self.__status = Status.DELETED
            print(f"Conta {self.__email} excluída com sucesso.")
            return True
        except Exception as e:
            print(f"Erro inesperado ao excluir conta {self.__email}: {str(e)}")
    
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
            if not self.validateEmail(email):
                raise ValueError("Email inválido.")
            if not self.validateCPF(cpf):
                raise ValueError("CPF inválido.")
            if email != self.__email or cpf != self.__cpf:
                raise ValueError("Email ou CPF não correspondem.")
            # Simula envio de link de recuperação (implementação real teria que enviar um email)
            print(f"Link de recuperação de password enviado para {email}")
            return True
        except ValueError as e:
            print(f"Erro na recuperação de password para {email}: {str(e)}")
            return False
        except Exception as e:
            print(f"Erro inesperado na recuperação de password para {email}: {str(e)}")
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

