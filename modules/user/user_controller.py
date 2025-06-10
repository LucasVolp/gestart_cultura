from fastapi import APIRouter, Depends
from modules.user import UserService, UserResponse
from modules.user.dto.create_user_dto import CreateUserDTO
from modules.user.dto.update_user_dto import UpdateUserDTO
from fastapi.security import OAuth2PasswordRequestForm
from modules.user.utils.dependencies import requiredRole

router = APIRouter(prefix="/user", tags=["User"])

def getUserService():
    return UserService()

@router.post("/auth")
def auth(formData: OAuth2PasswordRequestForm = Depends(), service: UserService = Depends(getUserService)):
    """
    Authenticates a user based on email and password.
    
    Args:
        formData (OAuth2PasswordRequestForm): Form data containing email and password.
    
    Returns:
        Access token if authentication is successful.
    
    Raises:
        HTTPException: If authentication fails due to invalid credentials.
    """
    return service.authenticate(formData.username, formData.password)

@router.get("/", response_model=list[UserResponse])
def findAll(service: UserService = Depends(getUserService)):
    """
    Retrieves all users.
    
    Returns:
        List of all users.
    """
    return service.findAll()

@router.get("/{id}", response_model=UserResponse)
def findOne(id: str, service: UserService = Depends(getUserService)):
    """
    Retrieves a user by its ID.
    
    Args:
        id (str): The ID of the user to retrieve.
    
    Returns:
        User object if found.
    
    Raises:
        HTTPException: If the user is not found or if an error occurs.
    """
    return service.findOne(id)

@router.post("/", response_model=UserResponse)
def create(data: CreateUserDTO, service: UserService = Depends(getUserService)):
    """
    Creates a new user.
    
    Args:
        data (CreateUserDTO): Data for the new user.
    
    Returns:
        Created user object.
    
    Raises:
        HTTPException: If an error occurs during creation.
    """
    return service.create(data)
    
@router.patch("/{id}", response_model=UserResponse)
def update(id: str, data: UpdateUserDTO, service: UserService = Depends(getUserService)):
    """
    Updates an existing user.
    
    Args:
        id (str): The ID of the user to update.
        data (UpdateUserDTO): Updated data for the user.
    
    Returns:
        Updated user object.
    
    Raises:
        HTTPException: If the user is not found or if an error occurs during update.
    """
    return service.update(id, data)

@router.delete("/{id}")
def remove(id: str, service: UserService = Depends(getUserService)):
    """
    Deletes a user by its ID.
    
    Args:
        id (str): The ID of the user to delete.
    
    Returns:
        Message indicating successful deletion.
    
    Raises:
        HTTPException: If the user is not found or if an error occurs during deletion.
    """
    return service.remove(id)
