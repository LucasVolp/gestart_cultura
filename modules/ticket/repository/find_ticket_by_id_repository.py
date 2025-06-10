from db import SessionLocal
from models.models import Ticket

class FindTicketByIdRepository:
    def __init__(self, session=None):
        self.session = session or SessionLocal()

    def findById(self, id: str):
        """
        Finds a ticket by ID in the database.

        Args:
            id (str): Ticket ID to be found.
        Returns:
            Ticket | None: Ticket model instance or None if not found.
        """
        return self.session.query(Ticket).filter(Ticket.id == id).first()
