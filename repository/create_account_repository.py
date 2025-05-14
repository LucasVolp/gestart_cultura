from typing import Optional
from models import User, Seller, Producer

class AccountRepository:
    def find_by_email(self, email: str) -> Optional[object]:
        try:
            email = email.lower()
            if not email:
                raise ValueError("Email não pode ser vazio.")
            for user in User.users:
                if user.email == email:
                    return user
            for seller in Seller.sellers:
                if seller.email == email:
                    return seller
            for producer in Producer.producers:
                if producer.email == email:
                    return producer
            return None
        except ValueError as e:
            print(f"Erro ao buscar conta por email: {e}")
            return None

    def find_by_cpf(self, cpf: str) -> Optional[object]:
        try:
            if not cpf:
                raise ValueError("CPF não pode ser vazio.")
            for user in User.users:
                if user.cpf == cpf:
                    return user
            for seller in Seller.sellers:
                if seller.cpf == cpf:
                    return seller
            for producer in Producer.producers:
                if producer.cpf == cpf:
                    return producer
            return None
        except ValueError as e:
            print(f"Erro ao buscar conta por CPF: {e}")
            return None

    def find_producer_by_cnpj(self, cnpj: str) -> Optional[Producer]:
        try:
            if not cnpj:
                raise ValueError("CNPJ não pode ser vazio.")
            for producer in Producer.producers:
                if producer.cnpj == cnpj:
                    return producer
            return None
        except ValueError as e:
            print(f"Erro ao buscar produtor por CNPJ: {e}")
            return None