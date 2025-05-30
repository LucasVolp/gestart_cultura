from models import Seller
from db import SessionLocal

class FindSellerByIdRepository:
    def __init__(self, session=None):
        self.session = session or SessionLocal()

    def findById(self, seller_id: int):
        return self.session.query(Seller).filter(Seller.id == seller_id).first()
