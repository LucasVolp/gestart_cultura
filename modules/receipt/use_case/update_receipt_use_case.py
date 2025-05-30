from modules.receipt import UpdateReceiptDTO, UpdateReceiptRepository, FindReceiptByIdRepository

class UpdateReceiptUseCase:
    def __init__(self, repository=None, findReceiptByIdRepo=None):
        self.repository = repository or UpdateReceiptRepository()
        self.findReceiptByIdRepo = findReceiptByIdRepo or FindReceiptByIdRepository()

    def execute(self, id: str, data: UpdateReceiptDTO):
        """
        Updates a receipt using the provided DTO.
        Args:
            id (str): The ID of the receipt to update.
            data (UpdateReceiptDTO): Data transfer object for updating a receipt.
        Returns:
            Receipt: The updated Receipt object.
        Raises:
            Exception: If an error occurs during update.
        """
        try:
            receiptExists = self.findReceiptByIdRepo.findById(id)
            if not receiptExists:
                raise ValueError(f"Recibo não encontrado.")
            receipt = self.repository.update(receiptExists, data)
            if receipt:
                print(f"Recibo {receipt.id} atualizado com sucesso.")
            return receipt
        except Exception as e:
            print(f"Erro ao atualizar recibo: {e}")
            raise e
        finally:
            self.repository.session.close()
            self.findReceiptByIdRepo.session.close()
