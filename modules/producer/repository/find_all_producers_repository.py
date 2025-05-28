from models.producer import Producer
from db import SessionLocal

class FindAllProducersRepository:
    def __init__(self, session=None):
        self.session = session or SessionLocal()

    def findAll(self):
        """
        Retorna todos os produtores do banco de dados.
        
        :return: Lista de instâncias do modelo Producer.
        """
        return self.session.query(Producer).all()