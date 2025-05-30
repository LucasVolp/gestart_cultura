from models.models import Producer
from modules.producer import UpdateProducerDTO
from modules.producer import FindProducerByIdRepository
from modules.producer import UpdateProducerRepository

class UpdateProducerUseCase:
    def __init__(self, ProducerRepository = None, findProducer = None):
        self.repository = ProducerRepository or UpdateProducerRepository()
        self.findRepository = findProducer or FindProducerByIdRepository()

    def execute(self, id: str, data: UpdateProducerDTO) -> Producer:
        """Update a producer by ID in the database.

        Args:
            id (str): ID of the producer to be updated.
            data (UpdateProducerDTO): Data transfer object containing the updated producer information.

        Raises:
            ValueError: If the producer with the given ID does not exist.
            e: Exception raised during the update process.

        Returns:
            Producer: Updated Producer model instance if successful, None if not found.
        """
        try:
            producerExists = self.findRepository.findById(id)
            if not producerExists:
                raise ValueError(f"Produtor não encontrado.")
            producer = self.repository.update(producerExists, data)
            if producer:
                print(f"Produtor {producer.name} atualizado com sucesso.")
            return producer
        except Exception as e:
            print(f"Erro ao atualizar produtor: {e}")
            raise e
        finally:
            self.repository.session.close()