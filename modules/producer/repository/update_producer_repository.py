from models.models import Producer
from db import SessionLocal
from modules.producer.dto.update_producer_dto import UpdateProducerDTO

class UpdateProducerRepository:
    def __init__(self, session=None):
        self.session = session or SessionLocal()

    def update(self, id, data: UpdateProducerDTO):
        """
        Atualiza um produtor existente no banco de dados.

        :param id: ID do produtor a ser atualizado.
        :param data: Dados do produtor a serem atualizados.
        :return: Instância do modelo Producer atualizada.
        """
        producer = self.session.query(Producer).filter(Producer.id == id).first()
        for key, value in data.dict().items():
            setattr(producer, key, value)
        self.session.commit()
        self.session.refresh(producer)
        return producer