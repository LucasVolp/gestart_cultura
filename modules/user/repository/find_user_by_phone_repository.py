from db import SessionLocal
from models.models import User


class FindUserByPhoneRepository:
    def __init__(self, session=None):
        """
        Initializes the repository with a database session.

        :param session: The database session to use for queries. If None, a default session is used.
        """
        self.session = session or SessionLocal()

    def findUserByPhone(self, phone: str):
        """
        Find a user by their phone number.

        :param phone: The phone number of the user to find.
        :return: The user object if found, otherwise None.
        """
        try:
            user = self.session.query(User).filter(User.phone == phone).first()
            if user:
                return user
            return None
        except Exception as e:
            self.session.rollback()
            print(f"Error finding user by phone: {e}")
            return None