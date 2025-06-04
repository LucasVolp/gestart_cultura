from models.models import Status
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
            
            if not (userExists.events or userExists.tickets or userExists.sales):
                self.userRepository.delete(id)
                raise HTTPException(status_code=200, detail="Usuário deletado com sucesso.")
            
            if userExists.status == Status.DELETED:
                raise HTTPException(status_code=400, detail="Usuário já deletado.")
            
            print(f"Usuário {userExists.name} encontrado, iniciando processo de deleção.")
            user = self.userRepository.softDelete(id)
            
            if not user:
                raise HTTPException(status_code=400, detail="Erro ao deletar usuário.")
            
            print(f"Usuário deletado com sucesso.")
            raise HTTPException(status_code=200, detail="Usuário deletado com sucesso.")
        
        except HTTPException as e:
            print(f"Erro ao deletar usuário: {e.detail}")
            raise e
        except Exception as e:
            print(f"Erro ao deletar usuário: {e}")
            raise HTTPException(status_code=500, detail="Erro ao deletar usuário.")
        finally:
            if hasattr(self.userRepository, 'session'):
                self.userRepository.session.close()
            if hasattr(self.findUser, 'session'):
                self.findUser.session.close()