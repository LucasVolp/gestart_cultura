from models.models import Producer
from db import SessionLocal

class FindProducerByCPFRepository:
    def __init__(self, session=None):
        self.session = session or SessionLocal()

    def findByCPF(self, cpf: str) -> Producer:
        """
        Encontra um produtor pelo cpf no banco de dados.
        
        :param cpf: cpf do produtor a ser encontrado.
        :return: Instância do modelo Producer ou None se não encontrado.
        """
        return self.session.query(Producer).filter(Producer.cpf == cpf).first()