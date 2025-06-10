from passlib.hash import bcrypt
from modules.user.dto.update_user_dto import UpdateUserDTO
from modules.user.repository import FindUserByIdRepository, UpdateUserRepository
from fastapi import HTTPException


class UpdateUserUseCase:
    def __init__(self, userRepository=None, findUser=None):
        self.userRepository = userRepository or UpdateUserRepository()
        self.findUser = findUser or FindUserByIdRepository()

    def execute(self, id: str, data: UpdateUserDTO) -> bool:
        """
        Updates an existing user in the database.

        Args:
            id (str): ID of the user to be updated.
            data (UpdateUserDTO): Data Transfer Object containing the updated user information.

        Raises:
            HTTPException: If the user with the given ID does not exist or if an error occurs.

        Returns:
            User: Updated user model instance.
        """        
        try:
            userExists = self.findUser.findById(id)
            if not userExists:
                raise HTTPException(status_code=404, detail="Usuário não encontrado.")
            if data.password:
                data.password = bcrypt.hash(data.password)
            user = self.userRepository.update(userExists, data)
            print(f"Usuário {user.name} atualizado com sucesso.")
            return user
        except HTTPException as e:
            print(f"Erro ao atualizar usuário: {e.detail}")
            raise e
        except Exception as e:
            print(f"Erro ao atualizar usuário: {e}")
            raise HTTPException(status_code=400, detail="Erro ao atualizar usuário.")
        finally:
            self.userRepository.session.close()