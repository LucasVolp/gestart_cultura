from dataclasses import asdict
from db import SessionLocal
from models.models import Event
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
        data = asdict(data)
        for key, value in data.items():
            if value is not None:
                setattr(event, key, value)
        self.session.commit()
        self.session.refresh(event)
        return event
