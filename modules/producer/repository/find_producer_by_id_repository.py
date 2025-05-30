from models.models import Producer
from db import SessionLocal

class FindProducerByIdRepository:
    def __init__(self, session=None):
        self.session = session or SessionLocal()

    def findById(self, id: str) -> Producer:
        """
        Finds a producer by ID in the database.

        Args:
            id (str): ID of the producer to be found.
        Returns:
            Producer | None: Producer model instance or None if not found.
        """
        return self.session.query(Producer).filter(Producer.id == id).first()