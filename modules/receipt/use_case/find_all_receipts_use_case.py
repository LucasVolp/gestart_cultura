from modules.receipt import FindAllReceiptsRepository

class FindAllReceiptsUseCase:
    def __init__(self, repository=None):
        self.repository = repository or FindAllReceiptsRepository()

    def execute(self):
        """
        Retrieves all receipts from the repository.
        Returns:
            list: List of Receipt objects.
        Raises:
            Exception: If an error occurs during retrieval.
        """
        try:
            receipts = self.repository.findAll()
            if not receipts:
                print("Nenhum recibo encontrado.")
                return []
            return receipts
        except Exception as e:
            print(f"Erro ao buscar recibos: {e}")
            raise e
        finally:
            self.repository.session.close()
