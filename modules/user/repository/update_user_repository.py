from models.models import User
from modules.user.dto.update_user_dto import UpdateUserDTO
from db import SessionLocal

class UpdateUserRepository:
    def __init__(self, session=None):
        self.session = session or SessionLocal()

    def update(self, id: str, data: UpdateUserDTO) -> User:
        """
        Atualiza um usuário no banco de dados pelo ID.

        :param id: ID do usuário a ser atualizado.
        :param data: Dados a serem atualizados.
        :return: Instância do modelo User atualizada.
        """
        user = self.session.query(User).filter(User.id == id).first()
        for key, value in data.items():
            setattr(user, key, value)
        self.session.commit()
        self.session.refresh(user)
        return user