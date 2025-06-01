from fastapi import APIRouter, Depends, HTTPException
from modules.ticket import TicketService, CreateTicketDTO, UpdateTicketDTO

router = APIRouter(prefix="/ticket", tags=["Ticket"])

def getTicketService():
    return TicketService()

@router.get("/")
def findAll(service: TicketService = Depends(getTicketService)):
    """
    Retrieves all tickets.
    
    Returns:
        List of all tickets.
    """
    return service.findAll()

@router.get("/{id}")
def findOne(id: str, service: TicketService = Depends(getTicketService)):
    """
    Retrieves a ticket by its ID.
    
    Args:
        id (str): The ID of the ticket to retrieve.
    
    Returns:
        Ticket object if found.
    
    Raises:
        HTTPException: If the ticket is not found or if an error occurs.
    """
    return service.findOne(id)

@router.post("/")
def create(data: CreateTicketDTO, service: TicketService = Depends(getTicketService)):
    """
    Creates a new ticket.
    
    Args:
        data (CreateTicketDTO): Data for the new ticket.
    
    Returns:
        Created ticket object.
    
    Raises:
        HTTPException: If an error occurs during creation.
    """
    return service.create(data)
    
@router.patch("/{id}")
def update(id: str, data: UpdateTicketDTO, service: TicketService = Depends(getTicketService)):
    """
    Updates an existing ticket.
    
    Args:
        id (str): The ID of the ticket to update.
        data (UpdateTicketDTO): Updated data for the ticket.
    
    Returns:
        Updated ticket object.
    
    Raises:
        HTTPException: If the ticket is not found or if an error occurs during update.
    """
    return service.update(id, data)

@router.delete("/{id}")
def remove(id: str, service: TicketService = Depends(getTicketService)):
    """
    Deletes a ticket by its ID.
    
    Args:
        id (str): The ID of the ticket to delete.
    
    Returns:
        Message indicating successful deletion.
    
    Raises:
        HTTPException: If the ticket is not found or if an error occurs during deletion.
    """
    service.remove(id)
    return {"message": f"Ticket with ID {id} deleted successfully."}
