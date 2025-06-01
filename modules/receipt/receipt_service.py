from modules.receipt.use_case import (
    CreateReceiptUseCase,
    DeleteReceiptUseCase,
    FindAllReceiptsUseCase,
    FindReceiptByIdUseCase,
    UpdateReceiptUseCase,
)
from modules.receipt.dto import CreateReceiptDTO, UpdateReceiptDTO

class ReceiptService:
    def __init__(
        self, 
        CreateReceiptUseCase=CreateReceiptUseCase, 
        FindAllReceiptsUseCase=FindAllReceiptsUseCase, 
        FindReceiptByIdUseCase=FindReceiptByIdUseCase, 
        UpdateReceiptUseCase=UpdateReceiptUseCase, 
        DeleteReceiptUseCase=DeleteReceiptUseCase
    ):
        self.CreateReceiptUseCase = CreateReceiptUseCase()
        self.FindAllReceiptsUseCase = FindAllReceiptsUseCase()
        self.FindReceiptByIdUseCase = FindReceiptByIdUseCase()
        self.UpdateReceiptUseCase = UpdateReceiptUseCase()
        self.DeleteReceiptUseCase = DeleteReceiptUseCase()

    def create(self, data: CreateReceiptDTO):
        """
        Creates a new receipt using the CreateReceiptUseCase.

        Args:
            data: Data Transfer Object containing the receipt information to be created.
        
        Returns:
            Created receipt instance.
        """
        return self.CreateReceiptUseCase.execute(data)
    
    def findAll(self):
        """
        Retrieves all receipts using the FindAllReceiptsUseCase.

        Returns:
            List of all receipts.
        """
        return self.FindAllReceiptsUseCase.execute()
    
    def findOne(self, id: str):
        """
        Retrieves a receipt by its ID using the FindReceiptByIdUseCase.

        Args:
            id: The ID of the receipt to retrieve.
        
        Returns:
            Receipt instance if found.
        """
        return self.FindReceiptByIdUseCase.execute(id)
    
    def update(self, id: str, data: UpdateReceiptDTO):
        """
        Updates an existing receipt using the UpdateReceiptUseCase.

        Args:
            id: The ID of the receipt to update.
            data: Data Transfer Object containing the updated receipt information.
        
        Returns:
            Updated receipt instance.
        """
        return self.UpdateReceiptUseCase.execute(id, data)
    
    def remove(self, id: str):
        """
        Deletes a receipt by its ID using the DeleteReceiptUseCase.

        Args:
            id: The ID of the receipt to delete.
        
        Returns:
            Boolean indicating successful deletion.
        """
        return self.DeleteReceiptUseCase.execute(id)
