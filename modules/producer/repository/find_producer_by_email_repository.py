from models.models import Producer
from db import SessionLocal

class FindProducerByEmailRepository:
    def __init__(self, session=None):
        self.session = session or SessionLocal()

    def findByEmail(self, email: str) -> Producer:
        """
        Encontra um produtor pelo ID no banco de dados.
        
        :param email: ID do produtor a ser encontrado.
        :return: Instância do modelo Producer ou None se não encontrado.
        """
        return self.session.query(Producer).filter(Producer.email == email).first()