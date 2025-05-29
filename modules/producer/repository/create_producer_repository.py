from dataclasses import asdict
from models.models import Producer
from db import SessionLocal
from modules.producer.dto.create_producer_dto import CreateProducerDTO
from sqlalchemy.exc import IntegrityError

class CreateProducerRepository:
    def __init__(self, session=None):
        self.session = session or SessionLocal()

    def create(self, data: CreateProducerDTO):
        """
        Cria um novo produtor no banco de dados.

        :param data: Dados do produtor a ser criado.
        :return: Instância do modelo Producer criada.
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

