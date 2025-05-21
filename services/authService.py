from models.producer import Producer
from models.seller import Seller
from models.user import User


class AuthService:

    @staticmethod
    def searchAccount(email):
        try:
            if not email:
                raise ValueError("Email não pode ser vazio.")
            for accounts in [User.users, Seller.sellers, Producer.producers]:
                for account in accounts:
                    if account.email == email:
                        return account
            return None
        except ValueError as e:
            print(f"Erro ao buscar conta por email: {e}")
            return None

    @staticmethod
    def authenticate(email, password):
        try:
            if not email or not password:
                raise ValueError("Email e senha são obrigatórios.")
            account = AuthService.searchAccount(email)
            if account and account.auth(email, password):
                return account
            return None
        except ValueError as e:
            print(f"Erro ao autenticar usuário: {e}")
            return None
    
    @staticmethod
    def recoverPassword(email, cpf):
        try:
            if not email or not cpf:
                raise ValueError("Email e CPF são obrigatórios.")
            account = AuthService.searchAccount(email)
            if account:
                account.recoverPassword(email)
                return True
            raise ValueError("Conta não encontrada.")
        except ValueError as e:
            print(f"Erro ao recuperar senha: {e}")
            return None