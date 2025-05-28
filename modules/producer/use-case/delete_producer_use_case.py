from models.models import Producer
from modules.producer.repository.delete_producer_repository import DeleteProducerRepository
from modules.producer.repository.find_producer_by_id_repository import FindProducerByIdRepository

class DeleteProducerUseCase:
    def __init__(self, repository=DeleteProducerRepository(), FindProducerByIdRepository=FindProducerByIdRepository()):
        self.repository = repository
        self.findRepository = FindProducerByIdRepository

    def execute(self, id: str) -> bool:
        """
        Deleta um produtor do banco de dados pelo ID.

        :param id: ID do produtor a ser deletado.
        :return: True se o produtor foi deletado com sucesso, False caso contrário.
        """
        try:
            producerExists = self.findRepository.findById(id)
            if not producerExists:
                raise ValueError(f"Produtor não encontrado.")
            producer = self.repository.delete(id)
            print(f"Produtor deletado com sucesso.")
            return producer
        except Exception as e:
            print(f"Erro ao deletar produtor: {e}")
            raise e
        finally:
            self.repository.session.close()