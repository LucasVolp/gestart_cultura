from models.models import User
from db import SessionLocal

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
        user = self.session.query(User).filter(User.id == id).first()
        return user