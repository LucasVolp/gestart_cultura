from modules.tier import DeleteTierRepository, FindTierByIdRepository

class DeleteTierUseCase:
    def __init__(self, repository=None, findTierById=None):
        self.repository = repository or DeleteTierRepository()
        self.findTierById = findTierById or FindTierByIdRepository()
    def execute(self, id: str):
        try:
            tierExists = self.findTierById.findById(id)
            if not tierExists:
                raise ValueError(f"Tier com ID {id} não encontrado.")
            result = self.repository.delete(id)
            print(f"Tier deletado com sucesso.")
            return result
        except Exception as e:
            print(f"Erro ao deletar tier: {e}")
            raise e
        finally:
            self.repository.session.close()
