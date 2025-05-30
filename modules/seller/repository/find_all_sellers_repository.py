from models import Seller
from db import SessionLocal

class FindAllSellersRepository:
    def __init__(self, session=None):
        self.session = session or SessionLocal()

    def findAll(self):
        """        Finds all sellers in the database.

        Returns:
            _type_: List[Seller]: List of all Seller model instances.
        """
        return self.session.query(Seller).all()
