from uuid import UUID, uuid4
from models.receipt import Receipt
from models.ticket import Ticket
from enums.paymentStatus import PaymentStatus
from enums.paymentMethods import PaymentMethods
from enums.status import Status
from typing import TYPE_CHECKING, Tuple, List

if TYPE_CHECKING:
    from models.user import User
    from models.seller import Seller

class Purchase:
    def __init__(self, id: UUID, buyer: "User", seller: "Seller", purchaseDate: str, status: PaymentStatus, totalPrice: float, paymentMethod: PaymentMethods, items: list = None) -> None:
        self.__id = id
        self.__buyer = buyer
        self.__seller = seller
        self.__purchaseDate = purchaseDate
        self.__status = status
        self.__totalPrice = totalPrice
        self.__paymentMethod = paymentMethod
        self.__items = items if items is not None else []

    def __str__(self):
        tipo = self.__class__.__name__
        seller = self.__seller.name
        return f"[{tipo}] ID: {self.__id} | Comprador: {self.__buyer} | Vendedor: {seller} | Data da Compra: {self.__purchaseDate} | Status: {self.__status.name} | Preço Total: {self.__totalPrice} | Método de Pagamento: {self.__paymentMethod.name}"
    
    @property
    def id(self):
        return self.__id
    
    @property
    def buyer(self):
        return self.__buyer
    
    @buyer.setter
    def buyer(self, value):
        self.__buyer = value

    @property
    def seller(self):
        return self.__seller
    
    @seller.setter
    def seller(self, value):
        self.__seller = value

    @property
    def purchaseDate(self):
        return self.__purchaseDate
    
    @purchaseDate.setter
    def purchaseDate(self, value):
        self.__purchaseDate = value

    @property
    def status(self):
        return self.__status
    
    @status.setter
    def status(self, value):
        self.__status = value

    @property
    def totalPrice(self):
        return self.__totalPrice
    
    @totalPrice.setter
    def totalPrice(self, value):
        self.__totalPrice = value

    @property
    def paymentMethod(self):
        return self.__paymentMethod
    
    @paymentMethod.setter
    def paymentMethod(self, value):
        self.__paymentMethod = value

    @property
    def receipt(self):
        return self.__receipt

    @property
    def items(self):
        return self.__items
    
    @items.setter
    def items(self, value):
        self.__items = value

    def confirmPayment(self) -> Tuple[List[Ticket], Receipt]:
        """_summary_

        Raises:
            ValueError: _description_
            ValueError: _description_

        Returns:
            Tuple[List[Ticket], Receipt]: _description_
        """
        try:
            if self.__status != PaymentStatus.PAID:
                raise ValueError("Pagamento não está no status PAID")
            tickets = []
            for item in self.__items:
                tier = item.tier
                if tier.getDisponibility() < item.quantity:
                    raise ValueError(f"Não há ingressos suficientes no tier {tier.name}")
                for _ in range(item.quantity):
                    ticket = Ticket(
                        id=uuid4(),
                        owner=self.__buyer,
                        tier=tier,
                        event=tier.event if hasattr(tier, 'event') else None,
                        seller=self.__seller,
                        status=Status.VALID,
                        code=str(uuid4())
                    )
                    tickets.append(ticket)
                    tier.addTicket(ticket)
            receipt = self.generateReceipt()
            return tickets, receipt
        except ValueError as e:
            print(f"Erro ao confirmar pagamento {self.__id}: {str(e)}")
            raise
        except Exception as e:
            print(f"Erro inesperado ao confirmar pagamento {self.__id}: {str(e)}")
            raise
    
    def generateReceipt(self) -> Receipt:
        """_summary_

        Raises:
            ValueError: _description_

        Returns:
            Receipt: _description_
        """
        try:
            if self.__status != PaymentStatus.PAID:
                raise ValueError("Pagamento não está no status PAID")
            return Receipt(id=uuid4(), purchase=self, date=self.__purchaseDate, quantity=self.__totalPrice, description="Receipt for purchase")
        except ValueError as e:
            print(f"Erro ao gerar recibo para a compra {self.__id}: {str(e)}")
            raise
        except Exception as e:
            print(f"Erro inesperado ao gerar recibo para a compra {self.__id}: {str(e)}")
            raise