from modules.purchase import CreatePurchaseDTO, CreatePurchaseRepository


class CreatePurchaseUseCase:
    def __init__(self, repository=None):
        self.repository = repository or CreatePurchaseRepository()

    def execute(self, data: CreatePurchaseDTO):
        """
        Creates a new Purchase using the provided DTO.
        Args:
            dto (CreatePurchaseDTO): Data transfer object for creating a purchase.
        Returns:
            Purchase: The created Purchase object.
        Raises:
            Exception: If an error occurs during creation.
        """
        try:
            purchase = self.repository.create(data)
            print("Compra realizada com sucesso.")
            return purchase
        except Exception as e:
            print(f"Erro ao registrar compra {e}")
            raise e
        finally:
            self.repository.session.close()
