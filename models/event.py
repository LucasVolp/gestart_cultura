from datetime import date
import logging
from uuid import UUID, uuid4
from enums.status import Status
from enums.typeEvent import TypeEvent
from models.tier import Tier
from models.rating import Rating


class Event():
    events = []

    def __init__(self, id: UUID, name: str, description: str, date: str, local: str, size: int, typeEvent: TypeEvent, status: Status, tiers: list = None, ratings: list = None, producers: list = None) -> None:
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
        self.__producers = producers if producers else []
        Event.events.append(self)


    def __str__(self):
        tipo = self.__class__.__name__
        typeEvent = self.__typeEvent.name
        status = self.__status.name
        tiers = [tier.name for tier in self.__tiers]
        ratings = [f"{rating.user.name if hasattr(rating.user, 'name') else ''}: {rating.rate}" for rating in self.__ratings]
        return f"[{tipo}] Nome: {self.__name} | Descrição: {self.__description} | Data: {self.__date} | Local: {self.__local} | Tamanho: {self.__size} | Lotes: {tiers} | Avaliações: {ratings} | Tipo de Evento: {typeEvent} | Status: {status}"

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def description(self):
        return self.__description
    
    @description.setter
    def description(self, value):
        self.__description = value

    @property
    def date(self):
        return self.__date
    
    @date.setter
    def date(self, value):
        self.__date = value

    @property
    def local(self):
        return self.__local
    
    @local.setter
    def local(self, value):
        self.__local = value

    @property
    def size(self):
        return self.__size
    
    @size.setter
    def size(self, value):
        self.__size = value

    @property
    def tiers(self):
        return self.__tiers
    
    @property
    def ratings(self):
        return self.__ratings
    
    @property
    def status(self):
        return self.__status
    
    @status.setter
    def status(self, value):
        self.__status = value

    @property
    def typeEvent(self):
        return self.__typeEvent
    
    @typeEvent.setter
    def typeEvent(self, value):
        self.__typeEvent = value

    
    def addProducer(self, producer):
        try:
            if producer not in self.__producers:
                self.__producers.append(producer)
            else:
                raise ValueError("O produtor já está associado a este evento.")
        except ValueError as e:
            raise

    def removeProducer(self, producer):
        try:
            if producer in self.__producers:
                self.__producers.remove(producer)
            else:
                raise ValueError("O produtor não está associado a este evento.")
        except ValueError as e:
            raise

    def getProducers(self):
        return list(self.__producers)


    def getTiers(self):
        if not self.__tiers:
            print("Nenhum tier encontrado.")
            return []
        return list(self.__tiers)

    def getRatings(self):
        if not self.__ratings:
            print("Nenhuma avaliação encontrada.")
            return []
        return list(self.__ratings)

    def createTier(self, amount: int, name: str, price: float, startDate: str, endDate: str, status: Status) -> Tier:
        if self.__status != Status.OPEN:
            print("Não é possível criar tiers para um evento que não está aberto.")
            return None
        totalTickets = sum(tier.amount for tier in self.__tiers)
        if totalTickets + amount > self.__size:
            print("A quantidade de ingressos no tier excede o tamanho do evento.")
            return None
        if price < 0:
            print("O preço não pode ser negativo.")
            return None
        if startDate >= endDate:
            print("A data de início deve ser anterior à data de término.")
            return None
        tier = Tier(id=uuid4(), amount=amount, name=name, price=price, startDate=startDate, endDate=endDate, status=status)
        self.addTier(tier)
        return tier

    def updateTier(self, tier: Tier, amount: int = None, name: str = None, price: float = None, startDate: str = None, endDate: str = None, status: Status = None) -> Tier:
        if tier not in self.__tiers:
            print("O tier não pertence a este evento.")
            return None
        if amount and amount > self.__size:
            print("A quantidade de ingressos no tier excede o tamanho do evento.")
            return None
        if price and price < 0:
            print("O preço não pode ser negativo.")
            return None
        if startDate and endDate and startDate >= endDate:
            print("A data de início deve ser anterior à data de término.")
            return None
        if status and status not in [Status.OPEN, Status.CLOSED]:
            print("Status inválido. Deve ser OPEN ou CLOSED.")
            return None
        tier.amount = amount if amount is not None else tier.amount
        tier.name = name if name else tier.name
        tier.price = price if price is not None else tier.price
        tier.startDate = startDate if startDate else tier.startDate
        tier.endDate = endDate if endDate else tier.endDate
        tier.status = status if status else tier.status
        return tier

    def deleteTier(self, tier: Tier) -> bool:
        if tier not in self.__tiers:
            print("O tier não pertence a este evento.")
            return False
        if tier.getDisponibility() < tier.amount:
            print("Não é possível excluir um tier com ingressos já emitidos.")
            return False
        self.removeTier(tier)
        return True

    def getRatings(self):
        if not self.__ratings:
            print("Nenhuma avaliação encontrada.")
            return []
        return list(self.__ratings)

    def addRating(self, rating: Rating) -> None:
        if rating in self.__ratings:
            print("A avaliação já existe.")
            return
        self.__ratings.append(rating)

    def deleteRating(self, rating: Rating) -> bool:
        if rating not in self.__ratings:
            print("A avaliação não pertence a este evento.")
            return False
        self.__ratings.remove(rating)
        return True

    def availability(self) -> Status:
        return self.__status

    def addTier(self, tier: Tier):
        if tier not in self.__tiers:
            self.__tiers.append(tier)

    def removeTier(self, tier: Tier):
        if tier in self.__tiers:
            self.__tiers.remove(tier)

    def addRating(self, rating: Rating):
        if rating not in self.__ratings:
            self.__ratings.append(rating)

    def removeRating(self, rating: Rating):
        if rating in self.__ratings:
            self.__ratings.remove(rating)

