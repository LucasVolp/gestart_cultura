from modules.user import FindUserByIdRepository


class FindUserByIdUseCase:
    def __init__(self, userRepository):
        self.userRepository = userRepository or FindUserByIdRepository()

    def execute(self, id: str):
        """
        Encontra um usuário pelo ID no banco de dados.

        :param id: ID do usuário a ser encontrado.
        :return: Instância do modelo User ou None se não encontrado.
        """
        try:
            user = self.userRepository.findById(id)
            if not user:
                raise ValueError(f"Usuário não encontrado.")
            print(f"Usuário {user.name} encontrado com sucesso.")
            return user
        except Exception as e:
            print(f"Erro ao buscar usuário: {e}")
            raise e
        finally:
            self.userRepository.session.close()