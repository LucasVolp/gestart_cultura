from modules.purchase.repository import FindAllPurchasesRepository
from fastapi import HTTPException

class FindAllPurchasesUseCase:
    """Use case for retrieving all Purchases."""
    
    def __init__(self, repository=None):
        self.repository = repository or FindAllPurchasesRepository()

    def execute(self):
        """Retrieves all purchases from the repository.

        Returns:
            list: List of Purchase objects.

        Raises:
            HTTPException: If an error occurs during retrieval.
        """
        try:
            purchases = self.repository.findAll()
            if not purchases:
                print("Nenhuma compra encontrada.")
                return []
            
            print(f"{len(purchases)} compra(s) encontrada(s).")
            return purchases
            
        except Exception as e:
            print(f"Erro ao buscar compras: {e}")
            raise HTTPException(status_code=500, detail="Erro interno do servidor ao buscar compras.")
        finally:
            self.repository.session.close()
