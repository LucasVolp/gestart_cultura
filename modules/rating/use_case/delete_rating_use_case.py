from modules.rating import DeleteRatingRepository, FindRatingByIdRepository

class DeleteRatingUseCase:
    def __init__(self, repository=None, findRatingById=None):
        self.repository = repository or DeleteRatingRepository()
        self.findRatingById = findRatingById or FindRatingByIdRepository()
    def execute(self, id):
        """
        Executes the use case to delete a rating by its ID.
        Args:
            id (_type_): ID of the rating to be deleted.

        Raises:
            ValueError: If the rating with the given ID does not exist.
            e: Exception raised during the deletion process.

        Returns:
            _type_: Deleted Rating model instance if successful, None if not found.
        """
        try:
            ratingExists = self.findRatingById.find_by_id(id)
            if not ratingExists:
                raise ValueError("Avaliação não encontrada.")
            rating = self.repository.delete(ratingExists)
            if rating:
                print(f"Avaliação deletada com sucesso.")
            return rating
        except Exception as e:
            print(f"Erro ao deletar avaliação: {e}")
            raise e
        finally:
            self.repository.session.close()
