from models import Seller
from db import SessionLocal

class FindSellerByCpfRepository:
    def __init__(self, session=None):
        self.session = session or SessionLocal()

    def findByCPF(self, cpf: str):
        """
        Finds a seller by CPF in the database.

        Args:
            cpf (str): CPF of the seller to be found.

        Returns:
            _type_: Seller | None: Seller model instance or None if not found.
        """
        return self.session.query(Seller).filter(Seller.cpf == cpf).first()
