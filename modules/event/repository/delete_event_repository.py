from db import SessionLocal
from models.models import Event

class DeleteEventRepository:
    def __init__(self, session=None):
        self.session = session or SessionLocal()

    def delete(self, id):
        event = self.session.query(Event).filter(Event.id == id).first()
        if not event:
            return False
        self.session.delete(event)
        self.session.commit()
        return True
