from modules.user import DeleteUserRepository
from modules.user import FindUserByIdRepository


class DeleteUserUseCase:
    def __init__(self, userRepository, findUser):
        self.userRepository = userRepository or DeleteUserRepository()
        self.findUser = findUser or FindUserByIdRepository()

    def execute(self, id: str) -> bool:
        """Deletes a user by its ID.

        Args:
            id (str): ID of the user to be deleted.

        Raises:
            ValueError: If the user with the given ID does not exist.
            e: Exception raised during the deletion process.

        Returns:
            bool: True if deletion was successful, False otherwise.
        """
        try:
            userExists = self.findUser.findById(id)
            if not userExists:
                raise ValueError(f"Usuário não encontrado.")
            user = self.userRepository.delete(userExists)
            if user:
                print(f"Usuário deletado com sucesso.")
            return user
        except Exception as e:
            print(f"Erro ao deletar usuário: {e}")
            raise e
        finally:
            self.userRepository.session.close()