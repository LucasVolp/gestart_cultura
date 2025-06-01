from dataclasses import asdict
from db import SessionLocal
from models.models import Event, User
from modules.event import UpdateEventDTO

class UpdateEventRepository:
    def __init__(self, session=None):
        self.session = session or SessionLocal()

    def update(self, event, data: UpdateEventDTO):
        """
        Updates an existing event in the database.

        Args:
            event (_type_): Event model instance to be updated.
            data (UpdateEventDTO): Data of the event to be updated.

        Returns:
            _type_: Updated Event model instance.
        """
        try:
            producer_ids = data.producers

            data_dict = asdict(data)
            if 'producers' in data_dict:
                del data_dict['producers']

            for key, value in data_dict.items():
                if value is not None:
                    setattr(event, key, value)

            
            if producer_ids is not None:
                producers = self.session.query(User).filter(
                    User.id.in_(producer_ids),
                    User.role == "PRODUCER"
                ).all()
                
                event.producers = producers
            
            self.session.commit()
            self.session.refresh(event)
            return event
        except Exception as e:
            self.session.rollback()
            raise e
