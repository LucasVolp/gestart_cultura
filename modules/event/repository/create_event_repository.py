from db import SessionLocal
from models.models import Event, User
from modules.event import CreateEventDTO
from dataclasses import asdict

class CreateEventRepository:
    def __init__(self, session=None):
        self.session = session or SessionLocal()

    def create(self, data: CreateEventDTO) -> Event:
        """
        Cria um novo evento no banco de dados.

        :param data: Dados do evento a ser criado.
        :return: Instância do modelo Event criada.
        """
        try:
            producerIds = data.producers
            eventData = data.model_dump(exclude={"producers"})
            
            event = Event(**eventData)
            if producerIds:
                producers = self.session.query(User).filter(
                    User.id.in_(producerIds),
                    User.role == "PRODUCER"
                ).all()
            event.producers = producers if producerIds else []
            self.session.add(event)
            self.session.commit()
            self.session.refresh(event)
            return event
        except Exception as e:
            self.session.rollback()
            raise e