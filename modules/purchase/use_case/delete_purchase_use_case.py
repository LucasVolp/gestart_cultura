from modules.purchase import DeletePurchaseRepository, FindPurchaseByIdRepository

class DeletePurchaseUseCase:
    """
    Use case for deleting a Purchase.
    """
    def __init__(self, repository=None, findPurchaseByIdRepo=None):
        self.repository = repository or DeletePurchaseRepository()
        self.findPurchaseByIdRepo = findPurchaseByIdRepo or FindPurchaseByIdRepository()

    def execute(self, id: str):
        """
        Deletes a purchase from the repository.
        Args:
            purchase (Purchase): The purchase object to delete.
        Returns:
            bool: True if deletion was successful.
        Raises:
            Exception: If an error occurs during deletion.
        """
        try:
            purchaseExists = self.findPurchaseByIdRepo.findById(id)
            if not purchaseExists:
                raise ValueError(f"Compra não encontrada.")
            purchase = self.repository.delete(purchaseExists)
            if purchase:
                print(f"Compra {purchase.id} deletada com sucesso.")
            return purchase
        except Exception as e:
            print(f"Erro ao deletar compra: {e}")
            raise e
        finally:
            self.repository.session.close()
            self.findPurchaseByIdRepo.session.close()