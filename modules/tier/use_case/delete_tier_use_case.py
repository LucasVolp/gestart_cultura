from modules.tier import DeleteTierRepository, FindTierByIdRepository

class DeleteTierUseCase:
    def __init__(self, repository=None, findTierById=None):
        self.repository = repository or DeleteTierRepository()
        self.findTierById = findTierById or FindTierByIdRepository()
    def execute(self, id: str):
        """Deletes a tier by its ID.

        Args:
            id (str): ID of the tier to be deleted.

        Raises:
            ValueError: If the tier with the given ID does not exist.
            e: Exception raised during the deletion process.

        Returns:
            _type_: Deleted Tier model instance or None if not found.
        """
        try:
            tierExists = self.findTierById.findById(id)
            if not tierExists:
                raise ValueError(f"Tier não encontrado.")
            tier = self.repository.delete(tierExists)
            if tier:
                print(f"Tier deletado com sucesso.")
            return tier
        except Exception as e:
            print(f"Erro ao deletar tier: {e}")
            raise e
        finally:
            self.repository.session.close()
