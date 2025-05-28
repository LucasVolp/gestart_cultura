from models.models import Producer
from db import SessionLocal
from modules.producer.dto.create_producer_dto import CreateProducerDTO

class CreateProducerRepository:
    def __init__(self, session=None):
        self.session = session or SessionLocal()

    def create(self, data: CreateProducerDTO):
        """
        Cria um novo produtor no banco de dados.

        :param data: Dados do produtor a ser criado.
        :return: Instância do modelo Producer criada.
        """
        producer = Producer(**data.dict())
        self.session.add(producer)
        self.session.commit()
        self.session.refresh(producer)
        return producer
