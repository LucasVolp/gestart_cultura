from modules.seller import CreateSellerRepository, CreateSellerDTO, FindSellerByCpfRepository, FindSellerByEmailRepository
from sqlalchemy.exc import IntegrityError

class CreateSellerUseCase:
    def __init__(self, repository=None, findSellerByCPF=None, findSellerByEmail=None):
        self.repository = repository or CreateSellerRepository()
        self.findSellerByCPF = findSellerByCPF or FindSellerByCpfRepository()
        self.findSellerByEmail = findSellerByEmail or FindSellerByEmailRepository()
    def execute(self, data: CreateSellerDTO):
        try:
            cpfExists = self.findSellerByCPF.findByCPF(data.cpf)
            if cpfExists:
                raise ValueError("Usuário com CPF já cadastrado.")
            emailExists = self.findSellerByEmail.findByEmail(data.email)
            if emailExists:
                raise ValueError("Usuário com email já cadastrado.")
            seller = self.repository.create(data)
            print(f"Vendedor {seller.name} criado com sucesso.")
            return seller
        except IntegrityError as e:
            raise ValueError("Usuário com CPF, email ou telefone já cadastrado.") from e
        except Exception as e:
            print(f"Erro ao criar vendedor: {e}")
            raise e
        finally:
            self.repository.session.close()