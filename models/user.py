from datetime import date, datetime
import logging
from enums.paymentStatus import PaymentStatus
from models.person import Person
from models.rating import Rating
from models.ticket import Ticket
from enums.typeEvent import TypeEvent
from enums.status import Status
from uuid import uuid4
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.purchase import Purchase

class User(Person):
    users = []

    def __init__(self, id: str, name: str, cpf: str, birth: str, email: str, password: str, phone: str, status: str, tickets: list = None, ratings: list = None, purchases: list = None, receipts: list = None):
        super().__init__(id, name, cpf, birth, email, password, phone, status)
        self.__tickets = []
        self.__ratings = []
        self.__purchases = []
        self.__receipts = []

    def sendNotification(self, recipient: str, message: str) -> None:
        try:
            if not self._validate_email(recipient):
                raise ValueError("Destinatário inválido.")
            # Simula envio de email (implementação real usaria algum serviço de email)
            logging.info(f"Notificação enviada para {recipient}: {message}")
        except ValueError as e:
            logging.error(f"Erro ao enviar notificação para {recipient}: {str(e)}")
            raise
        except Exception as e:
            logging.error(f"Erro inesperado ao enviar notificação para {recipient}: {str(e)}")
            raise

    def scheduleNotification(self, recipient: str, message: str, datetime: date) -> None:
        try:
            if not self._validate_email(recipient):
                raise ValueError("Destinatário inválido.")
            if datetime < date.today():
                raise ValueError("A data de agendamento deve ser futura.")
            # Simula agendamento (implementação real usaria algum serviço de agendamento)
            logging.info(f"Notificação agendada para {recipient} em {datetime}: {message}")
        except ValueError as e:
            logging.error(f"Erro ao agendar notificação para {recipient}: {str(e)}")
            raise
        except Exception as e:
            logging.error(f"Erro inesperado ao agendar notificação para {recipient}: {str(e)}")
            raise

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
            logging.error(f"Erro ao obter usuários: {str(e)}")
            raise
        except Exception as e:
            logging.error(f"Erro inesperado ao obter usuários: {str(e)}")
            raise
    
    def getTickets(self):
        """_summary_

        Raises:
            ValueError: _description_

        Returns:
            _type_: _description_
        """
        try:
            if not self.__tickets:
                raise ValueError("Nenhum ticket encontrado.")
            return list(self.__tickets)
        except ValueError as e:
            logging.error(f"Erro ao obter tickets: {str(e)}")
            raise
        except Exception as e:
            logging.error(f"Erro inesperado ao obter tickets: {str(e)}")
            raise
    
    def getRatings(self):
        """_summary_

        Raises:
            ValueError: _description_

        Returns:
            _type_: _description_
        """
        try:
            if not self.__ratings:
                raise ValueError("Nenhum rating encontrado.")
            return list(self.__ratings)
        except ValueError as e:
            logging.error(f"Erro ao obter ratings: {str(e)}")
            raise
        except Exception as e:
            logging.error(f"Erro inesperado ao obter ratings: {str(e)}")
            raise
    
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
            logging.error(f"Erro ao obter compras: {str(e)}")
            raise
        except Exception as e:
            logging.error(f"Erro inesperado ao obter compras: {str(e)}")
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
                raise ValueError("Ticket já registrado.")
        except ValueError as e:
            logging.error(f"Erro ao adicionar ticket para o usuário {self._id}: {str(e)}")
            raise
        except Exception as e:
            logging.error(f"Erro inesperado ao adicionar ticket para o usuário {self._id}: {str(e)}")
            raise

    def buyTicket(self, tier, quantity, seller, paymentMethod):
        """_summary_

        Args:
            tier (_type_): _description_
            quantity (_type_): _description_
            seller (_type_): _description_
            paymentMethod (_type_): _description_

        Returns:
            _type_: _description_
        """
        try:
            if tier._event._typeEvent == TypeEvent.FREE_EVENT:
                return self.registerInFreeEvent(tier)
            purchase = seller.createPurchase(tier, quantity, self, paymentMethod)
            return purchase
        except ValueError as e:
            logging.error(f"Erro ao comprar ticket para o usuário {self._id}: {str(e)}")
            raise
        except Exception as e:
            logging.error(f"Erro inesperado ao comprar ticket para o usuário {self._id}: {str(e)}")
            raise
    
    def transferTicket(self, ticket: Ticket, newCPF: str) -> None:
        """_summary_

        Args:
            ticket (Ticket): _description_
            newCPF (str): _description_

        Raises:
            ValueError: _description_
            ValueError: _description_
            ValueError: _description_
            ValueError: _description_
            ValueError: _description_
        """
        try:
            if ticket._event._typeEvent == TypeEvent.FREE_EVENT:
                raise ValueError("Não é possível transferir ingressos de eventos gratuitos.")
            if ticket not in self.__tickets:
                raise ValueError("O ticket não pertence a este usuário.")
            if ticket._status != Status.VALID:
                raise ValueError("O ticket não está válido para transferência.")
            if ticket._event.status == Status.CLOSED:
                raise ValueError("O evento já foi encerrado, não é possível transferir o ingresso.")
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
        except ValueError as e:
            logging.error(f"Erro ao transferir ticket para o usuário {self._id}: {str(e)}")
            raise
        except Exception as e:
            logging.error(f"Erro inesperado ao transferir ticket para o usuário {self._id}: {str(e)}")
            raise

    def registerInFreeEvent(self, tier):
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
            if tier._event._typeEvent != TypeEvent.FREE_EVENT:
                raise ValueError("O evento não é gratuito.")
            if tier.getDisponibility() <= 0:
                raise ValueError("Não há ingressos disponíveis para o evento.")
            if tier._event.status == Status.CLOSED:
                raise ValueError("O evento já foi encerrado, não é possível registrar-se.")
            ticket = Ticket(id=uuid4(), owner=self, tier=tier, event=tier._event, status=Status.VALID, code=str(uuid4()))
            self.addTicket(ticket)
            return ticket
        except ValueError as e:
            logging.error(f"Erro ao registrar no evento gratuito para o usuário {self._id}: {str(e)}")
            raise
        except Exception as e:
            logging.error(f"Erro inesperado ao registrar no evento gratuito para o usuário {self._id}: {str(e)}")
            raise
    
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
                raise ValueError("O usuário não pode avaliar o evento.")
            if event.status == Status.CLOSED:
                rating = Rating(id=uuid4(), user=self, event=event, rate=rate, comment=comment)
                self.__ratings.append(rating)
                event.addRating(rating)
                return rating
            else:
                raise ValueError("O evento não está encerrado, não é possível avaliar.")
        except ValueError as e:
            logging.error(f"Erro ao criar rating para o usuário {self._id}: {str(e)}")
            raise
        except Exception as e:
            logging.error(f"Erro inesperado ao criar rating para o usuário {self._id}: {str(e)}")
            raise

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
                raise ValueError("O rating não pertence a este usuário.")
            if rating._event.status != Status.CLOSED:
                raise ValueError("O evento não está encerrado, não é possível atualizar a avaliação.")
            rating._rate = rate if 0 <= rate <= 5 else rating._rate
            rating._comment = comment if comment else rating._comment
        except ValueError as e:
            logging.error(f"Erro ao atualizar rating para o usuário {self.__name}: {str(e)}")
            raise
        except Exception as e:
            logging.error(f"Erro inesperado ao atualizar rating para o usuário {self.__name}: {str(e)}")
            raise

    def deleteRating(self, rating: Rating) -> None:
        """_summary_

        Args:
            rating (Rating): _description_

        Raises:
            ValueError: _description_
        """
        try:
            if rating not in self.__ratings:
                raise ValueError("O rating não pertence a este usuário.")
            self.__ratings.remove(rating)
        except ValueError as e:
            logging.error(f"Erro ao deletar rating para o usuário {self.__name}: {str(e)}")
            raise
        except Exception as e:
            logging.error(f"Erro inesperado ao deletar rating para o usuário {self.__name}: {str(e)}")
            raise

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
                raise ValueError("Compra não pertence a este usuário.")
            if purchase._status == PaymentStatus.PAID:
                raise ValueError("A compra já foi paga.")
            if purchase._status == PaymentStatus.PENDING:
                purchase._status = PaymentStatus.PAID
                tickets, receipt = purchase.confirmPayment()
                for ticket in tickets:
                    self.addTicket(ticket)
                self.addReceipt(receipt)
                self.addPurchase(purchase)
        except ValueError as e:
            logging.error(f"Erro ao pagar compra para o usuário {self._id}: {str(e)}")
            raise
    
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
                raise ValueError("Compra já registrada.")
            if purchase not in self.__purchases:
                self.__purchases.append(purchase)
            else:
                raise ValueError("Compra já registrada.")
        except ValueError as e:
            logging.error(f"Erro ao adicionar compra para o usuário {self._id}: {str(e)}")
            raise
        except Exception as e:
            logging.error(f"Erro inesperado ao adicionar compra para o usuário {self._id}: {str(e)}")
            raise

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
            logging.error(f"Erro ao solicitar reembolso para o usuário {self._id}: {str(e)}")
            return False
        except Exception as e:
            logging.error(f"Erro inesperado ao solicitar reembolso para o usuário {self._id}: {str(e)}")
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
                raise ValueError("Recibo já registrado.")
            if receipt not in self.__receipts:
                self.__receipts.append(receipt)
            else:
                raise ValueError("Recibo já registrado.")
        except ValueError as e:
            logging.error(f"Erro ao adicionar recibo para o usuário {self._id}: {str(e)}")
            raise
        except Exception as e:
            logging.error(f"Erro inesperado ao adicionar recibo para o usuário {self._id}: {str(e)}")
            raise

