from modules.receipt import FindReceiptByIdRepository

class FindReceiptByIdUseCase:
    def __init__(self, repository=None):
        self.repository = repository or FindReceiptByIdRepository()

    def execute(self, id: str):
        """
        Finds a receipt by ID.

        Args:
            id (str): The ID of the receipt to find.
        Returns:
            Receipt: The found Receipt object or None if not found.
        Raises:
            Exception: If an error occurs during retrieval.
        """
        try:
            receipt = self.repository.findById(id)
            if not receipt:
                print(f"Recibo com ID {id} não encontrado.")
                return None
            return receipt
        except Exception as e:
            print(f"Erro ao buscar recibo: {e}")
            raise e
        finally:
            self.repository.session.close()
