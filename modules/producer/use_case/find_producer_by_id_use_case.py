from models.models import Producer
from modules.producer import FindProducerByIdRepository

class FindProducerByIdUseCase:
    def __init__(self, repository = None):
        self.repository = repository or FindProducerByIdRepository()

    def execute(self, id: str) -> Producer:
        """
        Encontra um produtor pelo ID no banco de dados.

        :param id: ID do produtor a ser encontrado.
        :return: Instância do modelo Producer ou None se não encontrado.
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