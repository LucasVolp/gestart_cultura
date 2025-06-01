from modules.purchaseItems.repository import FindAllPurchaseItemsRepository
from fastapi import HTTPException

class FindAllPurchaseItemsUseCase:
    """Use case for retrieving all PurchaseItems."""
    
    def __init__(self, repository=None):
        self.repository = repository or FindAllPurchaseItemsRepository()

    def execute(self):
        """Retrieves all purchase items from the repository.

        Returns:
            list: List of PurchaseItem objects.

        Raises:
            HTTPException: If an error occurs during retrieval.
        """
        try:
            purchaseItems = self.repository.findAll()
            if not purchaseItems:
                print("Nenhum item de compra encontrado.")
                return []
            
            print(f"{len(purchaseItems)} item(s) de compra encontrado(s).")
            return purchaseItems
            
        except Exception as e:
            print(f"Erro ao buscar itens de compra: {e}")
            raise HTTPException(status_code=500, detail="Erro interno do servidor ao buscar itens de compra.")
        finally:
            self.repository.session.close()
