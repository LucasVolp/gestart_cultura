from modules.producer.dto.create_producer_dto import CreateProducerDTO
from modules.producer.repository.create_producer_repository import CreateProducerRepository
from models.models import Producer
from modules.producer.repository.find_producer_by_cpf_repository import FindProducerByCPFRepository
from modules.producer.repository.find_producer_by_email_repository import FindProducerByEmailRepository

class CreateProducerUseCase:
    def __init__(self, ProducerRepository, findProducerByEmail, findProducerByCPF):
        self.repository = ProducerRepository or CreateProducerRepository()
        self.findProducerByEmail = findProducerByEmail or FindProducerByEmailRepository()
        self.findProducerByCPF = findProducerByCPF or FindProducerByCPFRepository()

    def execute(self, data: CreateProducerDTO) -> Producer:
        """
        Cria um novo produtor no banco de dados.

        :param data: Dados do produtor a ser criado.
        :return: Instância do modelo Producer criada.
        """
        try:
            producerEmail = self.findProducerByEmail.findByEmail(data.email)
            producerCPF = self.findProducerByCPF.findByCPF(data.cpf)
            if producerEmail:
                raise ValueError("Produtor com este email já cadastrado.")
            if producerCPF:
                raise ValueError("Produtor com este CPF já cadastrado.")
            producer = self.repository.create(data)
            print(f"Produtor {producer.name} criado com sucesso.")
            return producer
        except Exception as e:
            print(f"Erro ao criar produtor: {e}")
            raise e
        finally:
            self.repository.session.close()