from modules.user import UpdateUserDTO
from modules.user import FindUserByIdRepository
from modules.user import UpdateUserRepository


class UpdateUserUseCase:
    def __init__(self, userRepository, findUser):
        self.userRepository = userRepository or UpdateUserRepository()
        self.findUser = findUser or FindUserByIdRepository()

    def execute(self, id: str, data: UpdateUserDTO) -> bool:
        """
        Atualiza um usuário no banco de dados pelo ID.

        :param id: ID do usuário a ser atualizado.
        :param data: Dados a serem atualizados.
        :return: True se o usuário foi atualizado com sucesso, False caso contrário.
        """
        try:
            userExists = self.findUser.findById(id)
            if not userExists:
                raise ValueError(f"Usuário não encontrado.")
            user = self.userRepository.update(id, data)
            print(f"Usuário {user.name} atualizado com sucesso.")
            return user
        except Exception as e:
            print(f"Erro ao atualizar usuário: {e}")
            raise e
        finally:
            self.userRepository.session.close()