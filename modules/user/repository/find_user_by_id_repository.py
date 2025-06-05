from models.models import Event, User
from db import SessionLocal
from sqlalchemy.orm import joinedload

class FindUserByIdRepository:
    def __init__(self, session=None):
        self.session = session or SessionLocal()

    def findById(self, id: str) -> User | None:
        """        Retrieves a user by their ID from the database.

        Args:
            id (str): ID of the user to be retrieved.

        Returns:
            User | None: User model instance if found, None otherwise.
        """
        return self.session.query(User).filter(User.id == id).options(
                joinedload(User.events).options(
                    joinedload(Event.tiers),
                    joinedload(Event.ratings),
                    joinedload(Event.producers),
                ),
                joinedload(User.sales),
                joinedload(User.tickets),
                joinedload(User.ratings),
                joinedload(User.purchases),
                joinedload(User.receipts),
        ).first()