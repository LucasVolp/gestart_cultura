from modules.purchaseItems.use_case import (
    CreatePurchaseItemUseCase,
    DeletePurchaseItemUseCase,
    FindAllPurchaseItemsUseCase,
    FindPurchaseItemByIdUseCase,
    UpdatePurchaseItemUseCase,
)
from modules.purchaseItems.dto import CreatePurchaseItemDTO, UpdatePurchaseItemDTO

class PurchaseItemsService:
    def __init__(
        self, 
        CreatePurchaseItemUseCase=CreatePurchaseItemUseCase, 
        FindAllPurchaseItemsUseCase=FindAllPurchaseItemsUseCase, 
        FindPurchaseItemByIdUseCase=FindPurchaseItemByIdUseCase, 
        UpdatePurchaseItemUseCase=UpdatePurchaseItemUseCase, 
        DeletePurchaseItemUseCase=DeletePurchaseItemUseCase
    ):
        self.CreatePurchaseItemUseCase = CreatePurchaseItemUseCase()
        self.FindAllPurchaseItemsUseCase = FindAllPurchaseItemsUseCase()
        self.FindPurchaseItemByIdUseCase = FindPurchaseItemByIdUseCase()
        self.UpdatePurchaseItemUseCase = UpdatePurchaseItemUseCase()
        self.DeletePurchaseItemUseCase = DeletePurchaseItemUseCase()

    def create(self, data: CreatePurchaseItemDTO):
        """
        Creates a new purchase item using the CreatePurchaseItemUseCase.

        Args:
            data: Data Transfer Object containing the purchase item information to be created.
        
        Returns:
            Created purchase item instance.
        """
        return self.CreatePurchaseItemUseCase.execute(data)
    
    def findAll(self):
        """
        Retrieves all purchase items using the FindAllPurchaseItemsUseCase.

        Returns:
            List of all purchase items.
        """
        return self.FindAllPurchaseItemsUseCase.execute()
    
    def findOne(self, id: str):
        """
        Retrieves a purchase item by ID using the FindPurchaseItemByIdUseCase.

        Args:
            id: ID of the purchase item to retrieve.
        
        Returns:
            PurchaseItem instance if found.
        """
        return self.FindPurchaseItemByIdUseCase.execute(id)
    
    def update(self, id: str, data: UpdatePurchaseItemDTO):
        """
        Updates a purchase item using the UpdatePurchaseItemUseCase.

        Args:
            id: ID of the purchase item to update.
            data: Data Transfer Object containing the updated purchase item information.
        
        Returns:
            Updated purchase item instance.
        """
        return self.UpdatePurchaseItemUseCase.execute(id, data)
    
    def remove(self, id: str):
        """
        Deletes a purchase item using the DeletePurchaseItemUseCase.

        Args:
            id: ID of the purchase item to delete.
        
        Returns:
            Result of the deletion operation.
        """
        return self.DeletePurchaseItemUseCase.execute(id)
