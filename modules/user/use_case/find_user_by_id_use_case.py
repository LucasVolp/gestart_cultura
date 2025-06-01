from modules.user.repository import FindUserByIdRepository
from fastapi import HTTPException


class FindUserByIdUseCase:
    def __init__(self, userRepository=None):
        self.userRepository = userRepository or FindUserByIdRepository()

    def execute(self, id: str):
        """Finds a user by ID in the database.

        Args:
            id (str): ID of the user to be found.

        Raises:
            HTTPException: If the user with the given ID does not exist or if an error occurs.

        Returns:
            User: User model instance if found.
        """
        try:
            user = self.userRepository.findById(id)
            if not user:
                raise HTTPException(status_code=404, detail="Usuário não encontrado.")
            print(f"Usuário {user.name} encontrado com sucesso.")
            return user
        except HTTPException as e:
            print(f"Erro ao buscar usuário: {e.detail}")
            raise e
        except Exception as e:
            print(f"Erro ao buscar usuário: {e}")
            raise HTTPException(status_code=500, detail="Erro ao buscar usuário.")
        finally:
            self.userRepository.session.close()