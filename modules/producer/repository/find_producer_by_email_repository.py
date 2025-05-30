from models.models import Producer
from db import SessionLocal

class FindProducerByEmailRepository:
    def __init__(self, session=None):
        self.session = session or SessionLocal()

    def findByEmail(self, email: str) -> Producer:
        """
        Finds a producer by email in the database.

        Args:
            email (str): Email of the producer to be found.
        Returns:
            Producer | None: Producer model instance or None if not found.
        """
        return self.session.query(Producer).filter(Producer.email == email).first()