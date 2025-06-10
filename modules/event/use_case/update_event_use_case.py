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
        except HTTPException as e:
            print(f"Erro ao atualizar evento: {e.detail}")
            raise e
        except Exception as e:
            print(f"Erro ao atualizar evento: {e}")
            raise HTTPException(status_code=400, detail="Erro ao atualizar evento")
        finally:
            self.repository.session.close()
            self.findEventById.session.close()
