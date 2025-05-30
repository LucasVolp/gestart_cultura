from db import SessionLocal
from models.models import Ticket

class FindAllTicketsRepository:
    def __init__(self, session=None):
        self.session = session or SessionLocal()

    def findAll(self):
        """
        Returns all tickets from the database.

        Returns:
            list[Ticket]: List of Ticket model instances.
        """
        return self.session.query(Ticket).all()
