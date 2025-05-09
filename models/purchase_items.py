from uuid import UUID, uuid4
from enum import Enum

class PurchaseItemStatus(Enum):
    AVAILABLE = "Disponível"
    PENDING = "Pendente"
    CANCELLED = "Cancelado"

class PurchaseItems:
    def __init__(self, purchase, tier, amount: int, unit_price: float, status: PurchaseItemStatus):
        self.__id: UUID = uuid4()
        self.__purchase = purchase      
        self.__tier = tier              
        self.__amount = amount
        self.__unit_price = unit_price
        self.__status = status
        

    @property
    def id(self) -> UUID:
        return self.__id

    @id.setter
    def id(self, value: UUID):
        self.__id = value

    @property
    def purchase(self):
        return self.__purchase

    @purchase.setter
    def purchase(self, value):
        self.__purchase = value

    @property
    def tier(self):
        return self.__tier

    @tier.setter
    def tier(self, value):
        self.__tier = value

    @property
    def amount(self) -> int:
        return self.__amount

    @amount.setter
    def amount(self, value: int):
        self.__amount = value

    @property
    def unit_price(self) -> float:
        return self.__unit_price

    @unit_price.setter
    def unit_price(self, value: float):
        self.__unit_price = value

    @property
    def status(self) -> PurchaseItemStatus:
        return self.__status

    @status.setter
    def status(self, value: PurchaseItemStatus):
        self.__status = value

    
    
    def calculate_total_price(self) -> float:
        return self.__amount * self.__unit_price

    def associate_purchase(self, purchase):
        self.__purchase = purchase