from models.models import Status, User
from db import SessionLocal

class DeleteUserRepository:
    def __init__(self, session=None):
        self.session = session or SessionLocal()

    def delete(self, id) -> bool:
        """
        Deletes a id from the database.

        Args:
            id (_type_): id model instance to be deleted.

        Returns:
            bool: True if deletion was successful, False otherwise.
        """
        try:
            user = self.session.query(User).filter(User.id == id).first()
            self.session.delete(user)
            self.session.commit()
            return True
        except Exception as e:
            self.session.rollback()
            return False
        
    def softDelete(self, id) -> bool:
        """
        Soft deletes a id by setting the 'is_deleted' flag to True.

        Args:
            id (_type_): id model instance to be soft deleted.

        Returns:
            bool: True if soft deletion was successful, False otherwise.
        """
        try:
            user = self.session.query(User).filter(User.id == id).first()
            user.status = Status.DELETED
            self.session.add(user)
            self.session.commit()
            return True
        except Exception as e:
            self.session.rollback()
            print(f"Error during soft delete: {e}")
            return False