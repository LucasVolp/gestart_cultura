from models import Seller
from db import SessionLocal

class FindSellerByCpfRepository:
    def __init__(self, session=None):
        self.session = session or SessionLocal()

    def findByCPF(self, cpf: str):
        return self.session.query(Seller).filter(Seller.cpf == cpf).first()
