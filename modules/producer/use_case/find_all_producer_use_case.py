from models.models import Producer
from modules.producer import FindAllProducersRepository

class FindAllProducersUseCase:
    def __init__(self, repository = None):
        self.repository = repository or FindAllProducersRepository()

    def execute(self) -> list[Producer]:
        """        Executes the use case to find all producers.

        Raises:
            e: Exception if an error occurs during the operation.

        Returns:
            list[Producer]: List of Producer model instances.
        """
        try:
            producers = self.repository.findAll()
            if not producers:
                print("Nenhum produtor encontrado.")
                return []
            return producers
        except Exception as e:
            print(f"Erro ao buscar produtores: {e}")
            raise e
        finally:
            self.repository.session.close()