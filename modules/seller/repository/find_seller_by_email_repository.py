from models import Seller
from db import SessionLocal

class FindSellerByEmailRepository:
    def __init__(self, session=None):
        self.session = session or SessionLocal()

    def findByEmail(self, email: str):
        return self.session.query(Seller).filter(Seller.email == email).first()
