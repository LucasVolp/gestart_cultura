from models.models import User
from modules.user import CreateUserDTO, CreateUserRepository, FindUserByEmailRepository, FindUserByCpfRepository


class CreateUserUseCase:
    def __init__(self, userRepository=None, findUserByEmail=None, findUserByCpf=None):
        self.repository = userRepository or CreateUserRepository()
        self.findUserByEmail = findUserByEmail or FindUserByEmailRepository()
        self.findUserByCpf = findUserByCpf or FindUserByCpfRepository()

    def execute(self, data: CreateUserDTO) -> User:
        """
        Cria um novo usuário no banco de dados.
        :param data: Dados do usuário a ser criado.
        :return: Instância do modelo User criada.
        """
        try:
            userEmail = self.findUserByEmail.findByEmail(data.email)
            userCPF = self.findUserByCpf.findByCPF(data.cpf)
            if userEmail:
                raise ValueError("Usuário com este email já cadastrado.")
            if userCPF:
                raise ValueError("Usuário com este CPF já cadastrado.")
            user = self.repository.create(data)
            print(f"Usuário {user.name} criado com sucesso.")
            return user
        except Exception as e:
            print(f"Erro ao criar usuário: {e}")
            raise e
        finally:
            self.repository.session.close()