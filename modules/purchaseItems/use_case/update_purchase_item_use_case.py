from modules.purchaseItems.repository import UpdatePurchaseItemRepository, FindPurchaseItemByIdRepository
from modules.purchaseItems.dto import UpdatePurchaseItemDTO
from modules.purchase.repository import FindPurchaseByIdRepository
from modules.tier.repository import FindTierByIdRepository
from fastapi import HTTPException

class UpdatePurchaseItemUseCase:
    def __init__(self, repository=None, findPurchaseItemByIdRepo=None, findPurchaseById=None, findTierById=None):
        self.repository = repository or UpdatePurchaseItemRepository()
        self.findPurchaseItemByIdRepo = findPurchaseItemByIdRepo or FindPurchaseItemByIdRepository()
        self.findPurchaseById = findPurchaseById or FindPurchaseByIdRepository()
        self.findTierById = findTierById or FindTierByIdRepository()

    def execute(self, id: str, data: UpdatePurchaseItemDTO):
        """Updates a purchase item using the provided DTO.

        Args:
            id (str): The ID of the purchase item to update.
            data (UpdatePurchaseItemDTO): Data transfer object for updating a purchase item.

        Returns:
            PurchaseItem: The updated PurchaseItem object.

        Raises:
            HTTPException: If the purchase item is not found, related entities don't exist, or an error occurs.
        """
        try:
            purchaseItemExists = self.findPurchaseItemByIdRepo.findById(id)
            if not purchaseItemExists:
                raise HTTPException(status_code=404, detail=f"Item da compra com ID {id} não encontrado.")
            
            if data.purchaseId is not None:
                purchase = self.findPurchaseById.findById(data.purchaseId)
                if not purchase:
                    raise HTTPException(status_code=404, detail=f"Compra com ID {data.purchaseId} não encontrada.")

            if data.tierId is not None:
                tier = self.findTierById.findById(data.tierId)
                if not tier:
                    raise HTTPException(status_code=404, detail=f"Tier com ID {data.tierId} não encontrado.")
            
            if data.isEmpty():
                raise HTTPException(status_code=400, detail="Nenhum dado fornecido para atualização.")
            
            updatedPurchaseItem = self.repository.update(purchaseItemExists, data)
            print(f"Item da compra {updatedPurchaseItem.id} atualizado com sucesso.")
            return updatedPurchaseItem
            
        except HTTPException as e:
            print(f"Erro ao atualizar item da compra: {e.detail}")
            raise e
        except Exception as e:
            print(f"Erro ao atualizar item da compra: {e}")
            raise HTTPException(status_code=500, detail="Erro interno do servidor ao atualizar item da compra.")
        finally:
            self.repository.session.close()
            self.findPurchaseItemByIdRepo.session.close()
            if hasattr(self.findPurchaseById, 'session'):
                self.findPurchaseById.session.close()
            if hasattr(self.findTierById, 'session'):
                self.findTierById.session.close()
