from fastapi import HTTPException
from modules.receipt import FindReceiptByIdRepository

class FindReceiptByIdUseCase:
    def __init__(self, repository=None):
        self.repository = repository or FindReceiptByIdRepository()

    def execute(self, id: str):
        """
        Finds a receipt by ID.

        Args:
            id (str): The ID of the receipt to find.
        Returns:
            Receipt: The found Receipt object.
        Raises:
            HTTPException: If receipt is not found or an error occurs during retrieval.
        """
        try:
            receipt = self.repository.findById(id)
            if not receipt:
                raise HTTPException(status_code=404, detail=f"Receipt with ID {id} not found")
            return receipt
        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Internal server error while retrieving receipt: {str(e)}")
        finally:
            self.repository.session.close()
