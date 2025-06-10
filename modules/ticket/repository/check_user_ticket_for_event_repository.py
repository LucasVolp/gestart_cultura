from db import SessionLocal
from models.models import Ticket, Tier, Event
from sqlalchemy.orm import joinedload
from uuid import UUID

class CheckUserTicketForEventRepository:
    def __init__(self, session=None):
        self.session = session or SessionLocal()

    def userHasTicketForEvent(self, userId: UUID, eventId: UUID) -> bool:
        """
        Checks if a user has a valid ticket for a specific event.
        
        Args:
            userId (UUID): The ID of the user
            eventId (UUID): The ID of the event
            
        Returns:
            bool: True if user has a valid ticket for the event, False otherwise
        """
        ticket = (
            self.session.query(Ticket)
            .join(Tier, Ticket.tierId == Tier.id)
            .join(Event, Tier.eventId == Event.id)
            .filter(
                Ticket.ownerId == userId,
                Event.id == eventId,
                Ticket.status == 'VALID'
            )
            .first()
        )
        
        return ticket is not None

    def getUserTicketsForEvent(self, userId: UUID, eventId: UUID) -> list[Ticket]:
        """
        Gets all valid tickets that a user has for a specific event.
        
        Args:
            userId (UUID): The ID of the user
            eventId (UUID): The ID of the event
            
        Returns:
            list[Ticket]: List of valid tickets for the event
        """
        tickets = (
            self.session.query(Ticket)
            .options(joinedload(Ticket.tier).joinedload(Tier.event))
            .join(Tier, Ticket.tierId == Tier.id)
            .join(Event, Tier.eventId == Event.id)
            .filter(
                Ticket.ownerId == userId,
                Event.id == eventId,
                Ticket.status == 'VALID'
            )
            .all()
        )
        
        return tickets
