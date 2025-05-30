from db import SessionLocal
from models.models import Ticket

class DeleteTicketRepository:
    def __init__(self, session=None):
        self.session = session or SessionLocal()

    def delete(self, ticket) -> bool:
        """
        Deletes a ticket from the database by ID.

        Args:
            id (str): Ticket ID to be deleted.
        Returns:
            bool: True if the ticket was deleted successfully, False otherwise.
        """
        self.session.delete(ticket)
        self.session.commit()
        return True