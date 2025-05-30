from modules.purchase import FindAllPurchasesRepository

class FindAllPurchasesUseCase:
    """
    Use case for retrieving all Purchases.
    """
    def __init__(self, repository=None):
        self.repository = repository or FindAllPurchasesRepository()

    def execute(self):
        """
        Retrieves all purchases from the repository.
        Returns:
            list: List of Purchase objects.
        Raises:
            Exception: If an error occurs during retrieval.
        """
        try:
            purchases = self.repository.findAll()
            if not purchases:
                print("Nenhuma compra encontrada.")
                return []
            return purchases
        except Exception as e:
            print(f"Erro ao buscar compras: {e}")
            raise e
        finally:
            self.repository.session.close()
