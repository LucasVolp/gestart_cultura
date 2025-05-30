from modules.purchaseItems import CreatePurchaseItemDTO, CreatePurchaseItemRepository

class CreatePurchaseItemUseCase:
    def __init__(self, repository=None):
        self.repository = repository or CreatePurchaseItemRepository()

    def execute(self, data: CreatePurchaseItemDTO):
        """
        Creates a new PurchaseItem using the provided DTO.
        Args:
            dto (CreatePurchaseItemDTO): Data transfer object for creating a purchase item.
        Returns:
            PurchaseItem: The created PurchaseItem object.
        Raises:
            Exception: If an error occurs during creation.
        """
        try:
            purchaseItem = self.repository.create(data)
            print("Erro ao criar Items:")
            return purchaseItem
        except Exception as e:
            print(f"Erro ao criar Items: {e}")
            raise e
        finally:
            self.repository.session.close()
