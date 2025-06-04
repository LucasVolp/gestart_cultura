from models.models import User
from db import SessionLocal
from sqlalchemy.orm import joinedload

class FindAllUsersRepository:
    def __init__(self, session=None):
        self.session = session or SessionLocal()

    def findAll(self) -> list[User]:
        """
        Retrieves all users from the database.

        Returns:
            list[User]: List of User model instances.
        """
        return (
            self.session.query(User)
            .options(
                joinedload(User.events),
                joinedload(User.sales),
                joinedload(User.tickets),
                joinedload(User.ratings),
                joinedload(User.purchases),
                joinedload(User.receipts),
            )
            .all()
        )