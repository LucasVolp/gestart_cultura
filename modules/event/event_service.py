from modules.event import (
    CreateEventUseCase,
    FindAllEventsUseCase,
    FindEventByIdUseCase,
    UpdateEventUseCase,
    DeleteEventUseCase,
    CreateEventDTO,
    UpdateEventDTO
)

class EventService:
    def __init__(self, CreateEventUseCase = CreateEventUseCase(), FindAllEventsUseCase = FindAllEventsUseCase(), FindEventByIdUseCase = FindEventByIdUseCase(), UpdateEventUseCase = UpdateEventUseCase(), DeleteEventUseCase = DeleteEventUseCase()):
        self.CreateEventUseCase = CreateEventUseCase
        self.FindAllEventsUseCase = FindAllEventsUseCase
        self.FindEventByIdUseCase = FindEventByIdUseCase
        self.UpdateEventUseCase = UpdateEventUseCase
        self.DeleteEventUseCase = DeleteEventUseCase

    def create(self, data: CreateEventDTO):
        """
        Creates a new event using the CreateEventUseCase.

        Args:
            data: Data Transfer Object containing the event information to be created.
        
        Returns:
            Created event instance.
        """
        return self.CreateEventUseCase.execute(data)
    
    def findAll(self):
        """
        Retrieves all events using the FindAllEventsUseCase.

        Returns:
            List of all event instances.
        """
        return self.FindAllEventsUseCase.execute()
    
    def findOne(self, id: str):
        """
        Finds an event by its ID using the FindEventByIdUseCase.

        Args:
            id: The ID of the event to be found.
        
        Returns:
            Event instance with the specified ID.
        """
        return self.FindEventByIdUseCase.execute(id)
    
    def update(self, id: str, data: UpdateEventDTO):
        """
        Updates an existing event using the UpdateEventUseCase.

        Args:
            id: The ID of the event to be updated.
            data: Data Transfer Object containing the updated event information.
        
        Returns:
            Updated event instance.
        """
        return self.UpdateEventUseCase.execute(id, data)
    
    def remove(self, id: str):
        """
        Deletes an event by its ID using the DeleteEventUseCase.

        Args:
            id: The ID of the event to be deleted.
        
        Returns:
            Confirmation of deletion.
        """
        return self.DeleteEventUseCase.execute(id)