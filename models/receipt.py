from uuid import UUID
from datetime import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.purchase import Purchase


class Receipt:
    def __init__(self, id: UUID, date: datetime, quantity: float, description: str, purchase: 'Purchase') -> None:
        self.__id = id
        self.__date = date
        self.__quantity = quantity
        self.__description = description
        self.__purchase = purchase

    def __str__(self):
        tipo = self.__class__.__name__
        return f"[{tipo}] ID: {self.__id} | Data: {self.__date} | Quantidade: {self.__quantity} | Descrição: {self.__description} | Compra: {self.__purchase}"
    
    @property
    def _id(self):
        return self.__id
    
    @property
    def _date(self):
        return self.__date
    
    @_date.setter
    def _date(self, value):
        self.__date = value

    @property
    def _quantity(self):
        return self.__quantity

    @_quantity.setter
    def _quantity(self, value):
        self.__quantity = value

    @property
    def _description(self):
        return self.__description
    
    @_description.setter
    def _description(self, value):
        self.__description = value

    @property
    def _purchase(self):
        return self.__purchase
    
    @_purchase.setter
    def _purchase(self, value):
        self.__purchase = value
