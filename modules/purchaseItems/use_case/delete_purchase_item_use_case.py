from modules.purchaseItems import DeletePurchaseItemRepository, FindPurchaseItemByIdRepository

class DeletePurchaseItemUseCase:
    def __init__(self, repository=None, findPurchaseItemByIdRepo=None):
        self.repository = repository or DeletePurchaseItemRepository()
        self.findPurchaseItemByIdRepo = findPurchaseItemByIdRepo or FindPurchaseItemByIdRepository()

    def execute(self, id: str):
        """
        Deletes a purchase item from the repository.
        Args:
            id: str): The purchase item object to delete.
        Returns:
            bool: True if deletion was successful.
        Raises:
            Exception: If an error occurs during deletion.
        """
        try:
            purchaseItemsExists = self.findPurchaseItemByIdRepo.findById(id)
            if not purchaseItemsExists:
                raise ValueError(f"Item de compra não encontrado!")
            purchaseItem = self.repository.delete(purchaseItemsExists)
            if purchaseItem:
                print(f"Item de compra {purchaseItemsExists.id} deletado com sucesso.")
            return purchaseItem
        except Exception as e:
            print(f"Erro ao deletar item de compra: {e}")
            raise e
        finally:
            self.repository.session.close()
            self.findPurchaseItemByIdRepo.session.close()
