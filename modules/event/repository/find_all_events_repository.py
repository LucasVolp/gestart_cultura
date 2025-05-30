from db import SessionLocal
from models.models import Event
from sqlalchemy.exc import IntegrityError

class FindAllEventsRepository:
    def __init__(self, session=None):
        self.session = session or SessionLocal()

    def findAll(self):
        return self.session.query(Event).all()
