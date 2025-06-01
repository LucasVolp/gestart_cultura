from fastapi import APIRouter, Depends, HTTPException
from modules.user import UserService, CreateUserDTO, UpdateUserDTO

router = APIRouter(prefix="/user", tags=["User"])

def getUserService():
    return UserService()

@router.get("/")
def findAll(service: UserService = Depends(getUserService)):
    """
    Retrieves all users.
    
    Returns:
        List of all users.
    """
    return service.findAll()

@router.get("/{id}")
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

@router.post("/")
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
    
@router.patch("/{id}")
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
    service.remove(id)
    return {"message": f"User with ID {id} deleted successfully."}
