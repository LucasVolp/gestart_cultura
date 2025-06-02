from fastapi import APIRouter, Depends
from modules.rating import RatingService, CreateRatingDTO, UpdateRatingDTO

router = APIRouter(prefix="/rating", tags=["Rating"])

def getRatingService():
    return RatingService()

@router.get("/")
def findAll(service: RatingService = Depends(getRatingService)):
    """
    Retrieves all ratings.
    
    Returns:
        List of all ratings.
    """
    return service.findAll()

    
@router.get("/{id}")
def findOne(id: str, service: RatingService = Depends(getRatingService)):
    """
    Retrieves a rating by its ID.
    
    Args:
        id (str): The ID of the rating to retrieve.
    
    Returns:
        Rating object if found.
    
    Raises:
        HTTPException: If the rating is not found or if an error occurs.
    """
    return service.findOne(id)

@router.post("/")
def create(data: CreateRatingDTO, service: RatingService = Depends(getRatingService)):
    """
    Creates a new rating.
    
    Args:
        data (dict): Data for the new rating.
    
    Returns:
        Created rating object.
    
    Raises:
        HTTPException: If an error occurs during creation.
    """
    return service.create(data)
    
@router.patch("/{id}")
def update(id: str, data: UpdateRatingDTO, service: RatingService = Depends(getRatingService)):
    """
    Updates an existing rating.
    
    Args:
        id (str): The ID of the rating to update.
        data (dict): Updated data for the rating.
    
    Returns:
        Updated rating object.
    
    Raises:
        HTTPException: If the rating is not found or if an error occurs during update.
    """
    return service.update(id, data)

    
@router.delete("/{id}")
def remove(id: str, service: RatingService = Depends(getRatingService)):
    """
    Deletes a rating by its ID.
    
    Args:
        id (str): The ID of the rating to delete.
    
    Returns:
        Message indicating successful deletion.
    
    Raises:
        HTTPException: If the rating is not found or if an error occurs during deletion.
    """
    return service.remove(id)
