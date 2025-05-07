from person import Person
from enum import Enum

class TypeEvent(Enum):
    FESTIVAL_MUSICA = "Festival de Música"
    EXPO_ARTE = "Exposicao de Arte"
    TEATRO = "Teatro"
    FESTIVAL_CINEMA = "Festival de Cinema"
    ARTESANATO = "Artesanato"
    RODA_CONVERSA = "Roda de Conversa"
    MUSEU = "Museu"
    FOLCLORE = "Folclore"
    ONLINE = "Evento Online"
    PRESENCIAL = "Evento Presencial"


class Producer(Person):
    def __init__(self, id, name, cpf, birth, email, password, phone, status, cnpj:str, enterprise):
      super().__init__(id, name, cpf, birth, email, password, phone, status)
      self.__cnpj = cnpj
      self.__enterprise = enterprise

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

#def createEvent(self, name:str, description:str, date:date, local:str, size:int, typeEvent: Enum) -> Event:
    pass

#def updateEvent(event:Event, name:str, description:str, date:date, local:str, size:int, typeEvent: Enum) -> None:
    pass

#def deleteEvent(event:Event) -> None:
    pass

#def getEvent() -> list[Event]:
    pass