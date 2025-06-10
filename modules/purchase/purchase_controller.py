from fastapi import APIRouter, Depends
from modules.purchase import PurchaseService, CreatePurchaseDTO, UpdatePurchaseDTO, PurchaseResponse

router = APIRouter(prefix="/purchase", tags=["Purchase"])

def getPurchaseService():
    return PurchaseService()

@router.get("/", response_model=list[PurchaseResponse])
def findAll(service: PurchaseService = Depends(getPurchaseService)):
    """
    Retrieves all purchases.
    
    Returns:
        List of all purchases.
    """
    return service.findAll()


@router.get("/{id}", response_model=PurchaseResponse)
def findOne(id: str, service: PurchaseService = Depends(getPurchaseService)):
    """
    Retrieves a purchase by its ID.
    
    Args:
        id (str): The ID of the purchase to retrieve.
    
    Returns:
        Purchase object if found.
    
    Raises:
        HTTPException: If the purchase is not found or if an error occurs.
    """
    return service.findOne(id)

@router.post("/", response_model=PurchaseResponse)
def create(data: CreatePurchaseDTO, service: PurchaseService = Depends(getPurchaseService)):
    """
    Creates a new purchase.
    
    Args:
        data (CreatePurchaseDTO): Data for the new purchase.
    
    Returns:
        Created purchase object.
    
    Raises:
        HTTPException: If an error occurs during creation.
    """
    return service.create(data)
    
@router.patch("/{id}", response_model=PurchaseResponse)
def update(id: str, data: UpdatePurchaseDTO, service: PurchaseService = Depends(getPurchaseService)):
    """
    Updates an existing purchase.
    
    Args:
        id (str): The ID of the purchase to update.
        data (UpdatePurchaseDTO): Updated data for the purchase.
    
    Returns:
        Updated purchase object.
    
    Raises:
        HTTPException: If the purchase is not found or if an error occurs during update.
    """
    return service.update(id, data)

@router.delete("/{id}")
def remove(id: str, service: PurchaseService = Depends(getPurchaseService)):
    """
    Deletes a purchase by its ID.
    
    Args:
        id (str): The ID of the purchase to delete.
    
    Returns:
        Message indicating successful deletion.
    
    Raises:
        HTTPException: If the purchase is not found or if an error occurs during deletion.
    """
    service.remove(id)
    return {"message": f"Purchase with ID {id} deleted successfully."}

@router.post("/pay/{purchaseId}")
def processPayment(
    purchaseId: str,
    service: PurchaseService = Depends(getPurchaseService)
):
    """
    Processes payment for a pending purchase.
    
    Args:
        purchaseId (str): The ID of the purchase to process payment for.
    
    Returns:
        Result of the payment processing with tickets and receipt generated.
    
    Raises:
        HTTPException: If the purchase is not found, already processed, insufficient balance, or other errors.
    """
    return service.processPayment(purchaseId)
