from dataclasses import asdict
from db import SessionLocal
from models.models import Purchase
from modules.purchase import CreatePurchaseDTO

class CreatePurchaseRepository:
    def __init__(self, session=None):
        self.session = session or SessionLocal()

    def create(self, data: CreatePurchaseDTO):
        """
        Creates a new purchase in the database.

        Args:
            data (CreatePurchaseDTO): Data of the purchase to be created.
        Returns:
            Purchase: Created Purchase model instance.
        Raises:
            ValueError: If an integrity error occurs while creating the purchase.
        """
        data = asdict(data)
        purchase = Purchase(**data)
        self.session.add(purchase)
        self.session.commit()
        self.session.refresh(purchase)
        return purchase
