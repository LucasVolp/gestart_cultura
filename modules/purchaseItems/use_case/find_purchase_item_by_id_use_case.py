from modules.purchaseItems import FindPurchaseItemByIdRepository

class FindPurchaseItemByIdUseCase:

    def __init__(self, repository=None):
        self.repository = repository or FindPurchaseItemByIdRepository()

    def execute(self, id):
        """
        Retrieves a purchase item by its ID from the repository.
        Args:
            id (str): The ID of the purchase item to retrieve.
        Returns:
            PurchaseItem | None: The PurchaseItem object if found, otherwise None.
        Raises:
            Exception: If an error occurs during retrieval.
        """
        try:
            purchaseItem = self.repository.findById(id)
            if not purchaseItem:
                print(f"Item de compra não encontrado.")
                return None
            return purchaseItem
        except Exception as e:
            print(f"Erro ao buscar item de compra por ID: {e}")
            raise e
        finally:
            self.repository.session.close()
