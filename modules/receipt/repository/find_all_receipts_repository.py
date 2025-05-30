from db import SessionLocal
from models.models import Receipt

class FindAllReceiptsRepository:
    def __init__(self, session=None):
        self.session = session or SessionLocal()

    def findAll(self):
        """
        Returns all receipts from the database.

        Returns:
            list[Receipt]: List of Receipt model instances.
        """
        return self.session.query(Receipt).all()
