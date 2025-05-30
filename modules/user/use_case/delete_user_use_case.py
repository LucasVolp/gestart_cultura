from modules.user import DeleteUserRepository
from modules.user import FindUserByIdRepository


class DeleteUserUseCase:
    def __init__(self, userRepository, findUser):
        self.userRepository = userRepository or DeleteUserRepository()
        self.findUser = findUser or FindUserByIdRepository()

    def execute(self, id: str) -> bool:
        """
        Deleta um usuário do banco de dados pelo ID.

        :param id: ID do usuário a ser deletado.
        :return: True se o usuário foi deletado com sucesso, False caso contrário.
        """
        try:
            userExists = self.findUser.findById(id)
            if not userExists:
                raise ValueError(f"Usuário não encontrado.")
            user = self.userRepository.delete(id)
            print(f"Usuário deletado com sucesso.")
            return user
        except Exception as e:
            print(f"Erro ao deletar usuário: {e}")
            raise e
        finally:
            self.userRepository.session.close()