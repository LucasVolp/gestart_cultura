from db import SessionLocal
from models.models import Event
from sqlalchemy.exc import IntegrityError

class FindAllEventsRepository:
    def __init__(self, session=None):
        self.session = session or SessionLocal()

    def findAll(self):
        """
        Returns all events from the database.

        Returns:
            Return: List of Event model instances.
        """
        return self.session.query(Event).all()
