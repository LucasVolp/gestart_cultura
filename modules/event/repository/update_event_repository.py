from dataclasses import asdict
from db import SessionLocal
from models.models import Event
from modules.event import UpdateEventDTO

class UpdateEventRepository:
    def __init__(self, session=None):
        self.session = session or SessionLocal()

    def update(self, id, data: UpdateEventDTO):
        
        data = asdict(data)
        event = self.session.query(Event).filter(Event.id == id).first()
        for key, value in data.items():
            if value is not None:
                setattr(event, key, value)
        self.session.commit()
        self.session.refresh(event)
        return event
