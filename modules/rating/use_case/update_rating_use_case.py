from modules.rating import UpdateRatingRepository, UpdateRatingDTO, FindRatingByIdRepository

class UpdateRatingUseCase:
    def __init__(self, repository=None, findRatingById=None):
        self.repository = repository or UpdateRatingRepository()
        self.findRatingById = findRatingById or FindRatingByIdRepository()
    def execute(self, id, data: UpdateRatingDTO):
        """        Executes the use case to update an existing rating by its ID.

        Args:
            id (_type_): ID of the rating to be updated.
            data (UpdateRatingDTO): Data Transfer Object containing the updated rating information.

        Raises:
            ValueError: If the rating with the given ID does not exist.
            e: Exception raised during the update process.

        Returns:
            _type_: Updated Rating model instance if successful, None if not found.
        """        
        try:
            ratingExists = self.findRatingById.findById(id)
            if not ratingExists:
                raise ValueError("Avaliação não encontrada.")
            rating = self.repository.update(ratingExists, data)
            print(f"Avaliação atualizada com sucesso.")
            return rating
        except Exception as e:
            print(f"Erro ao atualizar avaliação: {e}")
            raise e
        finally:
            self.repository.session.close()
