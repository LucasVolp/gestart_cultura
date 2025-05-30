from modules.rating import CreateRatingRepository, CreateRatingDTO

class CreateRatingUseCase:
    def __init__(self, repository=None):
        self.repository = repository or CreateRatingRepository()
    def execute(self, data: CreateRatingDTO):
        """        Executes the use case to create a new rating.

        Args:
            data (CreateRatingDTO): Data Transfer Object containing the rating information.

        Raises:
            e: Exception if an error occurs during the operation.

        Returns:
            _type_: Created Rating model instance.
        """
        try:
            rating = self.repository.create(data)
            print(f"Avaliação criada com sucesso!")
            return rating
        except Exception as e:
            print(f"Erro ao criar avaliação: {e}")
            raise e
        finally:
            self.repository.session.close()
