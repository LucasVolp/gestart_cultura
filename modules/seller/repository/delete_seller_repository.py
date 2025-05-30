from models import Seller
from db import SessionLocal

class DeleteSellerRepository:
    def __init__(self, session=None):
        self.session = session or SessionLocal()

    def delete(self, id: int):
        seller = self.session.query(Seller).filter(Seller.id == id).first()
        if not seller:
            return False
        self.session.delete(seller)
        self.session.commit()
        return True
