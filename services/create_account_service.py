from uuid import uuid4
from enums.status import Status
from models.producer import Producer
from models.seller import Seller
from models.user import User
from .auth_service import AuthService


class CreateAccountService:
    def findAccountByCpf(self, cpf: str) -> bool:
        try:
            if not cpf:
                raise ValueError("CPF não pode ser vazio.")
            for accounts in [User.users, Seller.sellers, Producer.producers]:
                for account in accounts:
                    if account.cpf == cpf:
                        return account
            return None
        except ValueError as e:
            print(f"Erro ao buscar conta por CPF: {e}")
            return None
    
    def createAccount(self, account_type: str, name: str, cpf: str, birth: str, email: str, password: str, phone: str, cnpj: str = None, enterprise: str = None) -> bool:
        try:
            if not name or not cpf or not birth or not email or not password or not phone:
                raise ValueError("Todos os campos são obrigatórios.")
            if account_type == "producer" and (not cnpj or not enterprise):
                raise ValueError("CNPJ e nome da empresa são obrigatórios para produtores.")
            if AuthService.searchAccount(email):
                raise ValueError("Email já cadastrado.")
            if self.findAccountByCpf(cpf):
                raise ValueError("CPF já cadastrado.")

            if account_type == "user":
                user = User(id=uuid4(),name=name, cpf=cpf, birth=birth, email=email, password=password, phone=phone, balance=1000, status=Status.ACTIVE)
                if user:
                    User.users.append(user)
                    return True
                return False
            elif account_type == "seller":
                seller = Seller(id=uuid4(), name=name, cpf=cpf, birth=birth, email=email, password=password, phone=phone, status=Status.ACTIVE)
                if seller:
                    Seller.sellers.append(seller)
                    return True
                return False
            elif account_type == "producer":
                producer = Producer(id=uuid4(), name=name, cpf=cpf, birth=birth, email=email, password=password, phone=phone, cnpj=cnpj, enterprise=enterprise, status=Status.ACTIVE)
                if producer:
                    Producer.producers.append(producer)
                    return True
                return False
        except ValueError as e:
            print(f"Erro ao criar conta: {e}")
            return False