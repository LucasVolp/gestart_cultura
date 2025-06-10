from db import SessionLocal
from models.models import Ticket
from modules.ticket.dto import CreateTicketDTO

class CreateTicketRepository:
    def __init__(self, session=None):
        self.session = session or SessionLocal()

    def create(self, data: CreateTicketDTO):
        """
        Creates a new ticket in the database.

        Args:
            data (CreateTicketDTO): Data of the ticket to be created.
        Returns:
            Ticket: Created Ticket model instance.
        Raises:
            ValueError: If an integrity error occurs while creating the ticket.
        """
        data_dict = data.model_dump()
        ticket = Ticket(**data_dict)
        self.session.add(ticket)
        self.session.commit()
        self.session.refresh(ticket)
        return ticket
