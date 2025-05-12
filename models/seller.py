from models.person import Person
from models.purchase import Purchase
from models.purchaseItems import PurchaseItems
from enums.paymentStatus import PaymentStatus
from datetime import datetime
from uuid import uuid4

from models.ticket import Ticket

class Seller(Person):
    sellers = []

    def __init__(self, id: str, name: str, cpf: str, birth: str, email: str, password: str, phone: str, status: str):
        super().__init__(id, name, cpf, birth, email, password, phone, status)
        self.purchases = []

    def createPurchase(self, tier, amount, user, paymentMethod):
        item = PurchaseItems(id=uuid4(), tier=tier, quantity=amount, unitPrice=tier._price, totalPrice=tier._price*amount)
        purchase = Purchase(id=uuid4(), buyer=user, purchaseDate=datetime.now(), status=PaymentStatus.PENDING, totalPrice=item._totalPrice, paymentMethod=paymentMethod, items=[item])
        self.purchases.append(purchase)
        user.addPurchase(purchase)
        return purchase
    
    @classmethod
    def getSellers(cls):
        return list(cls.sellers)
    
    def getPurchases(self):
        return list(self.purchases)


