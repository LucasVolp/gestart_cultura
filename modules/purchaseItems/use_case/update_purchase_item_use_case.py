from modules.purchaseItems import UpdatePurchaseItemRepository, FindPurchaseItemByIdRepository, UpdatePurchaseItemDTO

class UpdatePurchaseItemUseCase:

    def __init__(self, repository=None, findPurchaseItemByIdRepo=None):
        self.repository = repository or UpdatePurchaseItemRepository()
        self.findPurchaseItemByIdRepo = findPurchaseItemByIdRepo or FindPurchaseItemByIdRepository()

    def execute(self, id, data: UpdatePurchaseItemDTO):
        """
        Updates an existing purchase item in the repository.
        Args:
            id (str): The ID of the purchase item to update.
            data (UpdatePurchaseItemDTO): Data transfer object containing updated purchase item data.
        Returns:
            PurchaseItem: The updated PurchaseItem object.
        Raises:
            Exception: If an error occurs during the update process.
        """
        try:
            purchaseItemExists = self.findPurchaseItemByIdRepo.findById(id)
            if not purchaseItemExists:
                raise ValueError(f"Item de compra não encontrado!")

            updatedPurchaseItem = self.repository.update(purchaseItemExists, data)
            print(f"Item de compra atualizado com sucesso.")
            return updatedPurchaseItem
        except Exception as e:
            print(f"Erro ao atualizar item de compra: {e}")
            raise e
        finally:
            self.repository.session.close()
            self.findPurchaseItemByIdRepo.session.close()
