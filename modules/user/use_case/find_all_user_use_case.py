from modules.user import FindAllUsersRepository


class FindAllUserUseCase:
    def __init__(self, userRepository):
        self.userRepository = userRepository or FindAllUsersRepository()

    def execute(self) -> list:
        """        Executes the use case to find all users.

        Raises:
            e: Exception if an error occurs during the operation.

        Returns:
            list: List of User model instances or an empty list if no users are found.
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