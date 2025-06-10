from models.models import User
from db import SessionLocal

class FindUserByEmailRepository:
    def __init__(self, session=None):
        self.session = session or SessionLocal()

    def findByEmail(self, email: str):
        """        Finds a user by their email address in the database.

        Args:
            email (str): Email address of the user to be found.

        Returns:
            _type_: User model instance if found, None otherwise.
        """
        return self.session.query(User).filter(User.email == email).first()
