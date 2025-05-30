from dataclasses import asdict
from models.models import Producer
from db import SessionLocal
from modules.producer import CreateProducerDTO
from sqlalchemy.exc import IntegrityError

class CreateProducerRepository:
    def __init__(self, session=None):
        self.session = session or SessionLocal()

    def create(self, data: CreateProducerDTO):
        """
        Creates a new producer in the database.

        Args:
            data (CreateProducerDTO): Data of the producer to be created.
        Returns:
            Producer: Created Producer model instance.
        """
        try:
            data = asdict(data)
            producer = Producer(**data)
            self.session.add(producer)
            self.session.commit()
            self.session.refresh(producer)
            return producer
        except IntegrityError as e:
            self.session.rollback()
            raise ValueError("Usuário com CPF, email ou telefone já cadastrado.") from e

