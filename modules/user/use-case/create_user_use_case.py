from models.models import User
from modules.user.dto.create_user_dto import CreateUserDTO
from modules.user.repository.create_user_repository import CreateUserRepository


class CreateUserUseCase:
    def __init__(self, userRepository = None):
        self.repository = userRepository or CreateUserRepository()

    def execute(self, data: CreateUserDTO) -> User:
        """
        Cria um novo usuário no banco de dados.
        :param data: Dados do usuário a ser criado.
        :return: Instância do modelo User criada.
        """
        try:
            user = self.repository.create(data)
            print(f"Usuário {user.name} criado com sucesso.")
            return user
        except Exception as e:
            print(f"Erro ao criar usuário: {e}")
            raise e
        finally:
            self.repository.session.close()