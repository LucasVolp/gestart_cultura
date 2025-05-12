from uuid import uuid4, UUID
from enums.status import Status
from enums.typeEvent import TypeEvent
from models.tier import Tier
from models.rating import Rating


class Event():
    def __init__(self, id: UUID, name: str, description: str, date: str, local: str, size: int, typeEvent: TypeEvent, status: Status, tiers: list = None, ratings: list = None) -> None:
        self.__id = id
        self.__name = name
        self.__description = description
        self.__date = date
        self.__local = local
        self.__size = size
        self.__typeEvent = typeEvent
        self.__status = status
        self.__tiers = []
        self.__ratings = []

    def __str__(self):
        tipo = self.__class__.__name__
        typeEvent = self.__typeEvent.name
        status = self.__status.name
        return f"[{tipo}] Nome: {self.__name} | Descrição: {self.__description} | Data: {self.__date} | Local: {self.__local} | Tamanho: {self.__size} | Tipo de Evento: {typeEvent} | Status: {status}"

    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        self.__id = value

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


    def getTiers(self):
        return list(self.__tiers)
    
    def createTier(self, amount: int, nome: str, price: float, startDate: str, endDate: str, status: Status) -> Tier:
        tier_id = uuid4()
        tier = Tier(tier_id, amount, nome, price, startDate, endDate, status)
        self.__tiers.append(tier)
        return tier

    def updateTier(
        self,
        tier: Tier,
        amount: int = None,
        nome: str = None,
        price: float = None,
        startDate: str = None,
        endDate: str = None,
        status: Status = None
    ) -> None:
            if amount is not None:
                tier._amount = amount
            if nome is not None:
                tier._nome = nome
            if price is not None:
                tier._price = price
            if startDate is not None:
                tier._startDate = startDate
            if endDate is not None:
                tier._endDate = endDate
            if status is not None:
                tier._status = status
            return tier
    
    def deleteTier(self, tier: Tier) -> bool:
        if tier in self.__tiers:
            self.__tiers.remove(tier)
            return True
        return False

    def getRatings(self):
        return list(self.__ratings)
    
    def addRating(self, rating: Rating) -> None:
        self.__ratings.append(rating)

    def deleteRating(self, rating: Rating) -> bool:
        if rating in self.__ratings:
            self.__ratings.remove(rating)
            return True
        return False

    def availability(self) -> Status:
        return self.__status

        