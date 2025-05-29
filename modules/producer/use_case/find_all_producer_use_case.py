from models.models import Producer
from modules.producer.repository.find_all_producers_repository import FindAllProducersRepository

class FindAllProducersUseCase:
    def __init__(self, repository = None):
        self.repository = repository or FindAllProducersRepository()

    def execute(self) -> list[Producer]:
        """
        Retorna todos os produtores do banco de dados.
        :return: Lista de instâncias do modelo Producer.
        """
        try:
            producers = self.repository.findAll()
            print(f"{len(producers)} produtores encontrados.")
            return producers
        except Exception as e:
            print(f"Erro ao buscar produtores: {e}")
            raise e
        finally:
            self.repository.session.close()