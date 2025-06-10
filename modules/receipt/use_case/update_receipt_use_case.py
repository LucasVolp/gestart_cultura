from fastapi import HTTPException
from modules.receipt import UpdateReceiptDTO, UpdateReceiptRepository, FindReceiptByIdRepository

class UpdateReceiptUseCase:
    def __init__(self, repository=None, findReceiptByIdRepo=None):
        self.repository = repository or UpdateReceiptRepository()
        self.findReceiptByIdRepo = findReceiptByIdRepo or FindReceiptByIdRepository()

    def execute(self, id: str, data: UpdateReceiptDTO):
        """
        Updates a receipt using the provided DTO.
        Args:
            id (str): The ID of the receipt to update.
            data (UpdateReceiptDTO): Data transfer object for updating a receipt.
        Returns:
            Receipt: The updated Receipt object.
        Raises:
            HTTPException: If receipt is not found or an error occurs during update.
        """
        try:
            receiptExists = self.findReceiptByIdRepo.findById(id)
            if not receiptExists:
                raise HTTPException(status_code=404, detail=f"Receipt with ID {id} not found")
            
            if data.isEmpty():
                raise HTTPException(status_code=400, detail="No data provided for update")
            
            receipt = self.repository.update(receiptExists, data)
            return receipt
        except HTTPException:
            raise
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Internal server error while updating receipt: {str(e)}")
        finally:
            self.repository.session.close()
            self.findReceiptByIdRepo.session.close()
