from modules.user.use_case import (
    CreateUserUseCase,
    DeleteUserUseCase,
    FindAllUsersUseCase,
    FindUserByIdUseCase,
    UpdateUserUseCase,
)
from modules.user.dto.create_user_dto import CreateUserDTO
from modules.user.dto.update_user_dto import UpdateUserDTO
from modules.user.auth import AuthenthicateUser

class UserService:
    def __init__(
        self, 
        CreateUserUseCase=CreateUserUseCase, 
        FindAllUsersUseCase=FindAllUsersUseCase, 
        FindUserByIdUseCase=FindUserByIdUseCase, 
        UpdateUserUseCase=UpdateUserUseCase, 
        DeleteUserUseCase=DeleteUserUseCase,
        AuthenthicateUser=AuthenthicateUser
    ):
        self.CreateUserUseCase = CreateUserUseCase()
        self.FindAllUsersUseCase = FindAllUsersUseCase()
        self.FindUserByIdUseCase = FindUserByIdUseCase()
        self.UpdateUserUseCase = UpdateUserUseCase()
        self.DeleteUserUseCase = DeleteUserUseCase()
        self.AuthenthicateUser = AuthenthicateUser()

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
    
    def authenticate(self, username: str, password: str):
        """
        Authenticates a user using the AuthenthicateUser use case.

        Args:
            username: The email of the user to be authenticated.
            password: The password of the user to be authenticated.
        
        Returns:
            Dictionary containing the access token and token type if authentication is successful.
        
        Raises:
            HTTPException: If authentication fails due to invalid credentials.
        """
        return self.AuthenthicateUser.execute(username, password)
