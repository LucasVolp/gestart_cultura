from dataclasses import asdict
from models.models import Producer
from db import SessionLocal
from modules.producer import UpdateProducerDTO

class UpdateProducerRepository:
    def __init__(self, session=None):
        self.session = session or SessionLocal()

    def update(self, producer, data: UpdateProducerDTO):
        """
        Updates an existing producer in the database.

        Args:
            id: ID of the producer to be updated.
            data: Data of the producer to be updated.
        Returns:
            Producer: Updated Producer model instance.
        """
        data = asdict(data)
        for key, value in data.items():
            setattr(producer, key, value)
        self.session.commit()
        self.session.refresh(producer)
        return producer