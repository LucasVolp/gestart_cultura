from modules.user.repository import DeleteUserRepository, FindUserByIdRepository
from fastapi import HTTPException


class DeleteUserUseCase:
    def __init__(self, userRepository=None, findUser=None):
        self.userRepository = userRepository or DeleteUserRepository()
        self.findUser = findUser or FindUserByIdRepository()

    def execute(self, id: str) -> bool:
        """Deletes a user by its ID.

        Args:
            id (str): ID of the user to be deleted.

        Raises:
            HTTPException: If the user with the given ID does not exist or if an error occurs.

        Returns:
            bool: True if deletion was successful.
        """
        try:
            userExists = self.findUser.findById(id)
            if not userExists:
                raise HTTPException(status_code=404, detail="Usuário não encontrado.")
            user = self.userRepository.delete(userExists)
            if user:
                print(f"Usuário deletado com sucesso.")
            return user
        except HTTPException as e:
            print(f"Erro ao deletar usuário: {e.detail}")
            raise e
        except Exception as e:
            print(f"Erro ao deletar usuário: {e}")
            raise HTTPException(status_code=500, detail="Erro ao deletar usuário.")
        finally:
            self.userRepository.session.close()