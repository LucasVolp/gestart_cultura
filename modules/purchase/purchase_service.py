from modules.purchase.use_case import (
    CreatePurchaseUseCase,
    DeletePurchaseUseCase,
    FindAllPurchasesUseCase,
    FindPurchaseByIdUseCase,
    UpdatePurchaseUseCase,
)
from modules.purchase.dto import CreatePurchaseDTO, UpdatePurchaseDTO

class PurchaseService:
    def __init__(
        self, 
        CreatePurchaseUseCase=CreatePurchaseUseCase, 
        FindAllPurchasesUseCase=FindAllPurchasesUseCase, 
        FindPurchaseByIdUseCase=FindPurchaseByIdUseCase, 
        UpdatePurchaseUseCase=UpdatePurchaseUseCase, 
        DeletePurchaseUseCase=DeletePurchaseUseCase
    ):
        self.CreatePurchaseUseCase = CreatePurchaseUseCase()
        self.FindAllPurchasesUseCase = FindAllPurchasesUseCase()
        self.FindPurchaseByIdUseCase = FindPurchaseByIdUseCase()
        self.UpdatePurchaseUseCase = UpdatePurchaseUseCase()
        self.DeletePurchaseUseCase = DeletePurchaseUseCase()

    def create(self, data: CreatePurchaseDTO):
        """
        Creates a new purchase using the CreatePurchaseUseCase.

        Args:
            data: Data Transfer Object containing the purchase information to be created.
        
        Returns:
            Created purchase instance.
        """
        return self.CreatePurchaseUseCase.execute(data)
    
    def findAll(self):
        """
        Retrieves all purchases using the FindAllPurchasesUseCase.

        Returns:
            List of all purchases.
        """
        return self.FindAllPurchasesUseCase.execute()
    
    def findOne(self, id: str):
        """
        Retrieves a purchase by ID using the FindPurchaseByIdUseCase.

        Args:
            id: ID of the purchase to retrieve.
        
        Returns:
            Purchase instance if found.
        """
        return self.FindPurchaseByIdUseCase.execute(id)
    
    def update(self, id: str, data: UpdatePurchaseDTO):
        """
        Updates a purchase using the UpdatePurchaseUseCase.

        Args:
            id: ID of the purchase to update.
            data: Data Transfer Object containing the updated purchase information.
        
        Returns:
            Updated purchase instance.
        """
        return self.UpdatePurchaseUseCase.execute(id, data)
    
    def remove(self, id: str):
        """
        Deletes a purchase using the DeletePurchaseUseCase.

        Args:
            id: ID of the purchase to delete.
        
        Returns:
            Result of the deletion operation.
        """
        return self.DeletePurchaseUseCase.execute(id)
