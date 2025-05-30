from modules.rating import FindAllRatingsRepository

class FindAllRatingUseCase:
    def __init__(self, repository=None):
        self.repository = repository or FindAllRatingsRepository()
    def execute(self):
        """        Executes the use case to find all ratings.

        Raises:
            e: Exception if an error occurs during the operation.

        Returns:
            _type_: List of Rating model instances or an empty list if no ratings are found.
        """        
        try:
            ratings = self.repository.findAll()
            if not ratings:
                print("Nenhuma avaliação encontrada.")
                return []
            print(f"{len(ratings)} avaliações encontradas.")
            return ratings
        except Exception as e:
            print(f"Erro ao buscar avaliações: {e}")
            raise e
        finally:
            self.repository.session.close()
