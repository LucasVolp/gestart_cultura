from models.models import Producer
from modules.producer import DeleteProducerRepository
from modules.producer import FindProducerByIdRepository

class DeleteProducerUseCase:
    def __init__(self, producerRepository = None, findProducer = None):
        self.repository = producerRepository or DeleteProducerRepository()
        self.findRepository = findProducer or FindProducerByIdRepository()

    def execute(self, id: str) -> bool:
        """Delete a producer by ID from the database.

        Args:
            id (str): ID of the producer to be deleted.

        Raises:
            ValueError: If the producer with the given ID does not exist.
            Exception: If an error occurs during the deletion process.
            e: Exception raised during the deletion process.

        Returns:
            bool: True if the producer was successfully deleted, False otherwise.
        """
        try:
            producerExists = self.findRepository.findById(id)
            if not producerExists:
                raise ValueError(f"Produtor não encontrado.")
            producer = self.repository.delete(producerExists)
            if producer:
                print(f"Produtor {producerExists.name} deletado com sucesso.")
            return producer
        except Exception as e:
            print(f"Erro ao deletar produtor: {e}")
            raise e
        finally:
            self.repository.session.close()