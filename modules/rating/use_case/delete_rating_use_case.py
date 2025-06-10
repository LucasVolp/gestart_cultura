from fastapi import HTTPException
from modules.rating import DeleteRatingRepository, FindRatingByIdRepository

class DeleteRatingUseCase:
    def __init__(self, repository=None, findRatingById=None):
        self.repository = repository or DeleteRatingRepository()
        self.findRatingById = findRatingById or FindRatingByIdRepository()
        
    def execute(self, id):
        """
        Executes the use case to delete a rating by its ID.
        
        Args:
            id (int): ID of the rating to be deleted.

        Raises:
            HTTPException: 404 if the rating with the given ID does not exist.
            HTTPException: 500 if an error occurs during the deletion process.

        Returns:
            bool: True if deleted successfully.
        """
        try:
            ratingExists = self.findRatingById.findById(id)
            if not ratingExists:
                raise HTTPException(
                    status_code=404,
                    detail="Avaliação não encontrada."
                )
            deleted = self.repository.delete(id)
            if not deleted:
                raise HTTPException(status_code=400, detail="Erro ao deletar avaliação.")
            print(f"Avaliação com ID {id} deletada com sucesso.")
            raise HTTPException(status_code=200, detail="Avaliação deletada com sucesso.")
        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(status_code=400,detail="Erro ao deletar avaliação: ")
        finally:
            if hasattr(self.repository, 'session') and self.repository.session:
                self.repository.session.close()
            if hasattr(self.findRatingById, 'session') and self.findRatingById.session:
                self.findRatingById.session.close()
