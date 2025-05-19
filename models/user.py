from datetime import date, datetime
from enums.paymentStatus import PaymentStatus
from models.person import Person
from models.rating import Rating
from models.ticket import Ticket
from enums.typeEvent import TypeEvent
from enums.status import Status
from uuid import UUID, uuid4
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.purchase import Purchase

class User(Person):
    users = []

    def __init__(self, id: UUID, name: str, cpf: str, birth: str, email: str, password: str, phone: str, status: Status, balance: float, tickets: list = None, ratings: list = None, purchases: list = None, receipts: list = None):
        super().__init__(id, name, cpf, birth, email, password, phone, status)
        self.__balance = balance
        self.__tickets = []
        self.__ratings = []
        self.__purchases = []
        self.__receipts = []

    @property
    def balance(self):
        return self.__balance

    @property
    def id(self):
        return self._Person__id
    
    @property
    def _id(self):
        return self._Person__id

    def getUserbyEmail(cls, email):
        """_summary_

        Args:
            cls (_type_): _description_
            email (_type_): _description_

        Returns:
            _type_: _description_
        """
        try:
            for user in cls.users:
                if user.email == email:
                    return user
            return None
        except Exception as e:
            print(f"Erro inesperado ao buscar usuário por email: {str(e)}")
            raise

    def sendNotification(self, recipient: str, message: str) -> None:
        try:
            if not self._validate_email(recipient):
                print("Email inválido.")
                return
            # Simula envio de email
            print(f"Notificação enviada para {recipient}: {message}")
        except Exception as e:
            print(f"Erro inesperado ao enviar notificação para {recipient}: {str(e)}")

    def scheduleNotification(self, recipient: str, message: str, datetime: date) -> None:
        try:
            if not self._validate_email(recipient):
                print("Email inválido.")
                return
            if datetime < date.today():
                print("A data de agendamento deve ser futura.")
                return
            # Simula agendamento de email
            print(f"Notificação agendada para {recipient} em {datetime}: {message}")
        except Exception as e:
            print(f"Erro inesperado ao agendar notificação para {recipient}: {str(e)}")

    @classmethod
    def getUsers(cls):
        """_summary_

        Raises:
            ValueError: _description_

        Returns:
            _type_: _description_
        """
        try:
            if not cls.users:
                raise ValueError("Nenhum usuário encontrado.")
            return list(cls.users)
        except ValueError as e:
            print(f"Erro ao obter usuários: {str(e)}")
            raise
        except Exception as e:
            print(f"Erro inesperado ao obter usuários: {str(e)}")
            raise
    
    def getTickets(self):
        """_summary_

        Raises:
            ValueError: _description_

        Returns:
            _type_: _description_
        """
        #try:
        if not self.__tickets:
          raise ValueError("Nenhum ticket encontrado.")
        return list(self.__tickets)
        # except ValueError as e:
        #     print(f"Erro ao obter tickets: {str(e)}")
        #     raise
        # except Exception as e:
        #     print(f"Erro inesperado ao obter tickets: {str(e)}")
        #     raise
    
    def getRatings(self):
        """_summary_

        Raises:
            ValueError: _description_

        Returns:
            _type_: _description_
        """
        
        if not self.__ratings:
         raise ValueError("Nenhuma avaliação encontrada.")
        return list(self.__ratings)
       
    
    def getPurchases(self):
        """_summary_

        Raises:
            ValueError: _description_

        Returns:
            _type_: _description_
        """
        try:
            if not self.__purchases:
                raise ValueError("Nenhuma compra encontrada.")
            return list(self.__purchases)
        except ValueError as e:
            print(f"Erro ao obter compras: {str(e)}")
            raise
        except Exception as e:
            print(f"Erro inesperado ao obter compras: {str(e)}")
            raise

    def addTicket(self, ticket):
        """_summary_

        Args:
            ticket (_type_): _description_

        Raises:
            ValueError: _description_
        """
        try:
            if ticket not in self.__tickets:
                self.__tickets.append(ticket)
            else:
                print("Ticket já registrado.")
        except Exception as e:
            print(f"Erro inesperado ao adicionar ticket para o usuário {self._id}: {str(e)}")

    def buyTicket(self, tier, quantity, seller, paymentMethod):
        try:
            if hasattr(tier, 'event') and getattr(tier, 'event') and getattr(tier, 'event').typeEvent == TypeEvent.FREE_EVENT:
                return self.registerInFreeEvent(tier)
            purchase = seller.createPurchase(tier, quantity, self, paymentMethod)
            return purchase
        except ValueError as e:
            print(f"Erro ao comprar ingresso: {str(e)}")
            return None
        except Exception as e:
            print(f"Erro inesperado ao comprar ingresso: {str(e)}")
            return None
    
    def transferTicket(self, ticket: Ticket, newCPF: str) -> None:
        try:
            if hasattr(ticket, 'tier') and hasattr(ticket.tier, 'event') and ticket.tier.event.typeEvent == TypeEvent.FREE_EVENT:
                print("Não é possível transferir ingressos de eventos gratuitos.")
                return
            if ticket not in self.__tickets:
                print("O ticket não pertence a este usuário.")
                return
            if ticket._status != Status.VALID:
                print("O ticket não está válido para transferência.")
                return
            if hasattr(ticket, 'tier') and hasattr(ticket.tier, 'event') and ticket.tier.event.status == Status.CLOSED:
                print("O evento já foi encerrado, não é possível transferir o ingresso.")
                return
            new_owner = None
            for user in User.users:
                if user._cpf == newCPF:
                    new_owner = user
                    break
            if not new_owner:
                print("Novo usuário com o CPF informado não encontrado.")
                return
            self.__tickets.remove(ticket)
            new_owner.addTicket(ticket)
            ticket.owner = new_owner
        except Exception as e:
            print(f"Erro inesperado ao transferir ticket: {str(e)}")

    def registerInFreeEvent(self, event):
        """_summary_

        Args:
            tier (_type_): _description_

        Raises:
            ValueError: _description_
            ValueError: _description_
            ValueError: _description_

        Returns:
            _type_: _description_
        """
        try:
            if event.typeEvent != TypeEvent.FREE_EVENT:
                print("O evento não é gratuito.")
                return None
            if event.size <= 0:
                print("Não há ingressos disponíveis para o evento.")
                return None
            if event.status == Status.CLOSED:
                print("O evento já foi encerrado, não é possível registrar-se.")
                return None
            ticket = Ticket(id=uuid4(), owner=self, tier=None, event=event, status=Status.VALID, code=str(uuid4()))
            self.addTicket(ticket)
            return ticket
        except Exception as e:
            print(f"Erro inesperado ao registrar no evento gratuito para o usuário {self._id}: {str(e)}")
            return None
    
    def createRating(self, event, rate: int, comment: str) -> Rating:
        """_summary_

        Args:
            event (_type_): _description_
            rate (int): _description_
            comment (str): _description_

        Raises:
            ValueError: _description_
            ValueError: _description_

        Returns:
            Rating: _description_
        """
        try:
            if not any(ticket.event == event for ticket in self.__tickets):
                print("O usuário não pode avaliar o evento.")
                return None
            if event.status == Status.CLOSED:
                rating = Rating(id=uuid4(), user=self, event=event, rate=rate, comment=comment)
                self.__ratings.append(rating)
                event.addRating(rating)
                return rating
            else:
                print("O evento não está encerrado, não é possível avaliar.")
                return None
        except Exception as e:
            print(f"Erro inesperado ao criar rating para o usuário {self._id}: {str(e)}")
            return None

    def updateRating(self, rating: Rating, rate: int, comment: str) -> None:
        """_summary_

        Args:
            rating (Rating): _description_
            rate (int): _description_
            comment (str): _description_

        Raises:
            ValueError: _description_
            ValueError: _description_
        """
        try:
            if rating not in self.__ratings:
                print("O rating não pertence a este usuário.")
                return
            if rating.event.status != Status.CLOSED:
                print("O evento não está encerrado, não é possível atualizar a avaliação.")
                return
            rating.rate = rate if 0 <= rate <= 5 else rating.rate
            rating.comment = comment if comment else rating.comment
        except Exception as e:
            print(f"Erro inesperado ao atualizar rating para o usuário {self.__name}: {str(e)}")

    def deleteRating(self, rating: Rating) -> None:
        """_summary_

        Args:
            rating (Rating): _description_

        Raises:
            ValueError: _description_
        """
        try:
            if rating not in self.__ratings:
                print("O rating não pertence a este usuário.")
                return
            self.__ratings.remove(rating)
        except Exception as e:
            print(f"Erro inesperado ao deletar rating para o usuário {self.__name}: {str(e)}")

    def payPurchase(self, purchase: "Purchase") -> None:
        """_summary_

        Args:
            purchase (Purchase): _description_

        Raises:
            ValueError: _description_
            ValueError: _description_
        """
        try:
            if purchase not in self.__purchases:
                print("Compra não pertence a este usuário.")
                return
            if purchase._status == PaymentStatus.PAID:
                print("A compra já foi paga.")
                return
            if purchase._status == PaymentStatus.PENDING and self.__balance >= purchase._totalPrice:
                self.__balance -= purchase._totalPrice
                purchase._status = PaymentStatus.PAID
                tickets, receipt = purchase.confirmPayment()
                for ticket in tickets:
                    self.addTicket(ticket)
                self.addReceipt(receipt)
                self.addPurchase(purchase)
        except Exception as e:
            print(f"Erro inesperado ao pagar compra: {str(e)}")
    
    def addPurchase(self, purchase: "Purchase") -> None:
        """_summary_

        Args:
            purchase (Purchase): _description_

        Raises:
            ValueError: _description_
            ValueError: _description_
        """
        try:
            if purchase in self.__purchases:
                print("Compra já registrada.")
                return
            if purchase not in self.__purchases:
                self.__purchases.append(purchase)
        except Exception as e:
            print(f"Erro inesperado ao adicionar compra para o usuário {self._id}: {str(e)}")

    def refundPurchase(self, purchase):
        """_summary_

        Args:
            purchase (_type_): _description_

        Raises:
            ValueError: _description_
            ValueError: _description_
            ValueError: _description_

        Returns:
            _type_: _description_
        """
        try:
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
        except ValueError as e:
            print(f"Erro ao solicitar reembolso para o usuário {self._id}: {str(e)}")
            return False
        except Exception as e:
            print(f"Erro inesperado ao solicitar reembolso para o usuário {self._id}: {str(e)}")
            return False
    
    def addReceipt(self, receipt):
        """_summary_

        Args:
            receipt (_type_): _description_

        Raises:
            ValueError: _description_
            ValueError: _description_
        """
        try:
            if receipt in self.__receipts:
                print("Recibo já registrado.")
                return
            if receipt not in self.__receipts:
                self.__receipts.append(receipt)
        except Exception as e:
            print(f"Erro inesperado ao adicionar recibo para o usuário {self._id}: {str(e)}")

