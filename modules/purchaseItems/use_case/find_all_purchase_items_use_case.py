from modules.purchaseItems import FindAllPurchaseItemsRepository

class FindAllPurchaseItemsUseCase:
    def __init__(self, repository=None):
        self.repository = repository or FindAllPurchaseItemsRepository()

    def execute(self):
        """
        Retrieves all purchase items from the repository.
        Returns:
            list: List of PurchaseItem objects.
        Raises:
            Exception: If an error occurs during retrieval.
        """
        try:
            purchaseItems = self.repository.findAll()
            if not purchaseItems:
                print("Nenhum item de compra encontrado.")
                return []
            return purchaseItems
        except Exception as e:
            print(f"Erro ao buscar itens de compra: {e}")
            raise e
        finally:
            self.repository.session.close()
