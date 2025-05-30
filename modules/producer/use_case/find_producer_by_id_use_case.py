from models.models import Producer
from modules.producer import FindProducerByIdRepository

class FindProducerByIdUseCase:
    def __init__(self, repository = None):
        self.repository = repository or FindProducerByIdRepository()

    def execute(self, id: str) -> Producer:
        """
        Finds a producer by ID in the database.

        Args:
            id (str): ID of the producer to be found.

        Raises:
            ValueError: If the producer with the given ID does not exist.
            e: Exception raised during the search process.

        Returns:
            Producer: Producer model instance if found.
        """
        try:
            producer = self.repository.findById(id)
            if not producer:
                raise ValueError(f"Produtor com ID {id} não encontrado.")
            print(f"Produtor {producer.name} encontrado com sucesso.")
            return producer
        except Exception as e:
            print(f"Erro ao buscar produtor: {e}")
            raise e
        finally:
            self.repository.session.close()