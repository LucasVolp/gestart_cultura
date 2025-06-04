from fastapi import APIRouter, Depends
from modules.tier import TierService, CreateTierDTO, UpdateTierDTO, TierResponse

router = APIRouter(prefix="/tier", tags=["Tier"])

def getTierService():
    return TierService()

@router.get("/", response_model=list[TierResponse])
def findAll(service: TierService = Depends(getTierService)):
    """
    Retrieves all tiers.
    
    Returns:
        List of all tiers.
    """
    return service.findAll()

@router.get("/{id}")
def findOne(id: str, service: TierService = Depends(getTierService)):
    """
    Retrieves a tier by its ID.
    
    Args:
        id (str): The ID of the tier to retrieve.
    
    Returns:
        Tier object if found.
    """
    return service.findOne(id)

@router.post("/")
def create(data: CreateTierDTO, service: TierService = Depends(getTierService)):
    """
    Creates a new tier.
    
    Args:
        data (CreateTierDTO): Data for the new tier.
    
    Returns:
        Created tier object.
    
    Raises:
        HTTPException: If an error occurs during creation.
    """
    return service.create(data)
    
@router.patch("/{id}")
def update(id: str, data: UpdateTierDTO, service: TierService = Depends(getTierService)):
    """
    Updates an existing tier.
    
    Args:
        id (str): The ID of the tier to update.
        data (UpdateTierDTO): Updated data for the tier.
    
    Returns:
        Updated tier object.
    
    """
    return service.update(id, data)

@router.delete("/{id}")
def remove(id: str, service: TierService = Depends(getTierService)):
    """
    Deletes a tier by its ID.
    
    Args:
        id (str): The ID of the tier to delete.
    
    Returns:
        Message indicating successful deletion.
    
    Raises:
        HTTPException: If the tier is not found or if an error occurs during deletion.
    """
    service.remove(id)
    return {"message": f"Tier with ID {id} deleted successfully."}
