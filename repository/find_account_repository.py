from typing import Optional, Union
from models import User, Seller, Producer

class FindAccountRepository:
    def find_account(self, email: str, identifier: str, account_type: str = None) -> Optional[Union[User, Seller, Producer]]:
        """
        Busca uma conta pelo email e identificador (CPF ou CNPJ).
        """
        account_type = account_type.lower() if account_type else None
        if account_type == "user":
            for user in User.users:
                if user.email == email and user.cpf == identifier:
                    return user
        elif account_type == "seller":
            for seller in Seller.sellers:
                if seller.email == email and seller.cpf == identifier:
                    return seller
        elif account_type == "producer":
            for producer in Producer.producers:
                if producer.email == email and producer.cnpj == identifier:
                    return producer
        else:
            for user in User.users:
                if user.email == email and user.cpf == identifier:
                    return user
            for seller in Seller.sellers:
                if seller.email == email and seller.cpf == identifier:
                    return seller
            for producer in Producer.producers:
                if producer.email == email and producer.cnpj == identifier:
                    return producer
        return None