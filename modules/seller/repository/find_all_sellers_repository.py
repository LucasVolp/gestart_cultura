from models import Seller
from db import SessionLocal

class FindAllSellersRepository:
    def __init__(self, session=None):
        self.session = session or SessionLocal()

    def findAll(self):
        return self.session.query(Seller).all()
