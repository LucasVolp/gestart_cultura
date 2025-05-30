from modules.receipt import CreateReceiptDTO, CreateReceiptRepository

class CreateReceiptUseCase:
    def __init__(self, repository=None):
        self.repository = repository or CreateReceiptRepository()

    def execute(self, data: CreateReceiptDTO):
        """
        Creates a new Receipt using the provided DTO.
        Args:
            data (CreateReceiptDTO): Data transfer object for creating a receipt.
        Returns:
            Receipt: The created Receipt object.
        Raises:
            Exception: If an error occurs during creation.
        """
        try:
            receipt = self.repository.create(data)
            print("Recibo criado com sucesso.")
            return receipt
        except Exception as e:
            print(f"Erro ao criar recibo: {e}")
            raise e
        finally:
            self.repository.session.close()
