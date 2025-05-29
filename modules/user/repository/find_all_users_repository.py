from models.models import User
from db import SessionLocal

class FindAllUsersRepository:
    def __init__(self, session=None):
        self.session = session or SessionLocal()

    def findAll(self) -> list[User]:
        """
        Busca todos os usuários no banco de dados.

        :return: Lista de instâncias do modelo User.
        """
        users = self.session.query(User).all()
        return users