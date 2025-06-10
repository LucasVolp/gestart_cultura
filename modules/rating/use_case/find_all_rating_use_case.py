from fastapi import HTTPException
from modules.rating import FindAllRatingsRepository

class FindAllRatingUseCase:
    def __init__(self, repository=None):
        self.repository = repository or FindAllRatingsRepository()
        
    def execute(self):
        """
        Executes the use case to find all ratings.

        Raises:
            HTTPException: 500 if an error occurs during the operation.

        Returns:
            List[Rating]: List of Rating model instances or an empty list if no ratings are found.
        """        
        try:
            ratings = self.repository.findAll()
            return ratings if ratings else []
        except Exception as e:
            raise HTTPException(
                status_code=400,
                detail="Erro ao buscar avaliações"
            )
        finally:
            if hasattr(self.repository, 'session') and self.repository.session:
                self.repository.session.close()
