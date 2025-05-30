from models.models import User
from db import SessionLocal

class DeleteUserRepository:
    def __init__(self, session=None):
        self.session = session or SessionLocal()

    def delete(self, user) -> bool:
        """
        Deletes a user from the database.

        Args:
            user (_type_): User model instance to be deleted.

        Returns:
            bool: True if deletion was successful, False otherwise.
        """
        try:
            self.session.delete(user)
            self.session.commit()
            return True
        except Exception as e:
            self.session.rollback()
            return False