from models.models import Producer
from db import SessionLocal

class FindProducerByCPFRepository:
    def __init__(self, session=None):
        self.session = session or SessionLocal()

    def findByCPF(self, cpf: str) -> Producer:
        """
        Finds a producer by CPF in the database.

        Args:
            cpf (str): CPF of the producer to be found.
        Returns:
            Producer | None: Producer model instance or None if not found.
        """
        return self.session.query(Producer).filter(Producer.cpf == cpf).first()