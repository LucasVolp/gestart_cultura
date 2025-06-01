from fastapi import HTTPException
from modules.receipt import DeleteReceiptRepository, FindReceiptByIdRepository

class DeleteReceiptUseCase:
    def __init__(self, repository=None, findReceiptByIdRepo=None):
        self.repository = repository or DeleteReceiptRepository()
        self.findReceiptByIdRepo = findReceiptByIdRepo or FindReceiptByIdRepository()

    def execute(self, id: str):
        """
        Deletes a receipt by ID.

        Args:
            id (str): The ID of the receipt to delete.
        Returns:
            bool: True if deletion was successful.
        Raises:
            HTTPException: If receipt is not found or an error occurs during deletion.
        """
        try:
            receipt = self.findReceiptByIdRepo.findById(id)
            if not receipt:
                raise HTTPException(status_code=404, detail=f"Receipt with ID {id} not found")
            
            self.repository.delete(receipt)
            return True
        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Internal server error while deleting receipt: {str(e)}")
        finally:
            self.repository.session.close()
            self.findReceiptByIdRepo.session.close()
