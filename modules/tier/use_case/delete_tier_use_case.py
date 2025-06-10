from modules.tier.repository import DeleteTierRepository, FindTierByIdRepository
from fastapi import HTTPException

class DeleteTierUseCase:
    def __init__(self, repository=None, findTierById=None):
        self.repository = repository or DeleteTierRepository()
        self.findTierById = findTierById or FindTierByIdRepository()
        
    def execute(self, id: str):
        """Deletes a tier by its ID.

        Args:
            id (str): ID of the tier to be deleted.

        Raises:
            HTTPException: If the tier with the given ID does not exist or if an error occurs.

        Returns:
            bool: True if deletion was successful.
        """
        try:
            tierExists = self.findTierById.findById(id)
            if not tierExists:
                raise HTTPException(status_code=404, detail="Tier não encontrado.")
            deleted = self.repository.delete(id)
            if not deleted:
                raise HTTPException(status_code=400, detail="Erro ao deletar tier.")
            print(f"Tier deletado com sucesso.")
            return True
        except HTTPException as e:
            print(f"Erro ao deletar tier: {e.detail}")
            raise e
        except Exception as e:
            print(f"Erro ao deletar tier: {e}")
            raise HTTPException(status_code=400, detail="Erro ao deletar tier.")
        finally:
            self.repository.session.close()
