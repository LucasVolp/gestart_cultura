from modules.tier import UpdateTierRepository, UpdateTierDTO, FindTierByIdRepository

class UpdateTierUseCase:
    def __init__(self, repository=None, findTierByIdRepo=None):
        self.repository = repository or UpdateTierRepository()
        self.findTierByIdRepo = findTierByIdRepo or FindTierByIdRepository()
    def execute(self, id: str, data: UpdateTierDTO):
        try:
            tierExists = self.findTierByIdRepo.findById(id)
            if not tierExists:
                raise ValueError("Tier não encontrado.")
            tier = self.repository.update(id, data)
            print(f"Tier {tier.name} atualizado com sucesso.")
            return tier
        except Exception as e:
            print(f"Erro ao atualizar tier: {e}")
            raise e
        finally:
            self.repository.session.close()
