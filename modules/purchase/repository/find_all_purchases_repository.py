from db import SessionLocal
from models.models import Purchase
from sqlalchemy.orm import joinedload

class FindAllPurchasesRepository:
    def __init__(self, session=None):
        self.session = session or SessionLocal()

    def findAll(self):
        """
        Returns all purchases from the database.

        Returns:
            list[Purchase]: List of Purchase model instances.
        """
        return self.session.query(Purchase).options(
            joinedload(Purchase.buyer),
            joinedload(Purchase.seller),
            joinedload(Purchase.items)
        ).all()
