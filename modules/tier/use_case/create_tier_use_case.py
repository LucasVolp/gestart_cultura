from modules.tier import CreateTierRepository, CreateTierDTO, FindTierByNameRepository

class CreateTierUseCase:
    def __init__(self, repository=None, findTierByName=None):
        self.repository = repository or CreateTierRepository()
        self.findTierByName = findTierByName or FindTierByNameRepository()
    def execute(self, data: CreateTierDTO):
        """Executes the use case to create a new tier.

        Args:
            data (CreateTierDTO): Data Transfer Object containing the tier information to be created.

        Raises:
            ValueError: If a tier with the same name already exists or if there is an error during creation.
            e: If any other error occurs during the creation process.

        Returns:
            _type_: Created Tier model instance.
        """
        try:
            tierExists = self.findTierByName.findByName(data.name)
            if tierExists:
                raise ValueError(f"Tier com o nome {data.name} já existe.")
            tier = self.repository.create(data)
            print(f"Tier {tier.name} criado com sucesso.")
            return tier
        except Exception as e:
            print(f"Erro ao criar tier: {e}")
            raise e
        finally:
            self.repository.session.close()
