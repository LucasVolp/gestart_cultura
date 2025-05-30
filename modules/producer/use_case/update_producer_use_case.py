from models.models import Producer
from modules.producer import UpdateProducerDTO
from modules.producer import FindProducerByIdRepository
from modules.producer import UpdateProducerRepository

class UpdateProducerUseCase:
    def __init__(self, ProducerRepository = None, findProducer = None):
        self.repository = ProducerRepository or UpdateProducerRepository()
        self.findRepository = findProducer or FindProducerByIdRepository()

    def execute(self, id: str, data: UpdateProducerDTO) -> Producer:
        """
        Atualiza um produtor existente no banco de dados.

        :param id: ID do produtor a ser atualizado.
        :param data: Dados do produtor a serem atualizados.
        :return: Instância do modelo Producer atualizada.
        """
        try:
            producerExists = self.findRepository.findById(id)
            if not producerExists:
                raise ValueError(f"Produtor não encontrado.")
            producer = self.repository.update(id, data)
            print(f"Produtor {producer.name} atualizado com sucesso.")
            return producer
        except Exception as e:
            print(f"Erro ao atualizar produtor: {e}")
            raise e
        finally:
            self.repository.session.close()