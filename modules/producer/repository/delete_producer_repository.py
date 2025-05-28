from models.models import Producer
from db import SessionLocal

class DeleteProducerRepository:
    def __init__(self, session=None):
        self.session = session or SessionLocal()

    def delete(self, id: str) -> bool:
        """
        Deleta um produtor do banco de dados pelo ID.

        :param id: ID do produtor a ser deletado.
        :return: True se o produtor foi deletado com sucesso, False caso contrário.
        """
        producer = self.session.query(Producer).filter(Producer.id == id).first()
        if not producer:
            return False
        self.session.delete(producer)
        self.session.commit()
        return True