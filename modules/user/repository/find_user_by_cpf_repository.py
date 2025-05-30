from models import User
from db import SessionLocal

class FindUserByCpfRepository:
    def __init__(self, session=None):
        self.session = session or SessionLocal()

    def findByCpf(self, cpf: str):
        """Finds a user by their CPF in the database.

        Args:
            cpf (str): The CPF of the user to be found.

        Returns:
            _type_: User model instance if found, None otherwise.
        """
        return self.session.query(User).filter(User.cpf == cpf).first()
