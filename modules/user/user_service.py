from modules.user.use_case import (
    CreateUserUseCase,
    DeleteUserUseCase,
    FindAllUsersUseCase,
    FindUserByIdUseCase,
    UpdateUserUseCase,
)
from modules.user.dto import CreateUserDTO, UpdateUserDTO

class UserService:
    def __init__(
        self, 
        CreateUserUseCase=CreateUserUseCase, 
        FindAllUsersUseCase=FindAllUsersUseCase, 
        FindUserByIdUseCase=FindUserByIdUseCase, 
        UpdateUserUseCase=UpdateUserUseCase, 
        DeleteUserUseCase=DeleteUserUseCase
    ):
        self.CreateUserUseCase = CreateUserUseCase()
        self.FindAllUsersUseCase = FindAllUsersUseCase()
        self.FindUserByIdUseCase = FindUserByIdUseCase()
        self.UpdateUserUseCase = UpdateUserUseCase()
        self.DeleteUserUseCase = DeleteUserUseCase()

    def create(self, data: CreateUserDTO):
        """
        Creates a new user using the CreateUserUseCase.

        Args:
            data: Data Transfer Object containing the user information to be created.
        
        Returns:
            Created user instance.
        """
        return self.CreateUserUseCase.execute(data)
    
    def findAll(self):
        """
        Retrieves all users using the FindAllUserUseCase.

        Returns:
            List of all user instances.
        """
        return self.FindAllUsersUseCase.execute()
    
    def findOne(self, id: str):
        """
        Finds a user by its ID using the FindUserByIdUseCase.

        Args:
            id: The ID of the user to be found.
        
        Returns:
            User instance with the specified ID.
        """
        return self.FindUserByIdUseCase.execute(id)
    
    def update(self, id: str, data: UpdateUserDTO):
        """
        Updates an existing user using the UpdateUserUseCase.

        Args:
            id: The ID of the user to be updated.
            data: Data Transfer Object containing the updated user information.
        
        Returns:
            Updated user instance.
        """
        return self.UpdateUserUseCase.execute(id, data)
    
    def remove(self, id: str):
        """
        Removes a user by its ID using the DeleteUserUseCase.

        Args:
            id: The ID of the user to be deleted.
        
        Returns:
            Deleted user instance.
        """
        return self.DeleteUserUseCase.execute(id)
