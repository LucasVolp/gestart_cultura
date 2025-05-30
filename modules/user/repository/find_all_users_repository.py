from models.models import User
from db import SessionLocal

class FindAllUsersRepository:
    def __init__(self, session=None):
        self.session = session or SessionLocal()

    def findAll(self) -> list[User]:
        """
        Retrieves all users from the database.

        Returns:
            list[User]: List of User model instances.
        """
        users = self.session.query(User).all()
        return users