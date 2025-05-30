from db import SessionLocal
from models.models import Event

class FindEventByIdRepository:
    def __init__(self, session=None):
        self.session = session or SessionLocal()

    def findById(self, id):
        return self.session.query(Event).filter(Event.id == id).first()
