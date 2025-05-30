from modules.rating import FindRatingByIdRepository

class FindRatingByIdUseCase:
    def __init__(self, repository=None):
        self.repository = repository or FindRatingByIdRepository()
    def execute(self, id):
        """        Executes the use case to find a rating by its ID.

        Args:
            id (_type_): ID of the rating to be found.

        Raises:
            ValueError: If the rating with the given ID does not exist.
            e: Exception raised during the search process.

        Returns:
            _type_: Rating model instance if found, None if not found.
        """        
        try:
            rating = self.repository.findById(id)
            if not rating:
                raise ValueError("Avaliação não encontrada.")
            print(f"Avaliação encontrada com sucesso.")
            return rating
        except Exception as e:
            print(f"Erro ao buscar avaliação: {e}")
            raise e
        finally:
            self.repository.session.close()
