from modules.purchase.repository import DeletePurchaseRepository, FindPurchaseByIdRepository
from fastapi import HTTPException

class DeletePurchaseUseCase:
    """Use case for deleting a Purchase."""
    
    def __init__(self, repository=None, findPurchaseByIdRepo=None):
        self.repository = repository or DeletePurchaseRepository()
        self.findPurchaseByIdRepo = findPurchaseByIdRepo or FindPurchaseByIdRepository()

    def execute(self, id: str):
        """Deletes a purchase from the repository.

        Args:
            id (str): The ID of the purchase to delete.

        Returns:
            Purchase: The deleted Purchase object.

        Raises:
            HTTPException: If the purchase is not found or an error occurs during deletion.
        """
        try:
            purchaseExists = self.findPurchaseByIdRepo.findById(id)
            if not purchaseExists:
                raise HTTPException(status_code=404, detail=f"Compra com ID {id} não encontrada.")

            purchase = self.repository.delete(purchaseExists)
            print(f"Compra {purchase.id} deletada com sucesso.")
            return purchase
            
        except HTTPException as e:
            print(f"Erro ao deletar compra: {e.detail}")
            raise e
        except Exception as e:
            print(f"Erro ao deletar compra: {e}")
            raise HTTPException(status_code=500, detail="Erro interno do servidor ao deletar compra.")
        finally:
            self.repository.session.close()
            self.findPurchaseByIdRepo.session.close()