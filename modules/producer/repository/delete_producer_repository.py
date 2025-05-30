from models.models import Producer
from db import SessionLocal

class DeleteProducerRepository:
    def __init__(self, session=None):
        self.session = session or SessionLocal()

    def delete(self, producer) -> bool:
        """
        Deletes a producer from the database by ID.

        Args:
            id (str): ID of the producer to be deleted.
        Returns:
            bool: True if the producer was successfully deleted, False otherwise.
        """
        try:
            self.session.delete(producer)
            self.session.commit()
            return True
        except Exception as e:
            self.session.rollback()
            return False