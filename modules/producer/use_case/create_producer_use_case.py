from modules.producer import CreateProducerDTO
from modules.producer import CreateProducerRepository
from modules.producer import FindProducerByCpfRepository
from modules.producer import FindProducerByEmailRepository
from models.models import Producer

class CreateProducerUseCase:
    def __init__(self, ProducerRepository, findProducerByEmail, findProducerByCPF):
        self.repository = ProducerRepository or CreateProducerRepository()
        self.findProducerByEmail = findProducerByEmail or FindProducerByEmailRepository()
        self.findProducerByCPF = findProducerByCPF or FindProducerByCpfRepository()

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