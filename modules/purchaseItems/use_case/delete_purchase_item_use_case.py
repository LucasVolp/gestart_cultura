from modules.purchaseItems.repository import DeletePurchaseItemRepository, FindPurchaseItemByIdRepository
from fastapi import HTTPException

class DeletePurchaseItemUseCase:
    """Use case for deleting a PurchaseItem."""
    
    def __init__(self, repository=None, findPurchaseItemByIdRepo=None):
        self.repository = repository or DeletePurchaseItemRepository()
        self.findPurchaseItemByIdRepo = findPurchaseItemByIdRepo or FindPurchaseItemByIdRepository()

    def execute(self, id: str):
        """Deletes a purchase item from the repository.

        Args:
            id (str): The ID of the purchase item to delete.

        Returns:
            PurchaseItem: The deleted PurchaseItem object.

        Raises:
            HTTPException: If the purchase item is not found or an error occurs during deletion.
        """
        try:
            purchaseItemExists = self.findPurchaseItemByIdRepo.findById(id)
            if not purchaseItemExists:
                raise HTTPException(status_code=404, detail=f"Item da compra com ID {id} não encontrado.")
            
            purchaseItem = self.repository.delete(purchaseItemExists)
            print(f"Item da compra {purchaseItem.id} deletado com sucesso.")
            return purchaseItem
            
        except HTTPException as e:
            print(f"Erro ao deletar item da compra: {e.detail}")
            raise e
        except Exception as e:
            print(f"Erro ao deletar item da compra: {e}")
            raise HTTPException(status_code=500, detail="Erro interno do servidor ao deletar item da compra.")
        finally:
            self.repository.session.close()
            self.findPurchaseItemByIdRepo.session.close()
