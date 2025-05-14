from repository import AccountRepository
from models import User, Seller, Producer
from enums import Status
from uuid import uuid4

class CreateAccountUseCase:
    def __init__(self, repository: AccountRepository):
        self.repository = repository

    def execute(self, account_type, name, cpf, birth, email, password, phone, cnpj=None, enterprise=None):
        if self.repository.find_by_email(email):
            raise ValueError("Email já cadastrado.")
        if self.repository.find_by_cpf(cpf):
            raise ValueError("CPF já cadastrado.")
        if account_type == "producer" and self.repository.find_producer_by_cnpj(cnpj):
            raise ValueError("CNPJ já cadastrado.")

        if account_type == "user":
            user = User(id=uuid4(), name=name, cpf=cpf, birth=birth, email=email, password=password, phone=phone, status=Status.ACTIVE)
            User.users.append(user)
            return user
        elif account_type == "seller":
            seller = Seller(id=uuid4(), name=name, cpf=cpf, birth=birth, email=email, password=password, phone=phone, status=Status.ACTIVE)
            Seller.sellers.append(seller)
            return seller
        elif account_type == "producer":
            producer = Producer(id=uuid4(), name=name, cpf=cpf, birth=birth, email=email, password=password, phone=phone, status=Status.ACTIVE, cnpj=cnpj, enterprise=enterprise)
            Producer.producers.append(producer)
            return producer
        else:
            raise ValueError("Tipo de conta inválido.")