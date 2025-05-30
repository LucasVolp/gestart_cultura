from models.producer import Producer
from db import SessionLocal

class FindAllProducersRepository:
    def __init__(self, session=None):
        self.session = session or SessionLocal()

    def findAll(self):
        """
        Returns all producers from the database.

        Returns:
            list[Producer]: List of Producer model instances.
        """
        return self.session.query(Producer).all()