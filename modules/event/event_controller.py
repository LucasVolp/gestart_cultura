from fastapi import APIRouter, Depends
from modules.event import EventService, CreateEventDTO, UpdateEventDTO
from modules.user.utils.dependencies import getCurrentUser

router = APIRouter(prefix="/event", tags=["Event"])

def getEventService():
    return EventService()

@router.get("/")
def findAll(service: EventService = Depends(getEventService)):
    """
    Retrieves all events.
    
    Returns:
        List of all events.
    """
    return service.findAll()

    
@router.get("/{id}")
def findOne(id: str, service: EventService = Depends(getEventService)):
    """
    Retrieves an event by its ID.
    
    Args:
        id (str): The ID of the event to retrieve.
    
    Returns:
        Event object if found.
    
    Raises:
        HTTPException: If the event is not found or if an error occurs.
    """
    return service.findOne(id)

@router.post("/")
def create(data: CreateEventDTO, service: EventService = Depends(getEventService)):
    """
    Creates a new event.
    
    Args:
        data (dict): Data for the new event.
    
    Returns:
        Created event object.
    
    Raises:
        HTTPException: If an error occurs during creation.
    """
    return service.create(data)
    
@router.patch("/{id}")
def update(id: str, data: UpdateEventDTO, service: EventService = Depends(getEventService)):
    """
    Updates an existing event.
    
    Args:
        id (str): The ID of the event to update.
        data (dict): Updated data for the event.
    
    Returns:
        Updated event object.
    
    Raises:
        HTTPException: If the event is not found or if an error occurs during update.
    """
    return service.update(id, data)

    
@router.delete("/{id}")
def remove(id: str, service: EventService = Depends(getEventService)):
    """
    Deletes an event by its ID.
    
    Args:
        id (str): The ID of the event to delete.
    
    Returns:
        Message indicating successful deletion.
    
    Raises:
        HTTPException: If the event is not found or if an error occurs during deletion.
    """
    return service.remove(id)