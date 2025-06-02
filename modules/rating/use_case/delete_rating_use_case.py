from fastapi import HTTPException, status
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
            Rating: Deleted Rating model instance if successful.
        """
        try:
            ratingExists = self.findRatingById.findById(id)
            if not ratingExists:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Rating not found"
                )
                
            rating = self.repository.delete(ratingExists)
            return rating
        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Error deleting rating: {str(e)}"
            )
        finally:
            if hasattr(self.repository, 'session') and self.repository.session:
                self.repository.session.close()
