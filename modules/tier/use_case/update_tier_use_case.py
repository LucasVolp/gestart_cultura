from modules.tier import UpdateTierRepository, UpdateTierDTO, FindTierByIdRepository

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
            ValueError: If the tier with the given ID does not exist.
            e: Exception raised during the update process.

        Returns:
            _type_: Updated Tier model instance if successful.
        """
        try:
            tierExists = self.findTierByIdRepo.findById(id)
            if not tierExists:
                raise ValueError("Tier não encontrado.")
            tier = self.repository.update(tierExists, data)
            print(f"Tier {tier.name} atualizado com sucesso.")
            return tier
        except Exception as e:
            print(f"Erro ao atualizar tier: {e}")
            raise e
        finally:
            self.repository.session.close()
