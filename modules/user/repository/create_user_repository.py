from models.models import User
from modules.user.dto.create_user_dto import CreateUserDTO
from db import SessionLocal

class CreateUserRepository:
    def __init__(self, session=None):
        self.session = session or SessionLocal()

    def create(self, data: CreateUserDTO) -> User:
        """
        Cria um novo usuário no banco de dados.

        :param data: Dados do usuário a ser criado.
        :return: Instância do modelo User criada.
        """
        user = User(**data.dict())
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user