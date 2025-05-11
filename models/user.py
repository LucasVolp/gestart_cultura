from datetime import datetime
from models.person import Person
from models.purchase import Purchase
from models.purchaseItems import PurchaseItems
from models.rating import Rating
from models.ticket import Ticket
from enums.typeEvent import TypeEvent
from enums.status import Status
from uuid import uuid4

class User(Person):
    users = []

    def __init__(self, id: str, name: str, cpf: str, birth: str, email: str, password: str, phone: str, status: str, tickets: list = None, ratings: list = None, purchases: list = None, receipts: list = None):
        super().__init__(id, name, cpf, birth, email, password, phone, status)
        self.__tickets = []
        self.__ratings = []
        self.__purchases = []
        self.__receipts = []

    @classmethod
    def getUsers(cls):
        return list(cls.users)
    
    def getTickets(self):
        return list(self.__tickets)
    
    def getRatings(self):
        return list(self.__ratings)
    
    def getPurchases(self):
        return list(self.__purchases)

    def addTicket(self, ticket):
        self.__tickets.append(ticket)

    def buyTicket(self, tier, quantity, seller, paymentMethod):
        if tier._event._typeEvent == TypeEvent.FREE_EVENT:
            return self.registerInFreeEvent(tier)
        # O seller registra a venda
        purchase = seller.createPurchase(tier, quantity, self, paymentMethod)
        return purchase
    
    def transferTicket(self, ticket: Ticket, newCPF: str) -> None:
        if ticket not in self.__tickets:
            raise ValueError("O ticket não pertence a este usuário.")
        
        new_owner = None
        for user in User.users:
            if user._cpf == newCPF:
                new_owner = user
                break
        if not new_owner:
            raise ValueError("Novo usuário com o CPF informado não encontrado.")

        self.__tickets.remove(ticket)
        new_owner.addTicket(ticket)
        ticket.owner = new_owner

    def registerInFreeEvent(self, tier):
        # Cria um ticket gratuito e adiciona ao usuário
        ticket = Ticket(id=uuid4(), owner=self, tier=tier, event=tier._event, status=Status.VALID, code=str(uuid4()))
        self.addTicket(ticket)
        return ticket
    
    def createRating(self, event, rate: int, comment: str) -> None:
        # Check if the user has a ticket for the given event
        if not any(ticket.event == event for ticket in self.__tickets):
            raise ValueError("O usuário não pode avaliar o evento.")
        if event.status == Status.CLOSED:
            rating = Rating(id=uuid4(), user=self, event=event, rate=rate, comment=comment)
            self.__ratings.append(rating)
            event.addRating(rating)

    def updateRating(self, rating: Rating, rate: int, comment: str) -> None:
        if rating not in self.__ratings:
            raise ValueError("O rating não pertence a este usuário.")
        
        if rate is not None:
            rating.rate = rate
        if comment is not None:
            rating.comment = comment
    
    def payPurchase(self, purchase: Purchase) -> None:
        if purchase not in self.__purchases:
            raise ValueError("Compra não pertence a este usuário.")
        
        if purchase.status == Status.PAID:
            raise ValueError("A compra já foi paga.")
        
        elif purchase.status == Status.PENDING:
            purchase.status = Status.PAID
            purchase.confirmPayment()
    
    def addPurchase(self, purchase: Purchase) -> None:
        if purchase not in self.__purchases:
            self.__purchases.append(purchase)
        else:
            raise ValueError("Compra já registrada.")

    def refundPurchase(self, purchase):
        if purchase not in self.__purchases:
            raise ValueError("Compra não pertence a este usuário.")

        if (datetime.now() - purchase._purchaseDate).days > 7:
            raise ValueError("O prazo para reembolso expirou.")

        for item in purchase._items:
            event = item._tier._event
            if event.status == Status.CLOSED:
                raise ValueError("O evento já foi encerrado, não é possível reembolsar.")

        for item in purchase._items:
            ticket_to_remove = None
            for ticket in self.__tickets:
                if ticket.tier == item._tier:
                    ticket_to_remove = ticket
                    break
            if ticket_to_remove:
                self.__tickets.remove(ticket_to_remove)

        purchase.status = Status.REFUND
        return True
    
    def addReceipt(self, receipt):
        self.__receipts.append(receipt)

