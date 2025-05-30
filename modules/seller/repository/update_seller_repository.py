from dataclasses import asdict
from models import Seller
from db import SessionLocal
from modules.seller import UpdateSellerDTO

class UpdateSellerRepository:
    def __init__(self, session=None):
        self.session = session or SessionLocal()

    def update(self, seller, data: UpdateSellerDTO):
        """
        Updates an existing seller in the database.

        Args:
            seller (Seller): Seller model instance to be updated.
            data (UpdateSellerDTO): Data Transfer Object containing the updated seller information.
        Returns:
            Seller: Updated Seller instance.
        """
        data = asdict(data)
        for key, value in data.items():
            if value is not None:
                setattr(seller, key, value)
        self.session.commit()
        self.session.refresh(seller)
        return seller
