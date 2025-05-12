from uuid import UUID, uuid4
from models.receipt import Receipt
from models.user import User
from enums.paymentStatus import PaymentStatus
from models.ticket import Ticket
from enums.status import Status
from models.event import Event
from models.tier import Tier
from models.purchaseItems import PurchaseItems

class Purchase:
    def __init__(self, id: UUID, buyer: User, purchaseDate: str, status: PaymentStatus, totalPrice: float, paymentMethod: str, items: list = None) -> None:
        self.__id = id
        self.__buyer = buyer
        self.__purchaseDate = purchaseDate
        self.__status = status
        self.__totalPrice = totalPrice
        self.__paymentMethod = paymentMethod
        self.__items = items if items is not None else []

    def __str__(self):
        tipo = self.__class__.__name__
        return f"[{tipo}] ID: {self.__id} | Comprador: {self.__buyer} | Data da Compra: {self.__purchaseDate} | Status: {self.__status.name} | Preço Total: {self.__totalPrice} | Método de Pagamento: {self.__paymentMethod}"
    
    @property
    def _id(self):
        return self.__id
    
    @property
    def _buyer(self):
        return self.__buyer
    
    @_buyer.setter
    def _buyer(self, value):
        self.__buyer = value

    @property
    def _purchaseDate(self):
        return self.__purchaseDate
    
    @_purchaseDate.setter
    def _purchaseDate(self, value):
        self.__purchaseDate = value

    @property
    def _status(self):
        return self.__status
    
    @_status.setter
    def _status(self, value):
        self.__status = value

    @property
    def _totalPrice(self):
        return self.__totalPrice
    
    @_totalPrice.setter
    def _totalPrice(self, value):
        self.__totalPrice = value

    @property
    def _paymentMethod(self):
        return self.__paymentMethod
    
    @_paymentMethod.setter
    def _paymentMethod(self, value):
        self.__paymentMethod = value

    @property
    def _receipt(self):
        return self.__receipt

    @property
    def _items(self):
        return self.__items
    
    @_items.setter
    def _items(self, value):
        self.__items = value

    def confirmPayment(self):
        if self.__status == PaymentStatus.PAID:
            for item in self.__items:
                tier = item._tier
                event = tier._event if hasattr(tier, '_event') else None
                for _ in range(item._quantity):
                    ticket = Ticket(
                        id=uuid4(),
                        owner=self.__buyer,
                        tier=tier,
                        event=event,
                        status=Status.VALID,
                        code=str(uuid4())
                    )
                    receipt = self.generateReceipt()
                    self.__buyer.addTicket(ticket)
                    self.__buyer.addReceipt(receipt)
                    item._tier.addTicket(ticket)
            self.__buyer.addPurchase(self)
        
    def generateReceipt(self):
        if self.__status == PaymentStatus.PAID:
            receipt = Receipt(id=uuid4(), purchase=self, date=self.__purchaseDate, quantity=self.__totalPrice, description="Receipt for purchase")
            return receipt
        else:
            raise ValueError("Cannot generate a receipt for a purchase that is not paid.")