from dataclasses import asdict
from db import SessionLocal
from models.models import Ticket
from modules.ticket import UpdateTicketDTO

class UpdateTicketRepository:
    def __init__(self, session=None):
        self.session = session or SessionLocal()

    def update(self, ticket, data: UpdateTicketDTO):
        """
        Updates an existing ticket in the database.

        Args:
            id (str): Ticket ID to be updated.
            data (UpdateTicketDTO): Data Transfer Object containing the updated ticket information.
        Returns:
            Ticket: Updated Ticket instance.
        """
        data = asdict(data)
        for key, value in data.items():
            if value is not None:
                setattr(ticket, key, value)
        self.session.commit()
        self.session.refresh(ticket)
        return ticket
