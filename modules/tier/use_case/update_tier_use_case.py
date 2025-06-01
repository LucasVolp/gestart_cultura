from modules.tier.repository import UpdateTierRepository, FindTierByIdRepository
from modules.tier.dto import UpdateTierDTO
from fastapi import HTTPException

class UpdateTierUseCase:
    def __init__(self, repository=None, findTierByIdRepo=None):
        self.repository = repository or UpdateTierRepository()
        self.findTierByIdRepo = findTierByIdRepo or FindTierByIdRepository()
        
    def execute(self, id: str, data: UpdateTierDTO):
        """Updates a tier by its ID with the provided data.

        Args:
            id (str): ID of the tier to be updated.
            data (UpdateTierDTO): Data transfer object containing the updated tier information.

        Raises:
            HTTPException: If the tier with the given ID does not exist or if an error occurs.

        Returns:
            Tier: Updated Tier model instance if successful.
        """
        try:
            tierExists = self.findTierByIdRepo.findById(id)
            if not tierExists:
                raise HTTPException(status_code=404, detail="Tier não encontrado.")
            tier = self.repository.update(tierExists, data)
            print(f"Tier {tier.name} atualizado com sucesso.")
            return tier
        except HTTPException as e:
            print(f"Erro ao atualizar tier: {e.detail}")
            raise e
        except Exception as e:
            print(f"Erro ao atualizar tier: {e}")
            raise HTTPException(status_code=500, detail="Erro ao atualizar tier.")
        finally:
            self.repository.session.close()
