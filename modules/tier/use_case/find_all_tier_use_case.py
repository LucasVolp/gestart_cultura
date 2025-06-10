from modules.tier.repository import FindAllTiersRepository
from fastapi import HTTPException

class FindAllTierUseCase:
    def __init__(self, repository=None):
        self.repository = repository or FindAllTiersRepository()
        
    def execute(self):
        """Executes the use case to find all tiers.

        Raises:
            HTTPException: If an error occurs during the operation.

        Returns:
            list: List of Tier model instances or an empty list if no tiers are found.
        """
        try:
            tiers = self.repository.findAll()
            if not tiers:
                print("Nenhum tier encontrado.")
                return []
            print(f"{len(tiers)} tiers encontrados.")
            return tiers
        except Exception as e:
            print(f"Erro ao buscar tiers: {e}")
            raise HTTPException(status_code=400, detail="Erro ao buscar tiers.")
        finally:
            self.repository.session.close()
