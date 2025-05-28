from models.models import Producer
from db import SessionLocal

class FindProducerByIdRepository:
    def __init__(self, session=None):
        self.session = session or SessionLocal()

    def findById(self, producer_id: str) -> Producer:
        """
        Encontra um produtor pelo ID no banco de dados.
        
        :param producer_id: ID do produtor a ser encontrado.
        :return: Instância do modelo Producer ou None se não encontrado.
        """
        return self.session.query(Producer).filter(Producer.id == producer_id).first()