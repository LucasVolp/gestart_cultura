from modules.user import UpdateUserDTO
from modules.user import FindUserByIdRepository
from modules.user import UpdateUserRepository


class UpdateUserUseCase:
    def __init__(self, userRepository, findUser):
        self.userRepository = userRepository or UpdateUserRepository()
        self.findUser = findUser or FindUserByIdRepository()

    def execute(self, id: str, data: UpdateUserDTO) -> bool:
        """
        Updates an existing user in the database.

        Args:
            id (str): ID of the user to be updated.
            data (UpdateUserDTO): Data Transfer Object containing the updated user information.

        Raises:
            ValueError: If the user with the given ID does not exist.
            e: Exception raised during the update process.

        Returns:
            bool: True if the user was updated successfully, otherwise raises an exception.
        """        
        try:
            userExists = self.findUser.findById(id)
            if not userExists:
                raise ValueError(f"Usuário não encontrado.")
            user = self.userRepository.update(userExists, data)
            print(f"Usuário {user.name} atualizado com sucesso.")
            return user
        except Exception as e:
            print(f"Erro ao atualizar usuário: {e}")
            raise e
        finally:
            self.userRepository.session.close()