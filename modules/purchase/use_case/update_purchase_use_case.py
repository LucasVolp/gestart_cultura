from modules.purchase import UpdatePurchaseDTO, FindPurchaseByIdRepository, UpdatePurchaseRepository

class UpdatePurchaseUseCase:
    def __init__(self, repository=None, findPurchaseByIdRepo=None):
        self.repository = repository or UpdatePurchaseRepository()
        self.findPurchaseByIdRepo = findPurchaseByIdRepo or FindPurchaseByIdRepository()

    def execute(self, id: str, data: UpdatePurchaseDTO):
        """
        Updates a purchase using the provided DTO.
        Args:
            purchase (Purchase): The purchase object to update.
            dto (UpdatePurchaseDTO): Data transfer object for updating a purchase.
        Returns:
            Purchase: The updated Purchase object.
        Raises:
            Exception: If an error occurs during update.
        """
        try:
            purchaseExists = self.findPurchaseByIdRepo.findById(id)
            if not purchaseExists:
                raise ValueError(f"Compra não encontrada.")
            purchase = self.repository.update(purchaseExists, data)
            if purchase:
                print(f"Compra {purchase.id} atualizada com sucesso.")
            return purchase
        except Exception as e:
            print(f"Erro ao atualizar compra: {e}")
            raise e
        finally:
            self.repository.session.close()
            self.findPurchaseByIdRepo.session.close()
