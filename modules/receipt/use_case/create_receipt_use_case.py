from fastapi import HTTPException
from modules.receipt import CreateReceiptDTO, CreateReceiptRepository

class CreateReceiptUseCase:
    def __init__(self, repository=None):
        self.repository = repository or CreateReceiptRepository()

    def execute(self, data: CreateReceiptDTO):
        """
        Creates a new Receipt using the provided DTO.
        Args:
            data (CreateReceiptDTO): Data transfer object for creating a receipt.
        Returns:
            Receipt: The created Receipt object.
        Raises:
            HTTPException: If an error occurs during creation.
        """
        try:
            receipt = self.repository.create(data)
            return receipt
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Internal server error while creating receipt: {str(e)}")
        finally:
            self.repository.session.close()
