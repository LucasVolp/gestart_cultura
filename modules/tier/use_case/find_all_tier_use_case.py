from modules.tier import FindAllTiersRepository

class FindAllTierUseCase:
    def __init__(self, repository=None):
        self.repository = repository or FindAllTiersRepository()
    def execute(self):
        """Executes the use case to find all tiers.

        Raises:
            e: Exception if an error occurs during the operation.

        Returns:
            _type_: List of Tier model instances or an empty list if no tiers are found.
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
            raise e
        finally:
            self.repository.session.close()
