from modules.producer.dto.create_producer_dto import CreateProducerDTO
from modules.producer.repository.create_producer_repository import CreateProducerRepository
from models.models import Producer

class CreateProducerUseCase:
    def __init__(self, ProducerRepository = None):
        self.repository = ProducerRepository or CreateProducerRepository()

    def execute(self, data: CreateProducerDTO) -> Producer:
        """
        Cria um novo produtor no banco de dados.

        :param data: Dados do produtor a ser criado.
        :return: Instância do modelo Producer criada.
        """
        try:
            producer = self.repository.create(data)
            print(f"Produtor {producer.name} criado com sucesso.")
            return producer
        except Exception as e:
            print(f"Erro ao criar produtor: {e}")
            raise e
        finally:
            self.repository.session.close()