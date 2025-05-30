from modules.user import FindUserByIdRepository


class FindUserByIdUseCase:
    def __init__(self, userRepository):
        self.userRepository = userRepository or FindUserByIdRepository()

    def execute(self, id: str):
        """Finds a user by ID in the database.

        Args:
            id (str): ID of the user to be found.

        Raises:
            ValueError: If the user with the given ID does not exist.
            e: Exception raised during the search process.

        Returns:
            _type_: User model instance if found, None otherwise.
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