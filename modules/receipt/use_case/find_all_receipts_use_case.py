from fastapi import HTTPException
from modules.receipt import FindAllReceiptsRepository

class FindAllReceiptsUseCase:
    def __init__(self, repository=None):
        self.repository = repository or FindAllReceiptsRepository()

    def execute(self):
        """
        Retrieves all receipts from the repository.
        Returns:
            list: List of Receipt objects.
        Raises:
            HTTPException: If an error occurs during retrieval.
        """
        try:
            receipts = self.repository.findAll()
            return receipts
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Internal server error while retrieving receipts: {str(e)}")
        finally:
            self.repository.session.close()
