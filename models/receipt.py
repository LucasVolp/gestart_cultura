from uuid import UUID
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.purchase import Purchase


class Receipt:
    def __init__(self, id: UUID, date: str, quantity: int, description: str, purchase: "Purchase") -> None:
        self.__id = id
        self.__date = date
        self.__quantity = quantity
        self.__description = description
        self.__purchase = purchase

    def __str__(self):
        tipo = self.__class__.__name__
        return f"[{tipo}] ID: {self.__id} | Data: {self.__date} | Quantidade: {self.__quantity} | Descrição: {self.__description} | Compra: {self.__purchase}"
    
    @property
    def id(self):
        return self.__id
    
    @property
    def date(self):
        return self.__date
    
    @date.setter
    def date(self, value):
        self.__date = value

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, value):
        self.__quantity = value

    @property
    def description(self):
        return self.__description
    
    @description.setter
    def description(self, value):
        self.__description = value

    @property
    def purchase(self):
        return self.__purchase
    
    @purchase.setter
    def _purchase(self, value):
        self.__purchase = value
