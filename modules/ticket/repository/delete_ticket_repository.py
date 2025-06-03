from db import SessionLocal
from models.models import Status, Ticket

class DeleteTicketRepository:
    def __init__(self, session=None):
        self.session = session or SessionLocal()

    def delete(self, id) -> bool:
        """
        Deletes a ticket from the database by ID.

        Args:
            id (str): Ticket ID to be deleted.
        Returns:
            bool: True if the ticket was deleted successfully, False otherwise.
        """
        try:
            ticket = self.session.query(Ticket).filter(Ticket.id == id).first()
            if not ticket:
                return False
            self.session.delete(ticket)
            self.session.commit()
            return True
        except Exception as e:
            self.session.rollback()
            return False
        
    def softDelete(self, id) -> bool:
        """
        Soft deletes a ticket by setting its 'deleted' attribute to True.

        Args:
            id (str): Ticket ID to be soft deleted.
        Returns:
            bool: True if the ticket was soft deleted successfully, False otherwise.
        """
        try:
            ticket = self.session.query(Ticket).filter(Ticket.id == id).first()
            if not ticket:
                return False
            ticket.status = Status.CANCELLED
            self.session.commit()
            return True
        except Exception as e:
            self.session.rollback()
            return False