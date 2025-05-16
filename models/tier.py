import logging
from uuid import UUID
from enums.status import Status

class Tier:
    def __init__(self, id: UUID, amount: int, name: str, price: float, startDate: str, endDate: str, status: str, tickets: list = None) -> None:
        self.__id = id
        self.__amount = amount
        self.__name = name
        self.__price = price
        self.__startDate = startDate
        self.__endDate = endDate
        self.__status = status
        self.__tickets = tickets if tickets is not None else []

    def __str__(self):
        tipo = self.__class__.__name__
        status = self.__status.name
        return f"[{tipo}] Nome: {self.__name} | Preço: {self.__price} | Início: {self.__startDate} | Fim: {self.__endDate} | Status: {status} | Ingressos: {self.__tickets} | Disponibilidade: {self.getDisponibility()}"

    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def amount(self):
        return self.__amount
    
    @amount.setter
    def amount(self, value):
        self.__amount = value

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, value):
        self.__price = value

    @property
    def startDate(self):
        return self.__startDate
    
    @startDate.setter
    def startDate(self, value):
        self.__startDate = value

    @property
    def endDate(self):
        return self.__endDate
    
    @endDate.setter
    def endDate(self, value):
        self.__endDate = value

    @property
    def status(self):
        return self.__status
    
    @status.setter
    def status(self, value):
        self.__status = value

    
    def openTier(self) -> bool:
        if self.__status == Status.CLOSED or self.getDisponibility() <= 0:
            print("Não é possível abrir um tier que já está fechado ou sem ingressos disponíveis.")
            return False
        self.__status = Status.OPEN
        return True

    def closeTier(self) -> bool:
        if self.__status == Status.CLOSED:
            print("Não é possível fechar um tier que já está fechado.")
            return False
        self.__status = Status.CLOSED
        return True

    def getDisponibility(self) -> int:
        return self.__amount - len(self.__tickets)

    def addTicket(self, ticket) -> bool:
        if self.__status != Status.OPEN:
            print("Não é possível adicionar ingressos a um tier fechado.")
            return False
        if self.getDisponibility() <= 0:
            print("Não há ingressos disponíveis neste tier.")
            return False
        self.__tickets.append(ticket)
        return True