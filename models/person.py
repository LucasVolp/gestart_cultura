from uuid import UUID, uuid4
from datetime import date
from enum import Enum
from abc import ABC, abstractmethod

# class Authenticable(ABC):
#     @abstractmethod
#     def auth(self, email: str, senha: str) -> bool:
#         pass

#     @abstractmethod
#     def updateProfile(self, name: str, birth: date, email: str, password: str) -> None:
#         pass

#     @abstractmethod
#     def recoverPassword(self, email: str, cpf: str) -> bool:
#         pass

# class Notifications(ABC):
#     @abstractmethod
#     def sendNotification(self, recipient: str, message: str) -> None:
#         pass

#     @abstractmethod
#     def scheduleNotification(self, recipient: str, message: str, datetime: date) -> None:
#         pass

class Status(Enum):
    ACTIVE = "Ativo"
    INACTIVE = "Inativo"
    DELETED = "Deletado"

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


    def auth(self, email: str, senha: str) -> bool:
        raise NotImplementedError("auth method not implemented")

    def updateProfile(self, name: str, birth: date, email: str, password: str) -> None:
        raise NotImplementedError("updateProfile method not implemented")

    def recoverPassword(self, email: str, cpf: str) -> bool:
        raise NotImplementedError("recoverPassword method not implemented")

    def sendNotification(self, recipient: str, message: str) -> None:
        raise NotImplementedError("sendNotification method not implemented")

    def scheduleNotification(self, recipient: str, message: str, datetime: date) -> None:
        raise NotImplementedError("scheduleNotification method not implemented")
