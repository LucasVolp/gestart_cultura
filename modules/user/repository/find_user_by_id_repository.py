from models.models import User
from db import SessionLocal

class FindUserByIdRepository:
    def __init__(self, session=None):
        self.session = session or SessionLocal()

    def findById(self, id: str) -> User | None:
        """
        Busca um usuário no banco de dados pelo ID.

        :param id: ID do usuário a ser buscado.
        :return: Instância do modelo User ou None se não encontrado.
        """
        user = self.session.query(User).filter(User.id == id).first()
        return user