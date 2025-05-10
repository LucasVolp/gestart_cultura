from uuid import UUID
from enums import TypeEvent


class Event():
    def __init__(self, id: UUID, name: str, description: str, date: str, local: str, size: int, typeEvent: TypeEvent, tiers: list = None):
        self.__id = id
        self.__name = name
        self.__description = description
        self.__date = date
        self.__local = local
        self.__size = size
        self.__typeEvent = typeEvent
        self.__tiers = []

    def __str__(self):
        tipo = self.__class__.__name__
        return f"[{tipo}] Nome: {self.__name} | Descrição: {self.__description} | Data: {self.__date} | Local: {self.__local} | Tamanho: {self.__size} | Tipo de Evento: {self.__typeEvent}"
    
    @property
    def _name(self):
        return self.__name
    
    @_name.setter
    def _name(self, value):
        self.__name = value

    @property
    def _description(self):
        return self.__description
    
    @_description.setter
    def _description(self, value):
        self.__description = value

    @property
    def _date(self):
        return self.__date
    
    @_date.setter
    def _date(self, value):
        self.__date = value

    @property
    def _local(self):
        return self.__local
    
    @_local.setter
    def _local(self, value):
        self.__local = value

    @property
    def _size(self):
        return self.__size
    
    @_size.setter
    def _size(self, value):
        self.__size = value

    @property
    def _typeEvent(self):
        return self.__typeEvent
    
    @_typeEvent.setter
    def _typeEvent(self, value):
        self.__typeEvent = value


    def getTickets(self):
        