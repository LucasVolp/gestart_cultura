from modules.tier.use_case import (
    CreateTierUseCase,
    DeleteTierUseCase,
    FindAllTierUseCase,
    FindTierByIdUseCase,
    UpdateTierUseCase,
)
from modules.tier.dto import CreateTierDTO, UpdateTierDTO

class TierService:
    def __init__(
        self, 
        CreateTierUseCase=CreateTierUseCase, 
        FindAllTierUseCase=FindAllTierUseCase, 
        FindTierByIdUseCase=FindTierByIdUseCase, 
        UpdateTierUseCase=UpdateTierUseCase, 
        DeleteTierUseCase=DeleteTierUseCase
    ):
        self.CreateTierUseCase = CreateTierUseCase()
        self.FindAllTierUseCase = FindAllTierUseCase()
        self.FindTierByIdUseCase = FindTierByIdUseCase()
        self.UpdateTierUseCase = UpdateTierUseCase()
        self.DeleteTierUseCase = DeleteTierUseCase()

    def create(self, data: CreateTierDTO):
        """
        Creates a new tier using the CreateTierUseCase.

        Args:
            data: Data Transfer Object containing the tier information to be created.
        
        Returns:
            Created tier instance.
        """
        return self.CreateTierUseCase.execute(data)
    
    def findAll(self):
        """
        Retrieves all tiers using the FindAllTierUseCase.

        Returns:
            List of all tiers.
        """
        return self.FindAllTierUseCase.execute()
    
    def findOne(self, id: str):
        """
        Retrieves a tier by ID using the FindTierByIdUseCase.

        Args:
            id: ID of the tier to retrieve.
        
        Returns:
            Tier instance if found.
        """
        return self.FindTierByIdUseCase.execute(id)
    
    def update(self, id: str, data: UpdateTierDTO):
        """
        Updates a tier using the UpdateTierUseCase.

        Args:
            id: ID of the tier to update.
            data: Data Transfer Object containing the updated tier information.
        
        Returns:
            Updated tier instance.
        """
        return self.UpdateTierUseCase.execute(id, data)
    
    def remove(self, id: str):
        """
        Deletes a tier using the DeleteTierUseCase.

        Args:
            id: ID of the tier to delete.
        
        Returns:
            Result of the deletion operation.
        """
        return self.DeleteTierUseCase.execute(id)
