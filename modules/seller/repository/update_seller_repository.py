from dataclasses import asdict
from models import Seller
from db import SessionLocal
from modules.seller import UpdateSellerDTO

class UpdateSellerRepository:
    def __init__(self, session=None):
        self.session = session or SessionLocal()

    def update(self, id: int, data: UpdateSellerDTO):

        data = asdict(data)
        seller = self.session.query(Seller).filter(Seller.id == id).first()
        for key, value in data.items():
            if value is not None:
                setattr(seller, key, value)
        self.session.commit()
        self.session.refresh(seller)
        return seller
