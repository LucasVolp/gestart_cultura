from modules.purchaseItems.repository import CreatePurchaseItemRepository
from modules.purchaseItems.dto import CreatePurchaseItemDTO
from modules.purchase.repository import FindPurchaseByIdRepository
from modules.tier.repository import FindTierByIdRepository
from fastapi import HTTPException

class CreatePurchaseItemUseCase:
    def __init__(self, repository=None, findPurchaseById=None, findTierById=None):
        self.repository = repository or CreatePurchaseItemRepository()
        self.findPurchaseById = findPurchaseById or FindPurchaseByIdRepository()
        self.findTierById = findTierById or FindTierByIdRepository()

    def execute(self, data: CreatePurchaseItemDTO):
        """Executes the use case to create a new purchase item.

        Args:
            data (CreatePurchaseItemDTO): Data Transfer Object containing the purchase item information to be created.

        Raises:
            HTTPException: If purchase or tier doesn't exist, or if an error occurs during creation.

        Returns:
            PurchaseItem: Created PurchaseItem model instance.
        """
        try:
            purchase = self.findPurchaseById.findById(data.purchaseId)
            if not purchase:
                raise HTTPException(status_code=404, detail=f"Compra com ID {data.purchaseId} não encontrada.")

            tier = self.findTierById.findById(data.tierId)
            if not tier:
                raise HTTPException(status_code=404, detail=f"Tier com ID {data.tierId} não encontrado.")

            purchaseItem = self.repository.create(data)
            print(f"Item da compra '{purchaseItem.id}' criado com sucesso para a compra {purchase.id}.")
            return purchaseItem
            
        except HTTPException as e:
            print(f"Erro ao criar item da compra: {e.detail}")
            raise e
        except Exception as e:
            print(f"Erro ao criar item da compra: {e}")
            raise HTTPException(status_code=500, detail="Erro interno do servidor ao criar item da compra.")
        finally:
            self.repository.session.close()
            if hasattr(self.findPurchaseById, 'session'):
                self.findPurchaseById.session.close()
            if hasattr(self.findTierById, 'session'):
                self.findTierById.session.close()
