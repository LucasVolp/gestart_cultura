from modules.purchase import FindPurchaseByIdRepository

class FindPurchaseByIdUseCase:
    """
    Use case for retrieving a Purchase by its ID.
    """
    def __init__(self, repository=None):
        self.repository = repository or FindPurchaseByIdRepository()

    def execute(self, id: str):
        """
        Retrieves a purchase by its ID.
        Args:
            id (UUID): The ID of the purchase to retrieve.
        Returns:
            Purchase: The found Purchase object.
        Raises:
            Exception: If the purchase is not found or an error occurs.
        """
        try:
            purchase = self.repository.findById(id)
            if not purchase:
                raise ValueError(f"Compra não encontrada.")
            print(f"Compra {purchase.id} encontrada com sucesso.")
            return purchase
        except Exception as e:
            print(f"Erro ao buscar compra: {e}")
            raise e
        finally:
            self.repository.session.close()