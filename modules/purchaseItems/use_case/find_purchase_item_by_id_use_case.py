from modules.purchaseItems.repository import FindPurchaseItemByIdRepository
from fastapi import HTTPException

class FindPurchaseItemByIdUseCase:
    """Use case for retrieving a PurchaseItem by its ID."""

    def __init__(self, repository=None):
        self.repository = repository or FindPurchaseItemByIdRepository()

    def execute(self, id: str):
        """Retrieves a purchase item by its ID.

        Args:
            id (str): The ID of the purchase item to retrieve.

        Returns:
            PurchaseItem: The found PurchaseItem object.

        Raises:
            HTTPException: If the purchase item is not found or an error occurs.
        """
        try:
            purchaseItem = self.repository.findById(id)
            if not purchaseItem:
                raise HTTPException(status_code=404, detail=f"Item da compra com ID {id} não encontrado.")
            
            print(f"Item da compra {purchaseItem.id} encontrado com sucesso.")
            return purchaseItem
            
        except HTTPException as e:
            print(f"Erro ao buscar item da compra: {e.detail}")
            raise e
        except Exception as e:
            print(f"Erro ao buscar item da compra: {e}")
            raise HTTPException(status_code=500, detail="Erro interno do servidor ao buscar item da compra.")
        finally:
            self.repository.session.close()
