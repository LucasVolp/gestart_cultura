from modules.receipt import DeleteReceiptRepository, FindReceiptByIdRepository

class DeleteReceiptUseCase:
    def __init__(self, repository=None, findReceiptByIdRepo=None):
        self.repository = repository or DeleteReceiptRepository()
        self.findReceiptByIdRepo = findReceiptByIdRepo or FindReceiptByIdRepository()

    def execute(self, id: str):
        """
        Deletes a receipt by ID.

        Args:
            id (str): The ID of the receipt to delete.
        Returns:
            bool: True if deletion was successful.
        Raises:
            ValueError: If the receipt is not found.
            Exception: If an error occurs during deletion.
        """
        try:
            receipt = self.findReceiptByIdRepo.findById(id)
            if not receipt:
                raise ValueError(f"Recibo com ID {id} não encontrado.")
            
            self.repository.delete(receipt)
            print(f"Recibo com ID {id} deletado com sucesso.")
            return True
        except ValueError as e:
            print(e)
            raise e
        except Exception as e:
            print(f"Erro ao deletar recibo: {e}")
            raise e
        finally:
            self.repository.session.close()
            self.findReceiptByIdRepo.session.close()
