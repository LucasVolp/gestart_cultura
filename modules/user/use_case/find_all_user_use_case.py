from modules.user import FindAllUsersRepository


class FindAllUserUseCase:
    def __init__(self, userRepository):
        self.userRepository = userRepository or FindAllUsersRepository()

    def execute(self) -> list:
        """
        Busca todos os usuários no banco de dados.

        :return: Lista de instâncias do modelo User.
        """
        try:
            users = self.userRepository.findAll()
            print(f"{len(users)} usuários encontrados.")
            return users
        except Exception as e:
            print(f"Erro ao buscar usuários: {e}")
            raise e
        finally:
            self.userRepository.session.close()