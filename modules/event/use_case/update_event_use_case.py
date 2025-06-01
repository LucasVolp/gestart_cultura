from modules.event import UpdateEventRepository, UpdateEventDTO, FindEventByIdRepository
from fastapi import HTTPException

class UpdateEventUseCase:
    def __init__(self, repository=None, findEventById=None):
        self.repository = repository or UpdateEventRepository()
        self.findEventById = findEventById or FindEventByIdRepository()
    
    def execute(self, id: str, data: UpdateEventDTO):
        """Update an existing event in the database.

        Args:
            id (str): ID of the event to be updated.
            data (UpdateEventDTO): Data transfer object containing the updated event data.

        Raises:
            HTTPException: If the event with the given ID does not exist or an error occurs.

        Returns:
            Event: Updated Event model instance.
        """
        try:
            eventExists = self.findEventById.findById(id)
            if not eventExists:
                raise HTTPException(status_code=404, detail=f"Event with ID {id} not found")
            
            if data.isEmpty():
                raise HTTPException(status_code=400, detail="No data provided for update")
            
            event = self.repository.update(eventExists, data)
            return event
        except HTTPException:
            raise
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Internal server error while updating event: {str(e)}")
        finally:
            self.repository.session.close()
            self.findEventById.session.close()
