from modules.tier.repository import FindTierByIdRepository
from fastapi import HTTPException

class FindTierByIdUseCase:
    def __init__(self, repository=None):
        self.repository = repository or FindTierByIdRepository()
        
    def execute(self, id: str):
        """Finds a tier by its ID.

        Args:
            id (str): ID of the tier to be found.

        Raises:
            HTTPException: If the tier with the given ID does not exist or if an error occurs.

        Returns:
            Tier: Tier model instance if found.
        """
        try:
            tier = self.repository.findById(id)
            if not tier:
                raise HTTPException(status_code=404, detail="Tier não encontrado.")
            print(f"Tier {tier.name} encontrado com sucesso.")
            return tier
        except HTTPException as e:
            print(f"Erro ao buscar tier: {e.detail}")
            raise e
        except Exception as e:
            print(f"Erro ao buscar tier: {e}")
            raise HTTPException(status_code=400, detail="Erro ao buscar tier.")
        finally:
            self.repository.session.close()
