from modules.purchase.repository import FindPurchaseByIdRepository
from fastapi import HTTPException

class FindPurchaseByIdUseCase:
    """Use case for retrieving a Purchase by its ID."""
    
    def __init__(self, repository=None):
        self.repository = repository or FindPurchaseByIdRepository()

    def execute(self, id: str):
        """Retrieves a purchase by its ID.

        Args:
            id (str): The ID of the purchase to retrieve.

        Returns:
            Purchase: The found Purchase object.

        Raises:
            HTTPException: If the purchase is not found or an error occurs.
        """
        try:
            purchase = self.repository.findById(id)
            if not purchase:
                raise HTTPException(status_code=404, detail=f"Compra com ID {id} não encontrada.")
            
            print(f"Compra {purchase.id} encontrada com sucesso.")
            return purchase
            
        except HTTPException as e:
            print(f"Erro ao buscar compra: {e.detail}")
            raise e
        except Exception as e:
            print(f"Erro ao buscar compra: {e}")
            raise HTTPException(status_code=500, detail="Erro interno do servidor ao buscar compra.")
        finally:
            self.repository.session.close()