import logging
from enums.status import Status
from models.person import Person
from models.purchase import Purchase
from models.purchaseItems import PurchaseItems
from enums.paymentStatus import PaymentStatus
from datetime import date, datetime
from uuid import uuid4

class Seller(Person):
    sellers = []

    def __init__(self, id: str, name: str, cpf: str, birth: str, email: str, password: str, phone: str, status: str):
        super().__init__(id, name, cpf, birth, email, password, phone, status)
        self.purchases = []

    def sendNotification(self, recipient: str, message: str) -> None:
        try:
            if not self._validate_phone(recipient):
                raise ValueError("Número de telefone inválido.")
            # Simula envio de SMS
            logging.info(f"SMS enviado para {recipient}: {message}")
        except ValueError as e:
            logging.error(f"Erro ao enviar notificação para {recipient}: {str(e)}")
            raise
        except Exception as e:
            logging.error(f"Erro inesperado ao enviar notificação para {recipient}: {str(e)}")
            raise

    def scheduleNotification(self, recipient: str, message: str, datetime: date) -> None:
        try:
            if not self._validate_phone(recipient):
                raise ValueError("Número de telefone inválido.")
            if datetime < date.today():
                raise ValueError("A data de agendamento deve ser futura.")
            # Simula agendamento de SMS
            logging.info(f"SMS agendado para {recipient} em {datetime}: {message}")
        except ValueError as e:
            logging.error(f"Erro ao agendar notificação para {recipient}: {str(e)}")
            raise
        except Exception as e:
            logging.error(f"Erro inesperado ao agendar notificação para {recipient}: {str(e)}")
            raise

    def createPurchase(self, tier, amount, user, paymentMethod):
        try:
            if amount <= 0:
                raise ValueError("A quantidade deve ser maior que zero.")
            if tier._quantity < amount:
                raise ValueError("Quantidade solicitada maior que a disponível.")
            if tier._status != Status.OPEN:
                raise ValueError("O tier não está disponível para compra.")
            item = PurchaseItems(id=uuid4(), tier=tier, quantity=amount, unitPrice=tier._price, totalPrice=tier._price*amount)
            purchase = Purchase(id=uuid4(), buyer=user, purchaseDate=datetime.now(), status=PaymentStatus.PENDING, totalPrice=item._totalPrice, paymentMethod=paymentMethod, items=[item])
            self.purchases.append(purchase)
            user.addPurchase(purchase)
            return purchase
        except ValueError as e:
            logging.error(f"Erro ao criar compra: {str(e)}")
            raise
        except Exception as e:
            logging.error(f"Erro inesperado ao criar compra: {str(e)}")
            raise
    
    @classmethod
    def getSellers(cls):
        try:
            if not cls.sellers:
                raise ValueError("Nenhum vendedor encontrado.")
            return list(cls.sellers)
        except ValueError as e:
            logging.error(f"Erro: {str(e)}")
            raise
        except Exception as e:
            logging.error(f"Erro inesperado: {str(e)}")
            raise
    
    def getPurchases(self):
        try:
            if not self.purchases:
                raise ValueError("Nenhuma compra encontrada.")
            return list(self.purchases)
        except ValueError as e:
            logging.error(f"Erro: {str(e)}")
            return []
        except Exception as e:
            logging.error(f"Erro inesperado: {str(e)}")
            return []


