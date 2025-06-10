from modules.ticket.use_case import (
    CreateTicketUseCase,
    DeleteTicketUseCase,
    FindAllTicketUseCase,
    FindTicketByIdUseCase,
    UpdateTicketUseCase,
)
from modules.ticket.dto import CreateTicketDTO, UpdateTicketDTO

class TicketService:
    def __init__(
        self, 
        CreateTicketUseCase=CreateTicketUseCase, 
        FindAllTicketUseCase=FindAllTicketUseCase, 
        FindTicketByIdUseCase=FindTicketByIdUseCase, 
        UpdateTicketUseCase=UpdateTicketUseCase, 
        DeleteTicketUseCase=DeleteTicketUseCase
    ):
        self.CreateTicketUseCase = CreateTicketUseCase()
        self.FindAllTicketUseCase = FindAllTicketUseCase()
        self.FindTicketByIdUseCase = FindTicketByIdUseCase()
        self.UpdateTicketUseCase = UpdateTicketUseCase()
        self.DeleteTicketUseCase = DeleteTicketUseCase()

    def create(self, data: CreateTicketDTO):
        """
        Creates a new ticket using the CreateTicketUseCase.

        Args:
            data: Data Transfer Object containing the ticket information to be created.
        
        Returns:
            Created ticket instance.
        """
        return self.CreateTicketUseCase.execute(data)
    
    def findAll(self):
        """
        Retrieves all tickets using the FindAllTicketUseCase.

        Returns:
            List of all tickets.
        """
        return self.FindAllTicketUseCase.execute()
    
    def findOne(self, id: str):
        """
        Retrieves a ticket by its ID using the FindTicketByIdUseCase.

        Args:
            id: The ID of the ticket to retrieve.
        
        Returns:
            Ticket instance if found.
        """
        return self.FindTicketByIdUseCase.execute(id)
    
    def update(self, id: str, data: UpdateTicketDTO):
        """
        Updates an existing ticket using the UpdateTicketUseCase.

        Args:
            id: The ID of the ticket to update.
            data: Data Transfer Object containing the updated ticket information.
        
        Returns:
            Updated ticket instance.
        """
        return self.UpdateTicketUseCase.execute(id, data)
    
    def remove(self, id: str):
        """
        Deletes a ticket by its ID using the DeleteTicketUseCase.

        Args:
            id: The ID of the ticket to delete.
        
        Returns:
            Boolean indicating successful deletion.
        """
        return self.DeleteTicketUseCase.execute(id)
