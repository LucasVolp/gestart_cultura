from fastapi import APIRouter, Depends, HTTPException
from modules.receipt import ReceiptService, CreateReceiptDTO, UpdateReceiptDTO

router = APIRouter(prefix="/receipt", tags=["Receipt"])

def getReceiptService():
    return ReceiptService()

@router.get("/")
def findAll(service: ReceiptService = Depends(getReceiptService)):
    """
    Retrieves all receipts.
    
    Returns:
        List of all receipts.
    """
    return service.findAll()

@router.get("/{id}")
def findOne(id: str, service: ReceiptService = Depends(getReceiptService)):
    """
    Retrieves a receipt by its ID.
    
    Args:
        id (str): The ID of the receipt to retrieve.
    
    Returns:
        Receipt object if found.
    
    Raises:
        HTTPException: If the receipt is not found or if an error occurs.
    """
    return service.findOne(id)

@router.post("/")
def create(data: CreateReceiptDTO, service: ReceiptService = Depends(getReceiptService)):
    """
    Creates a new receipt.
    
    Args:
        data (CreateReceiptDTO): Data for the new receipt.
    
    Returns:
        Created receipt object.
    
    Raises:
        HTTPException: If an error occurs during creation.
    """
    return service.create(data)
    
@router.patch("/{id}")
def update(id: str, data: UpdateReceiptDTO, service: ReceiptService = Depends(getReceiptService)):
    """
    Updates an existing receipt.
    
    Args:
        id (str): The ID of the receipt to update.
        data (UpdateReceiptDTO): Updated data for the receipt.
    
    Returns:
        Updated receipt object.
    
    Raises:
        HTTPException: If the receipt is not found or if an error occurs during update.
    """
    return service.update(id, data)

@router.delete("/{id}")
def remove(id: str, service: ReceiptService = Depends(getReceiptService)):
    """
    Deletes a receipt by its ID.
    
    Args:
        id (str): The ID of the receipt to delete.
    
    Returns:
        Message indicating successful deletion.
    
    Raises:
        HTTPException: If the receipt is not found or if an error occurs during deletion.
    """
    service.remove(id)
    return {"message": f"Receipt with ID {id} deleted successfully."}
