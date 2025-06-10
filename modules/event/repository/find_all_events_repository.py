from db import SessionLocal
from models.models import Event
from sqlalchemy.orm import joinedload

class FindAllEventsRepository:
    def __init__(self, session=None):
        self.session = session or SessionLocal()

    def findAll(self):
        """
        Returns all events from the database.

        Returns:
            Return: List of Event model instances.
        """
        try:
            return (
                self.session.query(Event)
                .options(
                    joinedload(Event.tiers),
                    joinedload(Event.ratings),
                    joinedload(Event.producers),
            ).all()
            )
        except Exception as e:
            self.session.rollback()
            raise e
        finally:
            self.session.close()
