from uuid import uuid4
from models.person import Person
from models.event import Event
from enums.typeEvent import TypeEvent
from enums.status import Status
from datetime import date

class Producer(Person):
    def __init__(self, id, name, cpf, birth, email, password, phone, status, cnpj:str, enterprise):
      super().__init__(id, name, cpf, birth, email, password, phone, status)
      self.__cnpj = cnpj
      self.__enterprise = enterprise
      self.events = []

    @property
    def _cnpj(self):
        return self.__cnpj

    @_cnpj.setter
    def _cnpj(self, value):
        self.__cnpj = value

    @property
    def _enterprise(self):
        return self.__enterprise

    @_enterprise.setter
    def _enterprise(self, value):
        self.__enterprise = value

    def __str__(self):
        tipo = self.__class__.__name__
        return f"[{tipo}] Nome: {self.__name} | Email: {self.__email} | CNPJ: {self.__cnpj} | Empresa: {self.__enterprise}"

    def createEvent(self, name:str, description:str, date:date, local:str, size:int, typeEvent: TypeEvent, status: Status) -> Event:
        event_id = uuid4()
        event = Event(event_id, name, description, date, local, size, typeEvent, status)
        self.events.append(event)
        return event

    def updateEvent(self, event:Event, name:str, description:str, date:date, local:str, size:int, typeEvent: TypeEvent) -> None:
        event._name = name
        event._description = description
        event._date = date
        event._local = local
        event._size = size
        event._typeEvent = typeEvent

    def deleteEvent(self, event:Event) -> None:
        if event in self.events:
            self.events.remove(event)

    def getEvent(self) -> list[Event]:
        return list(self.events)