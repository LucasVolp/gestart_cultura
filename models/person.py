from uuid import UUID
from datetime import date
from abc import ABC, abstractmethod
from enums.status import Status

class Authenticable(ABC):
    @abstractmethod
    def auth(self, email: str, senha: str) -> bool:
        pass

    @abstractmethod
    def updateProfile(self, name: str, birth: date, email: str, password: str) -> None:
        pass

    @abstractmethod
    def recoverPassword(self, email: str, cpf: str) -> bool:
        pass

class Notifications(ABC):
    @abstractmethod
    def sendNotification(self, recipient: str, message: str) -> None:
        pass

    @abstractmethod
    def scheduleNotification(self, recipient: str, message: str, datetime: date) -> None:
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

    @property
    def _cpf(self):
        return self.__cpf

    @_cpf.setter
    def _cpf(self, value):
        self.__cpf = value

    @property
    def _birth(self):
        return self.__birth

    @_birth.setter
    def _birth(self, value):
        self.__birth = value

    @property
    def _email(self):
        return self.__email

    @_email.setter
    def _email(self, value):
        self.__email = value

    @property
    def _password(self):
        return self.__password

    @_password.setter
    def _password(self, value):
        self.__password = value

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value

    @property
    def _status(self):
        return self.__status

    @_status.setter
    def _status(self, value):
        self.__status = value

