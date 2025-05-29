from models.models import User
from db import SessionLocal

class DeleteUserRepository:
    def __init__(self, session=None):
        self.session = session or SessionLocal()

    def delete(self, id: str) -> bool:
        """
        Deleta um usuário do banco de dados pelo ID.

        :param id: ID do usuário a ser deletado.
        :return: Instância do modelo User deletada.
        """
        user = self.session.query(User).filter(User.id == id).first()
        if not user:
            return False
        self.session.delete(user)
        self.session.commit()
        return True