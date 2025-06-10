from fastapi import APIRouter, Depends, HTTPException
from modules.purchaseItems import PurchaseItemsService, CreatePurchaseItemDTO, UpdatePurchaseItemDTO

router = APIRouter(prefix="/purchase-items", tags=["PurchaseItems"])

def getPurchaseItemsService():
    return PurchaseItemsService()

@router.get("/")
def findAll(service: PurchaseItemsService = Depends(getPurchaseItemsService)):
    """
    Retrieves all purchase items.
    
    Returns:
        List of all purchase items.
    """
    return service.findAll()

@router.get("/{id}")
def findOne(id: str, service: PurchaseItemsService = Depends(getPurchaseItemsService)):
    """
    Retrieves a purchase item by its ID.
    
    Args:
        id (str): The ID of the purchase item to retrieve.
    
    Returns:
        PurchaseItem object if found.
    
    Raises:
        HTTPException: If the purchase item is not found or if an error occurs.
    """
    return service.findOne(id)

@router.post("/")
def create(data: CreatePurchaseItemDTO, service: PurchaseItemsService = Depends(getPurchaseItemsService)):
    """
    Creates a new purchase item.
    
    Args:
        data (CreatePurchaseItemDTO): Data for the new purchase item.
    
    Returns:
        Created purchase item object.
    
    Raises:
        HTTPException: If an error occurs during creation.
    """
    return service.create(data)
    
@router.patch("/{id}")
def update(id: str, data: UpdatePurchaseItemDTO, service: PurchaseItemsService = Depends(getPurchaseItemsService)):
    """
    Updates an existing purchase item.
    
    Args:
        id (str): The ID of the purchase item to update.
        data (UpdatePurchaseItemDTO): Updated data for the purchase item.
    
    Returns:
        Updated purchase item object.
    
    Raises:
        HTTPException: If the purchase item is not found or if an error occurs during update.
    """
    return service.update(id, data)

@router.delete("/{id}")
def remove(id: str, service: PurchaseItemsService = Depends(getPurchaseItemsService)):
    """
    Deletes a purchase item by its ID.
    
    Args:
        id (str): The ID of the purchase item to delete.
    
    Returns:
        Message indicating successful deletion.
    
    Raises:
        HTTPException: If the purchase item is not found or if an error occurs during deletion.
    """
    service.remove(id)
    return {"message": f"Purchase item with ID {id} deleted successfully."}
