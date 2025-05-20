from enums.status import Status
from models.person import Person
from models.purchase import Purchase
from models.purchaseItems import PurchaseItems
from enums.paymentStatus import PaymentStatus
from datetime import date, datetime
from uuid import uuid4, UUID

class Seller(Person):
    sellers = []

    def __init__(self, id: UUID, name: str, cpf: str, birth: str, email: str, password: str, phone: str, status: Status):
        super().__init__(id, name, cpf, birth, email, password, phone, status)
        self.purchases = []

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

    def createPurchase(self, tier, amount, user, paymentMethod):
        try:
            if amount <= 0:
                print("A quantidade deve ser maior que zero.")
                return None
            if tier.amount < amount:
                print("Quantidade solicitada maior que a disponível.")
                return None
            if tier.status != Status.OPEN:
                print("O tier não está disponível para compra.")
                return None
            item = PurchaseItems(id=uuid4(), tier=tier, quantity=amount, unitPrice=tier.price, totalPrice=tier.price*amount)
            purchase = Purchase(id=uuid4(), buyer=user, seller=self, purchaseDate=datetime.now(), status=PaymentStatus.PENDING, totalPrice=item.totalPrice, paymentMethod=paymentMethod, items=[item])
            
            self.purchases.append(purchase)
            user.addPurchase(purchase)
            return purchase
        except Exception as e:
            print(f"Erro inesperado ao criar compra: {str(e)}")
            return None
    
    @classmethod
    def getSellers(cls):
        try:
            if not cls.sellers:
                print("Nenhum vendedor encontrado.")
                return []
            return list(cls.sellers)
        except Exception as e:
            print(f"Erro inesperado: {str(e)}")
            return []
    
    def getPurchases(self):
        try:
            if not self.purchases:
                print("Nenhuma compra encontrada.")
                return []
            return list(self.purchases)
        except Exception as e:
            print(f"Erro inesperado: {str(e)}")
            return []


