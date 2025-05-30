from modules.tier import FindTierByIdRepository

class FindTierByIdUseCase:
    def __init__(self, repository=None):
        self.repository = repository or FindTierByIdRepository()
    def execute(self, id: str):
        try:
            tier = self.repository.findById(id)
            if not tier:
                raise ValueError("Tier não encontrado.")
            print(f"Tier {tier.name} encontrado com sucesso.")
            return tier
        except Exception as e:
            print(f"Erro ao buscar tier: {e}")
            raise e
        finally:
            self.repository.session.close()
