from modules.user.repository import FindAllUsersRepository
from fastapi import HTTPException


class FindAllUsersUseCase:
    def __init__(self, userRepository=None):
        self.userRepository = userRepository or FindAllUsersRepository()

    def execute(self) -> list:
        """        Executes the use case to find all users.

        Raises:
            HTTPException: If an error occurs during the operation.

        Returns:
            list: List of User model instances or an empty list if no users are found.
        """
        try:
            users = self.userRepository.findAll()
            print(f"{len(users)} usuários encontrados.")
            return users
        except Exception as e:
            print(f"Erro ao buscar usuários: {e}")
            raise HTTPException(status_code=500, detail="Erro ao buscar usuários.")
        finally:
            self.userRepository.session.close()