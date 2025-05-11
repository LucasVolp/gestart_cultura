from uuid import UUID
from models.user import User
from models.tier import Tier

class PurchaseItems:
    def __init__(self, id: UUID, tier: Tier, quantity: int, unitPrice: float, totalPrice: float) -> None:
        self.__id = id
        self.__tier = tier
        self.__quantity = quantity
        self.__unitPrice = unitPrice
        self.__totalPrice = totalPrice

    def __str__(self):
        tipo = self.__class__.__name__
        return f"[{tipo}] ID: {self.__id} | Tier: {self.__tier} | Quantidade: {self.__quantity} | Preço Unitário: {self.__unitPrice} | Preço Total: {self.__totalPrice}"
    
    @property
    def _id(self):
        return self.__id
    
    @property
    def _tier(self):
        return self.__tier
    
    @_tier.setter
    def _tier(self, value):
        self.__tier = value

    @property
    def _quantity(self):
        return self.__quantity
    
    @_quantity.setter
    def _quantity(self, value):
        self.__quantity = value
    
    @property
    def _unitPrice(self):
        return self.__unitPrice
    
    @property
    def _totalPrice(self):
        return self.__totalPrice