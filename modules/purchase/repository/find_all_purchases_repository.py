from db import SessionLocal
from models.models import Purchase

class FindAllPurchasesRepository:
    def __init__(self, session=None):
        self.session = session or SessionLocal()

    def findAll(self):
        """
        Returns all purchases from the database.

        Returns:
            list[Purchase]: List of Purchase model instances.
        """
        return self.session.query(Purchase).all()
