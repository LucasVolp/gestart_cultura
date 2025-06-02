from modules.rating.repository import FindRatingByIdRepository
from fastapi import HTTPException

class FindRatingByIdUseCase:
    """Use case for retrieving a Rating by its ID."""
    
    def __init__(self, repository=None):
        self.repository = repository or FindRatingByIdRepository()

    def execute(self, id: str):
        """Retrieves a rating by its ID.

        Args:
            id (str): The ID of the rating to retrieve.

        Returns:
            Rating: The found Rating object.

        Raises:
            HTTPException: If the rating is not found or an error occurs.
        """
        try:
            rating = self.repository.findById(id)
            if not rating:
                raise HTTPException(status_code=404, detail=f"Avaliação com ID {id} não encontrada.")
            
            print(f"Avaliação {rating.id} encontrada com sucesso.")
            return rating
            
        except HTTPException as e:
            print(f"Erro ao buscar avaliação: {e.detail}")
            raise e
        except Exception as e:
            print(f"Erro ao buscar avaliação: {e}")
            raise HTTPException(status_code=500, detail="Erro interno do servidor ao buscar avaliação.")
        finally:
            self.repository.session.close()
